from googletrans import Translator, constants
from pprint import pprint
def detect1(text):
    
    #for detection
    translator = Translator()
    detection = translator.detect(text)
    print("Language code:", detection.lang)
    return detection.lang
# print("Confidence:", detection.confidence)
#for translation of text 
def translate1(text,lang):
    translator = Translator()
    translation = translator.translate(text, dest=lang)
    print(f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})")
    return  translation

def language():   
    print("Total supported languages:", len(constants.LANGUAGES))
    print("Languages:")
    pprint(constants.LANGUAGES)
    return constants.LANGUAGES