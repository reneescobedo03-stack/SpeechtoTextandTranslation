import speech_recognition as sr
from translate import Translator


# Speech Recognition class
class SpeechRecognizer:

    #__init__ stores file path and creates recognizer
    def __init__(self, audio_file):
        self.audio_file = audio_file
        self.recognizer = sr.Recognizer()

    #get_text returns text for translation use
    def get_text(self):
        with sr.AudioFile(self.audio_file) as source:
            audio = self.recognizer.record(source)

        #Return transcribed text using Google Speech Recognition
        return self.recognizer.recognize_google(audio)

# Translation Class   
class TranslatorService:
    
    #__init__ "es" is passed for the target language(español), translator is created
    def __init__(self, target_lang="es"):
        self.translator = Translator(to_lang=target_lang)
    
    #Translate and return translated text
    def translate(self,text):
        return self.translator.translate(text)

#File path where audio file is stored
audio_path = r"C:\Users\notco\harvard.wav"

#SpeechRecognizer class with audio_path
speech = SpeechRecognizer(audio_path)

#Translator class with language
translator = TranslatorService("es")
#Try speech recognition and translation, if error occurs it is printed
try:
    text = speech.get_text()
    print("Original:", text, "\n")

    print("-----------------------------------------------\n",  )

    translated = translator.translate(text)
    print("Translation:", translated)

except Exception as e:
    print("Error:", e)