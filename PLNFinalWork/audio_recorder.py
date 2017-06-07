import wave
import pyaudio

FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
CHUNK = 1024
RECORD_SECONDS = 5

class Audio_Recorder(object):

    def __init__(self):
        self.audio = pyaudio.PyAudio()
        self.stream = None
        self.frames = []

    def recording(self):
        self.stream = self.audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)
        for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
            data = self.stream.read(CHUNK)
            self.frames.append(data)

        self.stream.stop_stream()
        self.stream.close()
        self.audio.terminate()

    def save_file(self, audio_output_filename):
        waveFile = wave.open(audio_output_filename, 'wb')
        waveFile.setnchannels(CHANNELS)
        waveFile.setsampwidth(self.audio.get_sample_size(FORMAT))
        waveFile.setframerate(RATE)
        waveFile.writeframes(b''.join(self.frames))
        waveFile.close()
