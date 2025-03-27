import os

from openai import OpenAI
from pydub import AudioSegment


class SpeechRecognition:
    def __init__(self, language="tr-TR", api_key=None, file_path: str = None):
        self.language = language
        self.client = OpenAI(api_key=api_key)
        self.file_path = file_path

    def recognize(self):
        return self.transcribe_large_audio()

    def split_audio(self, chunk_length_ms=100000):
        audio = AudioSegment.from_wav(self.file_path)
        chunks = []
        for i in range(0, len(audio), chunk_length_ms):
            chunk = audio[i:i + chunk_length_ms]
            chunk_name = f"chunk_{i // 1000}.wav"
            chunk.export(chunk_name, format="wav")
            chunks.append(chunk_name)
        return chunks

    def transcribe_audio_chunk(self, chunk_path):
        with open(chunk_path, "rb") as audio_file:
            transcription = self.client.audio.transcriptions.create(
                model="whisper-1",
                file=audio_file,
                language=self.language
            )
        return transcription.text

    def transcribe_large_audio(self):
        chunks = self.split_audio()
        full_transcription = ""
        for chunk in chunks:
            try:
                text = self.transcribe_audio_chunk(chunk)
                full_transcription += text + " "
                os.remove(chunk)
            except Exception as e:
                print(e)

        return full_transcription.strip()
