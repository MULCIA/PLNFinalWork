from unittest import TestCase
from PLNFinalWork.audio_recorder import Audio_Recorder

class TestAudio_Recorder(TestCase):

    def setUp(self):
        TestCase.setUp(self)
        self.audio_recorder = Audio_Recorder()

if __name__ == '__main__':
    unittest.main()
