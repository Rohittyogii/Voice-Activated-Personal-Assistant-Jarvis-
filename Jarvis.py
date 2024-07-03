import pyttsx3 as p
import speech_recognition as sr
from selenium_web import *
from YT_audio import *
from News import * 
import randfacts
from wheather import *
import datetime
import subprocess as sp
from camera import *


engine = p.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', 180)
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()


def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>0 and hour<12:
        return("Morning")
    elif hour>=12 and hour<16:
        return("Afternoon")
    else:
        return("Evening")

today_date=datetime.datetime.now()

r = sr.Recognizer()

speak("Hello Sir, good "+ wishme()+",I'm Jarvis.")
speak("Today is " + today_date.strftime("%d") + "of" + today_date.strftime("%B" + "And its currently" + (today_date.strftime("%I") +(today_date.strftime("%M") + today_date.strftime("%p") ))))
speak("Temperature in Gurgaon is "+ str(temp()) +"degree celcius" + "and with" + str(des()))
speak(",How are you??")
with sr.Microphone() as source:
    r.energy_threshold = 10000
    r.adjust_for_ambient_noise(source, 1.2)
    print("Listening.......")
    audio = r.listen(source)
    text = r.recognize_google(audio)
    print(text)

if "What" and "about" and "you" in text:
    speak("I am having a good day sir")
    speak("What can I do for you?")

with sr.Microphone() as source:
    r.energy_threshold = 10000
    r.adjust_for_ambient_noise(source, 1.2)
    print("Listening.......")
    audio = r.listen(source)
    text2 = r.recognize_google(audio)

if "information" in text2:
    speak("you need information related to which topic?")

    with sr.Microphone() as source:
        r.energy_threshold = 10000
        r.adjust_for_ambient_noise(source, 1.2)
        print("Listening.......")
        audio = r.listen(source)
        infor = r.recognize_google(audio)
        speak("searching {} in wikipedia".format(infor))
        assist = infow()
        assist.get_info(infor)

elif "play" and "video" in text2:
    speak("You want to play which video?")
    with sr.Microphone() as source:
        r.energy_threshold = 10000
        r.adjust_for_ambient_noise(source, 1.2)
        print("Listening.......")
        audio = r.listen(source)
        vid = r.recognize_google(audio)
    print("Playing {} an Youtube".format(vid))
    speak("Playing {} an Youtube".format(vid))
    assist = MusicPlayer()
    assist.play(vid)


elif "news" in text2:
    print("Sure sir, Now I will Read news for you.")
    speak("Sure sir, Now I will Read news for you.")
    arr = news()
    for i in range(len(arr)):
        print(arr[i])
        speak(arr[i])
        
elif "Fact" or "facts" in text2:
    print("sure sir")
    speak("Sure sir.")
    x = randfacts.get_fact()
    print(x)
    speak("Did you know that." +x)


