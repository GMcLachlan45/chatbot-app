from ast import parse
from collections import deque
from functools import reduce
import nltk
import re
import wikipediaapi
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
                    returnedStatement = self.lastpage.summary.split("\n")[0]
                else:
                    spliterator = self.lastpage.summary.split(".")
                    returnedStatement = spliterator[0]+spliterator[1]+spliterator[2]
                return returnedStatement
            if "no":
                returnedStatement = "Okay. Here's a link to the page if you change your mind: " + self.lastpage.fullurl
                self.lastpage =""
                self.longer = False

                    

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
                returnedStatement = "It doesn't look like there's a Wikipedia page on " +lookupQuery+". "

        base =chat(check)


        
        if(sentiment<-.8):
            base = "That doesn't sound good at all... " + base +" If you feel that bad, you should probably go to the hospital. Would you like directions to the nearest hospital?"
        
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

            if "they" in check:
                base = "Please tell " + ne_rec[len(ne_rec)-1] + ": \"" + base + "\""
                self.lastname = True
                
            if "They" in check:
                base = "Please tell " + ne_rec[len(ne_rec)-1] + ": \"" + base + "\""
                self.lastname = True
            if "their" in check:
                base = "Please tell " + ne_rec[len(ne_rec)-1] + ": \"" + base + "\""
                self.lastname = True
                
            if "Their" in check:
                base = "Please tell " + ne_rec[len(ne_rec)-1] + ": \"" + base + "\""
                self.lastname = True
                
            if "I'm" in check:
                base = "Hello, " + ne_rec[0] + ". " + base
        else:
            if "They" in check:
                base = "Tell them: \"" + base + "\""
            if "they" in check:
                base = "Tell them: \"" + base + "\""

            

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