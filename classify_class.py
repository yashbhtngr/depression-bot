from tensorflow import keras
from tensorflow.keras.preprocessing.text import Tokenizer
import numpy as np
import pickle

class classify_text:
    def __init__(self):
        self.model = keras.models.load_model('sentiment_classify')
        self.word_to_index = {} ## Gives the word to index mapping for the embedding layer
        with open('word_to_index.p','rb') as file:
            self.word_to_index = pickle.load(file)
    
    def classify(self,text):
        # Text is a string
        temp = text.split()
        sequence =[]
        for x in temp:
            if x in self.word_to_index:
                sequence.append((self.word_to_index)[x])
            else:
                sequence.append(0)
        test = [sequence]
        predictions = (self.model).predict(test)
        predictions = predictions[0]
        sentiment = np.argmax(predictions)
        return sentiment







    

    

    
    

