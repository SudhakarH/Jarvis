import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser as wb
import os

engine = pyttsx3.init()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

speak("this is sudhakar , student of vimal sir")

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    
    speak(Time)

#time()

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak(date)
    speak(month)
    speak(year)

#date()

def wishme():
    speak("Welcome back sir!")
    time()
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour<12:
        speak("Good morning sir!")
    elif hour >=12 and hour<18:
        speak("Good afternoon sir!")
    elif hour >=18 and hour<24:
        speak("Good evening sir!")
    else:
        speak("Good night sir!")

    speak("Jarvis at your service. Please tell me how can i help you?")
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.parse_threshold = 1
        audio = r.listen(source)


    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(query)

    except Exception as e:
        print(e)
        speak("Say that again please...")
        return "None"

    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.echlo()
    server.starttls()
    server.login('sudhi.lucky1999@gmail.com','12345')
    server.sendmail('sudhi.lucky1999@gmail.com', to, content)
    server.close()


if __name__ == "__main__":
    wishme()
    while True:
        query = takeCommand().lower()
        if 'not' in query or ('did not' or 'do not') in query:
            speak("Okay sir")

        elif 'time' in query:
            time()
        elif 'wikipedia' in query:
            speak("Searching...")
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query, sentences=2)
            print(result)
            speak(result)
        elif 'send email' in query:
            try:
                speak("what should I say?")
                content = takeCommand()
                to = 'sudhakarh1999@gmail.com'
                sendEmail(to,content)
                speak("Email has been sent!")
            except exception as e:
                print(e)
                speak("Unable to send the email")

        elif 'search in chrome' in query:
            speak("What should i search ?")
            chromepath = '/Applications/chrome.exe %s'
            search = takeCommand().lower()
            wb.get(chromepath).open_new_tab(search+'.com')

        elif 'chrome' in query and ('run' or 'execute' or 'open' or 'show') in query:
            os.system('chrome')

        elif ('notepad' or 'editor' or 'notebook' or 'notes') in query and ('run' or 'execute' or 'open' or 'show') in query:
            os.system('notepad')

        elif ('media player' or 'windows media player' or 'wmplayer') in query and ('run' or 'execute' or 'open' or 'show') in query:
            os.system('wmplayer')

        elif ('vlc player' or 'vlc media player' or 'vlc') in query and ('run' or 'execute' or 'open' or 'show') in query:
            os.system('vlc')

        elif 'offline' in query:
            quit()