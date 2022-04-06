from ast import parse
from collections import deque
from functools import reduce
import nltk
import re

import wikipediaapi #use of wikipediaAPI

from time import sleep
import googlemaps #use of Google Maps Services Python API 

from chat import chat
from random import randint


from plugins.agent_plugin import AgentPlugin
from nltk.corpus import wordnet
from nltk.sentiment.vader import SentimentIntensityAnalyzer

class Agent:
    lastname = False
    lastpage = ""
    longer = False
    wiki_wiki = wikipediaapi.Wikipedia('en')

    wantsDirections = False
    gmaps =googlemaps.Client(key= str(open("googleapikey.txt", "r+").read())) #only use when you think it's ready'


    def __init__(self, plugins, nltk_dependencies):
        print("Downloading nltk dependencies")
        for dependency in nltk_dependencies:
            nltk.download(dependency)

        self.plugins = list(map(lambda x: x(), plugins))

    def query(self, query) -> str:
        #return chat(query)

        print(self.plugins)
        # Spelling Check, call a function within agent to fix the query to realistic words 
        check = self.plugins[0].parse(query)
        # Part of speach tagging 
        pos_tag = self.plugins[1].parse(query)
        # Named Entity Recognition: Recognize names given and append
        ne_rec = self.plugins[2].parse(pos_tag) 
        # saying "hello" or "tell jessica to" or something to the front 
        # CoReference: Figure out if the query is about the user or their patient is talking about 
        sentiment = self.plugins[3].parse(query)
        
        print(ne_rec)
        print(sentiment)
        # Sentiment for easy interchangeable sentences

        ## Add all of the sections, and return Dr phils smart answer to the query all 3
        
        
        check = check.lower()




        if self.lastpage:
            if "yes" in  check:
                returnedStatement = ""
                if self.longer==True:
                    self.longer==False
                    returnedStatement = self.lastpage.summary.split("\n")[0]
                else:
                    spliterator = self.lastpage.summary.split(".")
                    returnedStatement = "Okay... here it is:" + spliterator[0]+"."+spliterator[1]+"."+spliterator[2] +"."
                self.lastpage=""
                return returnedStatement
            if "no":
                returnedStatement = "Okay. Here's a link to the page if you change your mind: " + self.lastpage.fullurl
                self.lastpage =""
                self.longer = False
                return returnedStatement

        if self.wantsDirections:
            if "yes" in  check:
                returnedStatement =  "Okay, " + self.getDirections()
                ##give the directions and return it
                self.wantsDirections = False
                return returnedStatement
            if "no":
                returnedStatement = "Okay. If you change your mind, then just ask me for directions to the hospital."
                self.wantsDirections= False
                return returnedStatement


        if "direction" in check or  "how to get to" in check:
            if "hospital" in check or "clinic" in check:
                returnedStatement =  "Okay, " + self.getDirections()
                ##give the directions and return it
                return returnedStatement
            else:
                return "Sorry, I'm only qualified to give you directions to the hospital."
            
            
        if "look up" in check:
            lookupQuery = check.split("look up")[1].strip(":;.,\" '!?").replace(" ", "_")


            print(lookupQuery)

            page_py = self.wiki_wiki.page(lookupQuery)
            if page_py.exists():
                medicalList =["medicine", "drug", "illness", "disease", "demic", "health", "infection", "inflamation"]
                categories=page_py.categories
                spliterator = page_py.summary.split(".")
                returnedStatement = "Okay, here's what I found: " +spliterator[0]+"."+spliterator[1]+"."+spliterator[2] +"...\nWould you like the rest of the summary?"
                self.lastpage = page_py

                for category in categories.keys():
                    medicinecheck = False

                    for x in medicalList:
                        if medicinecheck:
                            break        
                        if x in category.lower():
                            medicinecheck = True

                    if medicinecheck:
                        break 
                if medicinecheck:
                    self.longer = True
                    return returnedStatement
                else:
                    return "I'm not sure if that has anything to do with medicine... Are you sure?"
            else:
                returnedStatement = "It doesn't look like there's a Wikipedia page on " +lookupQuery+"."

        base =chat(check)


        
        if(sentiment<-.7):
            self.wantsDirections = True
            base = "That doesn't sound good at all... " + base +".. If you feel that bad though, you should probably go to the hospital. Would you like directions to the nearest hospital?"
        elif(sentiment<-.5):
            oh_nos = ["I'm sorry to hear that! ",
                      "That doesn't sound very good. ",
                      "I'm sorry you feel this way. ",
                      "I hope I can help you feel better! ",
                      "Hold on, we'll get you feeling better in no time! ",
                      "I'll work my hardest to help you feel better. "]
            base = oh_nos[randint(0, len(oh_nos)-1 ) ] + base
        

        
        

        if len(ne_rec)>0:
            check = query.split()

            if "they" in check or "They" in check or "their" in check or "Their" in check:
                base = "Please tell " + ne_rec[len(ne_rec)-1] + ": \"" + base + "\""
                self.lastname = True
            if "I'm" in check:
                base = "Hello, " + ne_rec[0] + ". " + base
        else:
            if "They" in check or "they" in check:
                base = 'Tell them: "' + base + '"'

            
        sleep(2.5)
        return base

    
    def pos_tag(self, query):
        token = nltk.word_tokenize(query)
        tagged = nltk.pos_tag(token)
        
        return tagged
   
    
    ## self.synonyms(word, pos_tag) returns list of synonyms for inputted word with the pos_tag
    ## has error catching now
    def synonyms(self, word, pos_tag):
        word = word.lower()
        try:
            synonyms = set()
            synonyms.add(word)
            valid_sets = [s for s in wordnet.synsets(word, pos = pos_tag) if s.name().startswith(word)]
            while len(synonyms) < 3 and valid_sets:
                syn_set = valid_sets.pop(0)
                print(syn_set)
                if syn_set.name().startswith(word):
                    for l in syn_set.lemmas():
                        name = l.name().replace("_", " ")
                        synonyms.add(name.lower())
            
            print(synonyms)

            return synonyms
        except:
            print("Encountered an error; make sure you inputted a valid word to get synonyms.")
            return word
    
        
    def getDirections(self):
        #find the user's location via geolocation    and reverse geocoding
        response = self.gmaps.geolocate()
        orig = response['location']
        origstr=str(orig['lat'])+","+ str(orig['lng']) #formats the latlng into proper coordinates

        response = self.gmaps.reverse_geocode(origstr)
        results = response[0]['address_components']

        origAdd = results[0]['short_name']+" " + results[1]['short_name']

        #get the desired location
        response = self.gmaps.places(location = origstr, type = "hospital")
        results = response['results'][0]
        
        name = results['name']

        dest = results['formatted_address']

        #Get the directions, and format them as a string
        directions_result = self.gmaps.directions(orig, dest)
                  
        returnStatement = "I see that you're around " + origAdd +". The closest hospital is "+ name+ ". To get there from your current location: "
        for i in range (0, len(directions_result[0]['legs'][0]['steps']) - 1):
            j = directions_result[0]['legs'][0]['steps'][i]['html_instructions'] 
            returnStatement = returnStatement + j
            if i != len(directions_result[0]['legs'][0]['steps']) - 2:
                returnStatement = returnStatement+ ", then "

        i =len(directions_result[0]['legs'][0]['steps'])-1
        returnStatement +=". " + directions_result[0]['legs'][0]['steps'][i]['html_instructions']
        #clean up the HTML tags
        returnStatement = returnStatement + ". I hope you get there safely!"
        returnStatement = re.sub(re.compile('<.*?>'), ' ', returnStatement).replace("  ", " ").replace(" ,", ",").replace(" .", ".")
        sleep(1)
        return returnStatement