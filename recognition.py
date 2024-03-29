import os
import speech_recognition



r = speech_recognition.Recognizer()

audio_file = './test_speech.wav'

with speech_recognition.AudioFile(audio_file) as source:
    audio = r.record(source)

try:
    text = r.recognize_google(audio, language='ja-JP')
    with open('audio_text.txt', mode='w') as f:
        f.write(text)
except speech_recognition.UnknownValueError:
    print('Google Speech Recognition could not understand audio')
except speech_recognition.RequestError as e:
    print('Could not request results from Google Speech Recognition service; {0}'.format(e))

