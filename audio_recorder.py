import pyaudio
import wave
import logging
from config import Config

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class AudioRecorder:
    def __init__(self, output_filename=Config.OUTPUT_FILENAME, chunk=Config.CHUNK,
                 format=Config.FORMAT, channels=Config.CHANNELS, rate=Config.RATE):
        """
        Audio recorder class

        Parameters:
        output_filename (str): Name of the recording file
        chunk (int): Amount of data to read each time
        format: Audio format
        channels (int): Number of channels (1: mono, 2: stereo)
        rate (int): Sampling rate (Hz)
        """
        self.output_filename = output_filename
        self.chunk = chunk
        self.format = format
        self.channels = channels
        self.rate = rate

        self.audio = pyaudio.PyAudio()
        self.stream = None
        self.frames = []
        self.is_recording = False

    def start_recording(self):
        """Starts audio recording"""
        if not self.is_recording:
            self.stream = self.audio.open(
                format=self.format,
                channels=self.channels,
                rate=self.rate,
                input=True,
                frames_per_buffer=self.chunk,
                stream_callback=self._callback
            )
            self.frames = []  # Reset frames list for new recording
            self.is_recording = True
            self.stream.start_stream()
            logging.info("Recording started...")
        else:
            logging.warning("Already recording!")

    def stop_recording(self):
        """Stops audio recording and saves to file"""
        if self.is_recording and self.stream is not None:
            self.stream.stop_stream()
            self.stream.close()
            self.is_recording = False

            # Save audio data to WAV file
            wf = wave.open(self.output_filename, 'wb')
            wf.setnchannels(self.channels)
            wf.setsampwidth(self.audio.get_sample_size(self.format))
            wf.setframerate(self.rate)
            wf.writeframes(b''.join(self.frames))
            wf.close()

            logging.info(f"Recording saved to {self.output_filename} file!")
        else:
            logging.warning("Recording already stopped or never started!")

    def _callback(self, in_data, frame_count, time_info, status):
        """Callback function that processes audio data"""
        if self.is_recording:
            self.frames.append(in_data)
            return (in_data, pyaudio.paContinue)
        return (in_data, pyaudio.paComplete)

    def __del__(self):
        """Cleans up PyAudio object when class is destroyed"""
        self.audio.terminate()
