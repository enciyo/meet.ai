import speech_recognition as sr

class SpeechRecognition:
    def __init__(self, language="tr-TR"):
        self.recognizer = sr.Recognizer()
        self.language = language

    def recognize(self, audio_input):
        with sr.AudioFile(audio_input) as source:
            audio = self.recognizer.record(source)
        try:
            return str(self.recognizer.recognize_google(audio, language=self.language))
        except sr.UnknownValueError:
            return "Google Web Speech API could not understand audio"
        except sr.RequestError as e:
            return f"Could not request results from Google Web Speech API; {e}"
