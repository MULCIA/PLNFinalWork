import argparse
from PLNFinalWork.audio_recorder import Audio_Recorder
from PLNFinalWork.audio_2_text import Audio_2_Text
from PLNFinalWork.lang_classifier import Lang_Classifier

# python3 main.py "Hola esto es un ejemplo" "spanish" model.pickle output.wav

if __name__ == "__main__":

    #Get arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('text', metavar='F', nargs='+', type=str, help='Text from audio')
    parser.add_argument('lang', metavar='M', type=str, help='Language')
    parser.add_argument('model', metavar='M', type=str, help='Pickle file')
    parser.add_argument('audio_file', metavar='M', type=str, help='Files to classify')
    args = parser.parse_args()

    print("Recording...")

    audio_recorder = Audio_Recorder()
    audio_recorder.recording()
    audio_recorder.save_file(args.audio_file)

    print("Recorded successfully!")

    print("Getting text from audio...")

    audio_lang = 'es-ES' if args.lang == 'spanish' else 'en-US'

    audio_2_text = Audio_2_Text(args.audio_file, audio_lang)
    audio_2_text.find_file()
    audio_2_text.load_audio()
    text_to_predict = audio_2_text.recognize()

    print("Recognize successfully!")

    print("Checking text and language...")

    lang_classifier = Lang_Classifier(args.model, [text_to_predict])
    predicted = lang_classifier.classify()

    if text_to_predict == args.text[0] and predicted[0] == args.lang:
        print('Success')
    else:
        print('Fail')
