# 310 Project: Chatbot App

## Individual Project Member:

Gabriel McLachlan 86257383

##### Original Project Team 31 Members:

Mohammad Al-surkhi

Jordan Colledge

Gabriel McLachlan

Jordan Ribbink

Nathan Wright

## Project Repo: 
https://github.com/GMcLachlan45/chatbot-app/

## Project Description and Purpose

Description copied and pasted from the Project Plan:
The project consists of a chatbot built in Electron; the chatbot comes with a generic visual interface to ensure simplicity of use and understanding.

The chatbot takes on the role of a doctor, who can be asked questions about different symptoms and describe the likely illness and remedy. Thus, the user takes on the role of a patient.

The purpose of the app is to make a simple diagnostic tool, so that the user can diagnose their possible illnesses without having to leave their home. A doctor will necessarily be a better diagnostic tool than this app, but it's meant to be functional just the same.

## Installation and Usage

### Requirements

- Node JS - https://nodejs.org/en/
- NVM (optional) - https://github.com/nvm-sh/nvm
- Python 3 - https://www.python.org/downloads/
- Pyenv (optional) - https://github.com/pyenv/pyenv
- Pyenv-virtualenv (optional) - https://github.com/pyenv/pyenv-virtualenv
- Google Maps Services API key (optional) -  https://developers.google.com/maps/documentation/javascript/get-api-key

Open terminal in the root of the project and run this command:

1.  Install NPM dependencies

    ```bash
    npm install
    ```

