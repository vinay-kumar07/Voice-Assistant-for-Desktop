import pyttsx3
import datetime
import speech_recognition as sr
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    ##
    hour = int(datetime.datetime.now().hour)
    if (hour >= 0) and (hour < 12):
        speak("morning")

    elif (hour >= 12) and (hour < 18):
        speak("afternoon")

    else:
        speak("evening")

    speak("how are u sir")
    ##

def takeCommand():
    ##
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening........")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as exp:
        print("Say that again.....")
        return "None"
    return query
    ##

if __name__ == '__main__':
    wishMe()
    takeCommand()
