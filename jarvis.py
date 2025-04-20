import datetime
import pyttsx3
import speech_recognition as sr

engin=pyttsx3.init("sapi5")
voices= engin.getProperty("voices")
engin.setProperty('voice',voices[0].id)

def speak(audio):
    engin.say(audio)
    engin.runAndWait()

def wishme():
    hour=int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("good morning")
    elif 12 <= hour < 18:
        speak("good afternoon!")
    else:
        speak("good evening")
    speak("I am Jarvis Sir, Please tell me how I may help you")
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
     print("Listening....")
     r.pause_threshold=1
     audio= r.listen(source)

    try:
        print("Recognizing...")
        query =r.recognize_bing(audio,language="en-in")
        print(f'User said: {query}\n')
    except Exception as e:
        print(e)

        print ("say that again pleasss...")
        return  "None"
    return query
if __name__ == "__main__":
    speak("jayant is  good")
    wishme()
    takecommand()
