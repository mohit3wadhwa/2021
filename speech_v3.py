# #import library
# import speech_recognition as sr

# # Initialize recognizer class (for recognizing the speech)
# r = sr.Recognizer()

# # Reading Audio file as source
# # listening the audio file and store in audio_text variable

# with sr.AudioFile('audio.wav') as source:
    
#     audio_text = r.listen(source)
    
# # recoginize_() method will throw a request error if the API is unreachable, hence using exception handling
#     try:
        
#         # using google speech recognition
#         text = r.recognize_google(audio_text)
#         print('Converting audio transcripts into text ...')
#         print(text)
     
#     except:
#          print('Sorry.. run again...')




#First off install below libraries - 
# 1. pip3 install SpeechRecognition
# 2. pip3 install PyAudio

#import speech library
import os
import speech_recognition as sr

print(os.path.abspath('Audio_transcript.txt')) 
# Initialize recognizer class (for recognizing the speech)
recogn = sr.Recognizer()

# listening from Microphone
# listening the speech and store in 'audio' variable

with sr.Microphone() as source:
    print("Please spreak now\n")
    audio = recogn.listen(source)
    print("Listening stops working!\n")
# recoginize_() method will throw error if the Google's API does not work
    
    try:
        # Calling google speech API for speech recognition
        #print("You said: " + recogn.recognize_google(audio))
        
        # Writing Transcript to a text file
        f = open("Audio_transcript.txt", "w")
        f.write(recogn.recognize_google(audio))
        f.close()

        #open and read the file after the writing:
        f = open("Audio_transcript.txt", "r")
        print("Reading from file - " + f.read() + "\n")
        
        print("_____________________________________________________________")
        print("Transcript has been successfully written to file 'Audio_transcript.txt' at path -> " + os.path.abspath('Audio_transcript.txt'))
        print("_____________________________________________________________")
        
        
    except:
         print("Something's wrong...")