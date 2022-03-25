import json 
import numpy as np 
import tensorflow as tf
from tensorflow import keras
from keras.models import Sequential
from keras.layers import Dense, Embedding, GlobalAveragePooling1D, LSTM, Dropout
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from sklearn.preprocessing import LabelEncoder
import pickle
import re
import nltk
from nltk.corpus import wordnet
from functools import lru_cache
import itertools


class Trainer:
    def __init__(self, input_file):
        self.input_file = input_file
    
    def train(self):
        with open(self.input_file) as file:
            data = json.load(file)
        
        training_sentences = []
        training_labels = []
        labels = []
        responses = []

        for i, (intent_key, intent) in enumerate(data.items()):
            for pattern in intent['patterns']:
                synonymous_sentences = self.get_synonymous_sentences(re.findall(r"\w+", pattern))
                for sentence in synonymous_sentences:
                    training_sentences.append(sentence)
                    training_labels.append(intent_key)
            
            responses.append(intent['responses'])
            labels.append(i)
        
        num_intents = len(labels)
        lbl_encoder = LabelEncoder()
        lbl_encoder.fit(training_labels)
        training_labels = lbl_encoder.transform(training_labels)

        vocab_size = 50000      # limit vocabulary to 50k most common words
        max_len = 20            # maximum sequence length (words)
        oov_token = "<OOV>"

        tokenizer = Tokenizer(num_words=vocab_size, oov_token=oov_token) # adding out of vocabulary token
        tokenizer.fit_on_texts(training_sentences)
        sequences = tokenizer.texts_to_sequences(training_sentences)
        padded_sequences = pad_sequences(sequences, truncating='post', maxlen=max_len)
        print(padded_sequences)

        embedding_vector_features=45

        model=Sequential()

        model.add(Embedding(vocab_size,embedding_vector_features,input_length=max_len))

        model.add(LSTM(128,activation='relu',return_sequences=True))

        model.add(Dropout(0.2))

        model.add(LSTM(128,activation='relu'))

        model.add(Dropout(0.2))

        model.add(Dense(32,activation='relu'))

        model.add(Dropout(0.2))

        model.add(Dense(num_intents,activation='softmax'))

        model.compile(loss='sparse_categorical_crossentropy',optimizer='adam',metrics=['accuracy'])


        epochs = 45
        history = model.fit(padded_sequences, np.array(training_labels), epochs=epochs)

        # saving model
        model.save("chat_model")

        # saving tokenizer
        with open('tokenizer.pickle', 'wb') as handle:
            pickle.dump(tokenizer, handle, protocol=pickle.HIGHEST_PROTOCOL)

        # saving label encoder
        with open('label_encoder.pickle', 'wb') as ecn_file:
            pickle.dump(lbl_encoder, ecn_file, protocol=pickle.HIGHEST_PROTOCOL)

    ## self.synonyms(word, pos_tag) returns list of synonyms for inputted word with the pos_tag
    ## has error catching now
    @lru_cache(maxsize=None)
    def synonyms(self, word, pos_tag):
        word = word.lower()
        try:
            synonyms = set()
            synonyms.add(word)
            lemmas = itertools.islice(itertools.chain.from_iterable([s.lemmas() for s in wordnet.synsets(word, pos = pos_tag)]), 2)
            for l in lemmas:
                name = l.name().replace("_", " ")
                synonyms.add(name.lower())
            
            return synonyms
        except:
            print("Encountered an error; make sure you inputted a valid word to get synonyms.")
            return word

    def get_synonymous_sentences(self, words: 'list[str]', idx: int = 0):
        if (idx == len(words)): return [" ".join(words)]
        res = []
        for w in self.synonyms(words[idx], None): #make sure get_synonyms includes self
            words_new = words.copy()
            words_new[idx] = w
            res += self.get_synonymous_sentences(words_new, idx + 1)
        return res 

    