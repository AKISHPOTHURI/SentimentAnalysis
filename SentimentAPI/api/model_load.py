from keras.preprocessing.text import Tokenizer
import keras
class load_model():
    @staticmethod
    def load():
        model = keras.models.load_model('model\LSTMModelV1.h5')
        return model