################# use cmd to get output ###################
import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes
import os
import time

def sptext ():
    reconizer=sr.Recognizer()
    with sr.Microphone() as source:
        print("Jarvis Activated.....")
        reconizer.adjust_for_ambient_noise(source)
        audio = reconizer.listen(source)
        try:
            print("reconizing...")
            data = reconizer.recognize_google(audio)
            print(data)
            return data
        except sr.UnknownValueError:
            print("I am angry")
            
def speechtx(x) :
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice' , voices[0].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate' , 150)
    engine.say(x)
    engine.runAndWait()
    
    # speechtx("hello welcome to jarvis ")
if __name__ =='__main__' :
    
    while True:
    
        # add question what you want to ask jarvis
        
        data1=sptext().lower()
        if "your name" in data1:
            name = "my name is jarvis"
            speechtx(name)
        
        elif "old are you" in data1:
            age = "I don't have an age in the traditional sense"
            speechtx(age)
        
        elif 'time' in data1:
            time = datetime.datetime.now().strftime("%I%M%p")
            speechtx(time)
        
        elif 'youtube' in data1:
            webbrowser.open("https://www.youtube.com/@rupakparajuli7537")
        
        elif 'google' in data1:
            webbrowser.open("https://www.google.com/")
        
        elif "joke" in data1:
            joke_1=pyjokes.get_joke(language="en", category= 'neutral')
            print(joke_1)
            speechtx(joke_1)
       
        elif 'play song' in data1:
            add = "C:\Users\paraj\Music\Unlimited Free Music Downloader\Downloaded Files"
            listsong = os.listdir(add)
            print (listsong)
            os.startfile(os.path.join(add,listsong[0]))
        
        elif "exit" in data1:
            speechtx("thank you for use me see you again stay safe stay healthy and have a good day")
            break
        
        time.sleep(10)

else:
    print("thanks")