2.  Install Python dependencies

    - OPTIONAL. Install [Pyenv](https://github.com/pyenv/pyenv) & [Pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv) to manage Python environment. Follow instructions provided within documentation

      Create a new virutalenv in Python 3.8.10 and activate it

      ```bash
      pyenv virtualenv 3.8.10 ${YOUR_VIRTUALENV_NAME}
      pyenv activate ${YOUR_VIRTUALENV_NAME}
      ```

    - Install requirements via pip by running the following command from the root folder of the project

      ```bash
      pip install -r requirements.txt
      ```

3.  Run this command to train the bot's neural network:

    ```bash
    npm run train
    ```

    If this gives an error, run this instead:

    ```bash
    python util/train.py
    ```

    This may take a bit of time, but after it's run once, it doesn't need to be run again.

4.  Launch development server using the following bash command in root of project

    ```bash
    npm run start
    ```

    The chatbot should launch.
    
5. (Optional) Get an API key for Google Maps Services

    Visit [Google API keys documentation](https://developers.google.com/maps/documentation/javascript/get-api-key)
    
    Make sure to get the  [Geocoding API](https://developers.google.com/maps/documentation/geocoding/overview), [Places API](https://developers.google.com/maps/documentation/places/web-service), [Geolocation API](https://developers.google.com/maps/documentation/geolocation/overview), and [Directions API](https://developers.google.com/maps/documentation/directions).
    
    Replace the contents of googleapikey.txt with the API key.

## List of API's used

### Wikipedia API

The Wikipedia API has been integrated into the chatbot so that if the user wants to know a bit more about what the Doctor is talking about, all they need to put is "Look up ______", and if it's medical related, the Bot will pull up the info from Wikipedia. 

The lookup simply uses the function to get the page's information, but determining whether something is related to medicine is actually much more subtle. It looks through the categories of the topic and sees if there are specific keywords within the categories.
    
This helps to fill out where the team identified were some pretty big gaps in conversation from A2 and A3. If the Bot doesn't know something, then it can search it up online. The ability to distinguish between medical topics also adds to the more human side of the Bot.
    
### The Google APIs

All 4 of the next APIs used were integrated all together to give directions to a dynamically chosen location (the closest hospital to the user). If the user is feeling particularly bad, or if the bot detects that something sounds particularly bad, then the user can inquire about the directions to the nearest hospital.
    
This works to add an extra, more personal and interactive feature to the Bot, one that grounds it more in the real world then a set of relatively disconnected back and forths.
    
Though Each individual api isn't extensively used, they all have their queries, parsing and formatting. More information below.
    
#### Google Geolocation API

Geolocation is a tool that uses nearby cell towers and wifi modems to triangulate the users latitude and longitude with a fair bit of accuracy (not 100% in more rural places, even UBCO).

Within the getDirections() function to find the general latitude and longitude of the user. This is then converted into a string for further use within the function.

#### Google Geocoding API

Reverse Geocoding is the process of taking a set of coordinates and approximating a formatted address based on nearby roads and other addresses.

Within the system, we take the latitude and longitude found via geolocation, and convert it into a named location. This location is output along with the rest of the directions, and lets the user know that the Bot knows the approximate location, which can help give a sense of security that a scared and sick user may need.

#### Google Places API

The Places API is a useful tool to find relevant destinations. In general this could be used to determine points of interest based on what the user wants to go to, but for the Bot he is restricted to giving directions to the nearest hospital.

For this system, we take the position of the user, and use it as an origin location to bias the results to the closest and most relevent result available. Using Places itself helps to make the system more dynamic, as depending where you are, the nearest hospital will change, making the system much more flexible.

#### Google Directions API

Directions is pretty self explanitory. Once we have the user's location, and the hospital's address, the Directions API determines the fastest path between the two and the directions that need to be taken to get there.

Once the directions to the nearest hospital have been determined, the system takes all of the relevant strings, brings them together, removes the html parts and concatinates it with the rest of the Bot's response. 

Though the wall of text isn't ideal, it makes much more sense that someone would be typing this out beforehand rather than in small segments. Even a user that didn't have GPS could take those instructions print them out, and follow them to where they needed to go. I also personally believe that this makes him a lot more like a first responder, and a lot more human.

### API Conclusion

Those were the 5 APIs integrated into my final rendition of Doctor Phil. 

The Wikipedia integration helps to extend conversational potential, adds to its humanness through asking about relevance,  and help to clarify anything that the Doctor has said. 

Meanwhile, the Google Maps integration helps to add a flexible, reliable and useful tool to the Doctor's coversational toolset while making him seem more human and part of this world.

Further inquiry can be had through looking at the implementation in src/agent/agent.py. 

## Simplified Project Structure

In the individual project, there were no added files to the bot. All of the work was done within src/agent/agent.py.

There are a few new files for user setup (googleapikey.txt) and the Final Project Report though. As such, I've added them here.

. &nbsp;<br />
├── ...&nbsp;<br />
├── googleapikey.txt<br />
├── config &nbsp;<br />
│ &nbsp; └── dataset.json &nbsp; -> Stores our dataset for NLP<br />
├── documentation &nbsp;<br />
│ &nbsp; ├── 30-Turn Convo.pdf &nbsp; -> Stores images of the thirty-turn conversation as stipulated in requirements. <br />
│ &nbsp; ├── DFD's.pdf &nbsp; -> Stores the Data Flow Diagrams and descriptions of them. <br />
│ &nbsp; └── Unit Test Descriptions.pdf &nbsp; -> Stores descriptions of the unit tests used.
├── Project-Report-A2.pdf &nbsp; -> Our project report document for A2<br />
├── Project-Report-A3.pdf &nbsp; -> Our project report document for A3<br />
├── Project-Report-FINAL.pdf &nbsp; -> A copy of my final project report for the individual assignment<br />
├── src &nbsp;<br />
│ &nbsp; ├── agent &nbsp;<br />
│ &nbsp; │ &nbsp; ├── plugins &nbsp; <br />
│ &nbsp; │ &nbsp; ├── tests &nbsp;<br />
│ &nbsp; │ &nbsp; │ &nbsp; └── agent_test.py &nbsp; -> Unit tests as used by Pytest.
│ &nbsp; │ &nbsp; └── agent.py &nbsp; -> The Python agent. Essentially used to read a query, manipulate it, and return the results.<br />
│ &nbsp; │ &nbsp; └── chat.py &nbsp; -> The Python agent. Essentially used to read a query, manipulate it, and return the results.<br />
│ &nbsp; ├── main &nbsp;<br />
│ &nbsp; │ &nbsp; ├── nlp-service.ts &nbsp;&nbsp;&nbsp;&nbsp;<- &nbsp;Interfaces with Node NLP module and trains from dataset &nbsp;<br />
│ &nbsp; │ &nbsp; ├── main.ts &nbsp;&nbsp;&nbsp;<- &nbsp;Electron entry point, also includes IPC module for communicating frontend<br />
│ &nbsp; ├── renderer &nbsp;<br />
│ &nbsp; │ &nbsp; ├── App.vue &nbsp;&nbsp;&nbsp;<- &nbsp;Vue entry point <br />
│ &nbsp; │ &nbsp; ├── components &nbsp;&nbsp;&nbsp;<- &nbsp;Component structure following atomic design principles<br />
│ &nbsp; │ &nbsp; │ &nbsp; ├── atoms &nbsp;&nbsp;&nbsp;<- &nbsp;Smallest component unit in atomic design<br />
│ &nbsp; │ &nbsp; │ &nbsp; │ &nbsp; ├── ChatMessage.vue &nbsp;&nbsp;&nbsp;<- &nbsp;Vue component for chat messages<br />
│ &nbsp; │ &nbsp; │ &nbsp; │ &nbsp; └── TypingMessage.vue &nbsp;&nbsp;&nbsp;<- &nbsp;Vue component for "user is typing..."<br />
│ &nbsp; │ &nbsp; │ &nbsp; ├── molecules &nbsp;&nbsp;&nbsp;<- &nbsp;Medium sized component unit<br />
│ &nbsp; │ &nbsp; │ &nbsp; │ &nbsp; ├── ChatBar.vue &nbsp;&nbsp;&nbsp;<- &nbsp;Vue component for chat bar<br />
│ &nbsp; │ &nbsp; │ &nbsp; │ &nbsp; ├── ChatBox.vue &nbsp;&nbsp;&nbsp;<- &nbsp;Vue component for chat box (where messages go)<br />
│ &nbsp; │ &nbsp; │ &nbsp; │ &nbsp; └── ChatHeader.vue &nbsp;&nbsp;&nbsp;<- &nbsp;Chat header component (recipient picture+name)<br />
│ &nbsp; │ &nbsp; │ &nbsp; └── organisms &nbsp;&nbsp;&nbsp;<- &nbsp;Largest component unit (full functioning features)<br />
│ &nbsp; │ &nbsp; │ &nbsp; &nbsp; &nbsp; └── ChatContainer.vue &nbsp;&nbsp;&nbsp;<- &nbsp;Chat container component (full chat feature)<br />
│ &nbsp; │ &nbsp; ├── index.ejs &nbsp;&nbsp;&nbsp;<- &nbsp;Main HTML template where Vue is injected<br />
│ &nbsp; │ &nbsp; ├── index.ts &nbsp;&nbsp;&nbsp;<- &nbsp;Webpack entry point<br />
│ &nbsp; │ &nbsp; ├── models &nbsp;&nbsp;&nbsp;<- &nbsp;Stores reusable object models (i.e. classes/data structures)<br />
│ &nbsp; │ &nbsp; │ &nbsp; ├── message.ts &nbsp;&nbsp;&nbsp;<- &nbsp;Class to identify a sent message<br />
│ &nbsp; │ &nbsp; │ &nbsp; ├── service.ts &nbsp;&nbsp;&nbsp;<- &nbsp;Abstract class representing stateful services injected into Vue<br />
│ &nbsp; │ &nbsp; │ &nbsp; └── user.ts &nbsp;&nbsp;<-Class to identify users in chat<br />
│ &nbsp; │ &nbsp; ├── services &nbsp;<br />
│ &nbsp; │ &nbsp; │ &nbsp; ├── chat-service.ts &nbsp;&nbsp;&nbsp;<- &nbsp;Service to manipulate chat state and provide responses from AI<br />
│ &nbsp; │ &nbsp; │ &nbsp; └── services.ts &nbsp;&nbsp;&nbsp;<- &nbsp;Services initializer plugin which is installed into Vue (inits all services)<br />
│ &nbsp; │ &nbsp; ├── store &nbsp;&nbsp;&nbsp;<- &nbsp;Configuration for Vuex store (state management) <br />
│ &nbsp; │ &nbsp; │ &nbsp; ├── createStore.ts &nbsp;&nbsp;&nbsp;<- &nbsp;Initializer for store (object factory)<br />
│ &nbsp; │ &nbsp; │ &nbsp; └── modules &nbsp;&nbsp;&nbsp;<- &nbsp;Stores all modules involved in store<br />
│ &nbsp; │ &nbsp; │ &nbsp; &nbsp; &nbsp; └── chat.ts &nbsp;&nbsp;&nbsp;<- &nbsp;Chat module for store (manages chat state for chat service)<br />
│ &nbsp; │ &nbsp; └── util &nbsp;&nbsp;&nbsp;<- &nbsp;Misc utilities<br />
│ &nbsp; │ &nbsp; &nbsp; &nbsp; ├── createApp.ts &nbsp;&nbsp;&nbsp;<- &nbsp;Factory to create Vue app with desired configuration<br />
│ &nbsp; │ &nbsp; &nbsp; &nbsp; └── inject-context.ts &nbsp;&nbsp;&nbsp;<- &nbsp;Helper function for injecting key into Vue/components (for DI)<br />
│ &nbsp; └── ... &nbsp;<br />
├── util &nbsp; <br />
│ &nbsp; ├── train.py &nbsp; -> A script used to train TensorFlow. <br />
│ &nbsp; └── trainer.py &nbsp; -> Utility for configuration used in train.py. <br />

**NOTE:** Not all files are included. Configuration files and similar files of low relevance (added clutter) are removed.

**NOTE:** Summary of Python files is very simplified.

## Vue Components (pseudo classes)

### ChatMessage.vue &lt;ChatMessage&gt;

Props (arguments):

- message -> Message (represents message object containing content/date/sender)

### TypingMessage.vue &lt;TypingMessage&gt;

Props (arguments):

- user -> User (represents user typing)

### ChatBar.vue &lt;ChatBar&gt;

Props (arguments): N/A

### ChatBox.vue &lt;ChatBox&gt;

Props (arguments): N/A

### ChatHeader.vue &lt;ChatHeader&gt;

Props (arguments):

- name -> String (represents name of user in header)

### ChatContainer.vue &lt;ChatContainer&gt;

Props (arguments): N/A

**NOTE:** Prop typings are denoted by [propName] -> [type]. They correspond with native TypeScript types OR typings found in our src/models folder. HTML selectors (class names) are indicated by "[file].vue &lt;[selector]&gt;"

**NOTE**: While vue components are phyiscally represented as classes in code/memory and generally function like so, I don't necessarily know if it is the correct nomenclature. However , based upon the requirements, we can call them this.

Vue technically abides by the MVC (Model-View-Controller structure) where the View is connected two-way data bindding to the Controller (i.e. JS in Vue component). Models are represented as classes in our "src/models" folder

## Models

├── models &nbsp;&nbsp;&nbsp;<- &nbsp;Stores reusable object models (i.e. classes/data structures)<br />
│ &nbsp; ├── message.ts &nbsp;&nbsp;&nbsp;<- &nbsp;Class to identify a sent message<br />
│ &nbsp; ├── service.ts &nbsp;&nbsp;&nbsp;<- &nbsp;Abstract class representing stateful services injected into Vue<br />
│ &nbsp; └── user.ts &nbsp;&nbsp;<-Class to identify users in chat<br />

### Message.ts (Message)

Class members:

- date: Date (message date sent)
- sender: User (message sender object)
- message: string (message body)

### Service.ts (_abstract_&nbsp; Service)

Class members:

- protected app: Vue.App (pointer to Vue App instance)

### User.ts (User)

Class members:

- name: string (represents user name)
- typing: boolean (represents whether user is typing, default=false)
- photo?: string (represents user photo URL, default=undefined)


## Possible API Elements

With a bot as complex as ours, there are a number of different functionalities that could be exposed or used to create our own API.

1. Extract the synonyms function (found in util/trainer.py and src/agents/agent.py) to find the synonyms for a specific word, occupying a specific part of speech.
2. Extract spellcheck.py to have a simple spellcheck function using Python's spellcheck library.
3. Extract get_synonymous_sentences (found in src/agents.py) to get sentences that are "one synonym away" from the input sentence.
4. Extract config/dataset.json for a basic map from symptoms to diagnoses to be used in a similar doctor-like or other healthcare-oriented program.
5. Extract the functions to train the neural network (from util/trainer.py) based on all the synonyms for a given word.
