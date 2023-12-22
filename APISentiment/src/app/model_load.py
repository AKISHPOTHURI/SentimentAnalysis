from keras.preprocessing.text import Tokenizer
import keras
class load_model():
    @staticmethod
    def load():
        model = keras.models.load_model('app\sentimentModel\model2.h5')
        return model