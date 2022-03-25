# 310 Project: Chatbot App

## Individual Project Member:

Gabriel McLachlan 86257383

## Original Project Team 31 Members:

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

## Simplified Project Structure

NEW TO Individual Project:

((((((TODO)))))))

Some files for A3 are not included for this list, as they're simply used by utilities such as TensorFlow or NLTK, or may be obsolete.

. &nbsp;<br />
├── ...&nbsp;<br />
├── config &nbsp;<br />
│ &nbsp; └── dataset.json &nbsp; -> Stores our dataset for NLP<br />
├── documentation &nbsp;<br />
│ &nbsp; ├── 30-Turn Convo.pdf &nbsp; -> Stores images of the thirty-turn conversation as stipulated in requirements. <br />
│ &nbsp; ├── DFD's.pdf &nbsp; -> Stores the Data Flow Diagrams and descriptions of them. <br />
│ &nbsp; └── Unit Test Descriptions.pdf &nbsp; -> Stores descriptions of the unit tests used.
├── Project Report.docx &nbsp; -> Our project report document<br />
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
