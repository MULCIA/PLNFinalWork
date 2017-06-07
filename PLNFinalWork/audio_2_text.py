import io
import os
from google.cloud import speech

class Audio_2_Text(object):

    def __init__(self, file_name, audio_lang):
        self.speech_client = speech.Client()
        self.file_name = file_name
        self.audio = None
        self.audio_lang = audio_lang

    def find_file(self):
        file_name = os.path.join(
            os.path.dirname(__file__),
            '.',
            self.file_name
        )

    def load_audio(self):
        with io.open(self.file_name, 'rb') as audio_file:
            content = audio_file.read()
            self.audio = speech_client.sample(
                content,
                source_uri=None,
                encoding='LINEAR16',
                sample_rate_hertz=16000
            )

    def recognize(self):
        alternatives = audio_sample.recognize(self.audio_lang)
        return alternatives[0]
        """for alternative in alternatives:
            print('Transcript: {}'.format(alternative.transcript))"""
