import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import random
import numpy as np

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
#print(voices[0].id)
engine.setProperty("voices", voices[0].id)


def speak(audio):
    """it takes string  as an input and speak out.

    Args:
        audio ([String]): [String which you want computer to speak out for you]
    """
    
    engine.say(audio)
    engine.runAndWait()
    
    
def wishMe():
    hour = int(datetime.datetime.now().hour)    
    if hour>=0 and hour <12:
        speak("Good Morning")
    elif hour >= 12 and hour<18:
        speak("Good Afternoon")   
    else:
        speak("Good EVening")    
    speak("I am lira Sir. please tell me how may i help you")   
    
def takeCommand():
    """
    It takes microphone input from the user and return string output.
    """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)
        
    try:
        print("Recognizing....")   
        query = r.recognize_google(audio, language = "en-in")
        print(f"User Said: {query}\n")
    
    except Exception as e:
        print(e)
        print("say that again please....")
        return "None" 
    
    return query     
           
            
            
       
        
if __name__ == "__main__":
    wishMe()
    while 1:
        query = takeCommand().lower()
        #logic for executing tasks based on query
        if "wikipedia" in query:
            speak("Searching Wikipedia....")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif "open youtube" in query:
            webbrowser.open("youtube.com")
            
        elif "open google" in query:
            webbrowser.open("google.com")    
            
        elif "open stackoverflow" in query:
            webbrowser.open("stackoverflow.com")
       
        elif "play music" in query:
            speak("Playing music sir, please wait")
            music_dir = "G:\\Desktop\\mp3"
            songs = os.listdir(music_dir)
            #print(songs)
            num = np.random.randint(0, len(songs)-1)
            os.startfile(os.path.join(music_dir,songs[num]))
            
        elif "change music" in query:
            speak("Changing music sir, please wait")
            music_dir = "G:\\Desktop\\mp3"
            songs = os.listdir(music_dir)
            #print(songs)
            num = np.random.randint(0, len(songs)-1)
            os.startfile(os.path.join(music_dir,songs[num]))    
            