import pyttsx3
import datetime
import speech_recognition as sr
#import pyaudio

eng = pyttsx3.init('sapi5')
voi = eng.getProperty('voices')
print(voi[0].id)
eng.setProperty('voices', voi[0].id)

def speak(audio):
    eng.say(audio)
    eng.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<12:
        speak("goood morning")
    elif hour>=12 and hour <16:
        speak("good afternoon")
    elif hour>=16 and hour<19:
        speak("good evening")
    else :
        speak("good night")

    speak("i am robot, shivam. how may i help you")

def takcommand():
    r = sr.Recognizer()
    with sr.Microphone() as source :
         print("listening...")
         r.pause_threshold = 1
         audio = r.listen(source)

    try:
        print("reconiging....")
        query = r.recognize_google(audio, language="en-in")
        print("user said: {}\n".format(query))

    except Exception as e:
        print(e)
        print("please say again")
        return "none "
    return query
if __name__== "__main__":

    wishme()
    takcommand()