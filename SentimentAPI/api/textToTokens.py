from keras.preprocessing.text import Tokenizer
from sklearn.preprocessing import LabelEncoder
from keras.utils import pad_sequences

class testToTokens:
    def __init__(self):
        pass
    def Tokens(self, plaintext):
        text = []
        print(plaintext)
        text.append(plaintext)
        print(text)
        vocab_size = 3000 # choose based on statistics
        oov_tok = ''
        max_length = 200
        # text = ["This is good i have ever ate"]
        tokenizer = Tokenizer(num_words = vocab_size, oov_token=oov_tok)
        tokenizer.fit_on_texts(text)
        sequences = tokenizer.texts_to_sequences(text)
        print("sequences",sequences)
        # pad the sequence
        padded = pad_sequences(sequences, padding='post', maxlen=max_length)
        print(padded)
        return padded
