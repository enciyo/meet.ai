from audio_recorder import AudioRecorder
from google_meet_connector import GoogleMeetConnector
from speech_rec import SpeechRecognition
from summarizer import Summarizer
import threading
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class MeetBot:
    def __init__(self, meet_url, user_name, output_file_name, language="tr-TR", api_key=None):
        self.meet_url = meet_url
        self.user_name = user_name
        self.output_file_name = output_file_name
        self.google_meet_connector = GoogleMeetConnector()
        self.audio_recorder = AudioRecorder(output_filename=output_file_name)
        self.speech_recognition = SpeechRecognition(language=language)
        self.summarizer = Summarizer(api_key=api_key, language=language)

    def on_finish(self):
        logging.info("Google meet katılım bitti")
        self.audio_recorder.stop_recording()
        try:
            logging.info("Dosya okumaya çalışıyoruz")
            text = self.speech_recognition.recognize(self.output_file_name)
            text = self.summarizer.summarize(text)
            logging.info(f"Recognized text: {text}")
        except Exception as e:
            logging.error(f"Error during speech recognition: {type(e).__name__} - {e}")

    def start(self):
        logging.info(f"Starting MeetBot with url: {self.meet_url}, user: {self.user_name}, output file: {self.output_file_name}")
        meet_thread = threading.Thread(
            target=self.google_meet_connector.join_google_meet,
            args=(self.meet_url, self.user_name, self.on_finish)
        )
        meet_thread.start()

        # Ses kaydını ayrı bir iş parçacığında başlat
        record_thread = threading.Thread(target=self.audio_recorder.start_recording)
        record_thread.start()

        try:
            meet_thread.join()
            record_thread.join()
        except Exception as e:
            logging.error(f"Error during threading: {type(e).__name__} - {e}")
