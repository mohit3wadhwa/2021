import speech_recognition as sr
# import pyaudio
import webbrowser
# import requests
#from /Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages/speech_recognition
#import sys; sys.executable

r1 = sr.Recognizer()
r2 = sr.Recognizer()
r3 = sr.Recognizer()

with sr.Microphone() as source:
    print('detect mic')
    print('Speak up')
    audio = r3.listen(source)
    print('audioooo', audio)
    
if 'Infosys' in r2.recognize_google(audio):
    r2 = sr.Recognizer()
    url = 'www.google.com'
    with sr.Microphone() as source:
        print('search your query')
        audio = r2.listen(source)
        
        try:
            get = r2.recognize_google(audio)
            print(get)
            webbrowser.get().open_new(url+get)
            
        except sr.UnknownValueError:
                print('erroorrr')
        except sr.RequestError as e:
                print('request')
      