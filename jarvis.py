import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    #To provide voice assisted output
    engine.say(audio)
    engine.runAndWait()

def wishme():
    #Speaks a Greeting message according to time
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        print("Good Morining!")
        speak("Good Morning!")
   
    elif hour>12 and hour <=18:
        print("Good Afternoon!")
        speak("Good Afternoon!") 
    else:
        print("Good Evening!")
        speak("Good Evening!")
    print("Hi, I am Jarvis, How can I help you....") 
    speak("Hi, I am Jarvis, How can I help you") 
    


def takecommand():
    #it takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio =  r.listen(source)
    try:
        print("Recognising...\n")
        query = r.recognize_google(audio, language='en-in')
        print("User said: "+query)

    except Exception as e:
        #print(e)    
        print("Say that again please....")
        return "None"                            
    return query
if __name__ == "__main__":
    wishme()
    while True:
        query = takecommand().lower()
        if 'wikipedia' in query:
            speak("Searching in wikipedia....")
            query=query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences =2)
            print("According to wikipedia!\n")
            speak("Accoding to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            print("Opening Youtube!\n")
            webbrowser.get(chrome_path).open("youtube.com")   
        elif 'open google' in query:
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            print("Opening Google!\n")
            webbrowser.get(chrome_path).open("google.com")      
        elif 'open gmail' in query:
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            print("Opeing Gmail!\n")
            webbrowser.get(chrome_path).open("gmail.com")      
        
        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            print("Current Time: "+strTime)
            speak("Hi, The time is"+strTime) 

        elif 'open windows application ' in query:
            #Opens only Windows recognizable and installed applications
            #Applications such as chrome,notepad,firefox..... 
            query=query.replace("open windows application","")
            print("Opening"+query)
            os.system(query)    

        elif 'play music' in query:
            music_dr =  'D:\\music'    #Path to fetch the music files
            songs = os.listdir(music_dr)
            songselected=random.choice(songs)   #playing music in random
            os.startfile(os.path.join(music_dr, songselected))

        elif 'quit' or 'exit'in query:
            print("Byee..")
            exit()    
