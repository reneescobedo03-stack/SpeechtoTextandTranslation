import speech_recognition as sr
from translate import Translator
import os


# Speech Recognition class
class SpeechRecognizer:

    #__init__ stores file path and creates recognizer
    def __init__(self, audio_file):
        self.audio_file = audio_file
        self.recognizer = sr.Recognizer()

    #get_text returns text for translation use
    def get_text(self):
        try:
            with sr.AudioFile(self.audio_file) as source:
                audio = self.recognizer.record(source)

            #Return transcribed text using Google Speech Recognition
            return self.recognizer.recognize_google(audio)
        
        except sr.UnkownValueError:
            return "Error: Speech could not be understood."
        except sr.RequestError:
            return "Error: Could not connect to speech recognition service."
        except FileNotFoundError:
            return "Error: Audio file not found."

# Translation Class   
class TranslatorService:
    
    #__init__ "es" is passed for the target language(español), translator is created
    def __init__(self, target_lang="es"):
        self.translator = Translator(to_lang=target_lang)
    
    #Translate and return translated text
    def translate(self,text):
        try:
            return self.translator.translate(text)
        except Exception:
            return "Error: Translation failed. "
 #Main program code       
def main():
    print("Speech to Text and Translation Program\n")

#File path where audio file is stored
    audio_path = input("Enter the path to your audio file: ").strip()
    #Output error if file does not exist
    if not os.path.exists(audio_path):
        print("Error: File does not exist.")
        return
    #Allow choice for translation language
    print("\nChoose translation langauge:")
    print("1. Spanish (es)")
    print("2. French (fr)")
    print("3. German (de)")

    choice = input ("Enter choice (1-3): ")

    lang = {"1": "es", "2": "fr", "3": "de"}
    #obtain users choice
    target_lang = lang.get(choice)
    #SpeechRecognizer class with audio_path
    speech = SpeechRecognizer(audio_path)

    #Translator class with language choice
    translator = TranslatorService(target_lang)


    #Printing speech
    text = speech.get_text()
    print("Original:", text, "\n")

    print("-----------------------------------------------\n",  )
    #Printing translation of text
    translated = translator.translate(text)
    print("Translation:", translated)

if __name__ == "__main__":
    main()