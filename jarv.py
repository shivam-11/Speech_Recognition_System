import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio
import wikipedia
import webbrowser
import os
import smtplib


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
    else:
        speak("good night")

    speak("i am virtual human, shivam. how may i help you")

def takcommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 4
        audio = r.listen(source)

    try:
        print("recogniging....")
        query = r.recognize_google(audio, language="en-in")
        print("user said: {}\n".format(query))

    except Exception as e:
        print(e)
        print("please say again")
        return "none"

    return query

def sendemail(to,content):

    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('shivam99cs@gmail.com', 'shivam@12')
    server.sendmail('shubh73585@gmail.com', to, content)
    server.close()


if __name__== "__main__":

   wishme()
   while True:
        query = takcommand().lower()

        if 'wikipedia' in query:
            speak('searching wikipedia...')
            query = query.replace("wikipedia", "" )
            result= wikipedia.summary(query, sentences=2)
            speak('according to wikipedia')
            print(result)
            speak(result)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com ")


        elif 'open google' in query:
            webbrowser.open("google.com ")

        elif 'play music' in query:
            music_dir = 'c:\\song'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'time' in query:
            strtime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"time is {strtime}")

        elif 'open eclipse' in query:
            codepath ="C:\\Users\\Shivam Singh\\eclipse\\java-2018-12\\eclipse\\eclipse.exe"
            os.startfile(codepath)

        elif 'open pycharm' in query:
            codepath = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2019.1.3\\bin\\pycharm64.exe"
            os.startfile(codepath)


        elif  'send email' in query:
            try:
                 speak("what should i have to sent ")
                 content = takcommand()
                 to = 'shivam99cs@gmail.com'
                 sendemail(to, content)
                 print('email has send')

            except Exception as e:
                print(e)
                print('sorry, i am not able to send ')



#we can add many other functionality