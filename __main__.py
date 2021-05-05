import pyttsx3
import datetime
from datetime import date
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
# import yagmail
# import urllib
# import urllib3

# [10:56] Magdalena Nozdrzykowska
# import smtplib, sslport = 587  # For starttlssmtp_server = "smtp.gmail.com"sender_email = "my@gmail.com"receiver_email = "your@gmail.com"password = input("Type your password and press enter:")message = """\Subject: Hi thereThis message is sent from Python."""context = ssl.create_default_context()with smtplib.SMTP(smtp_server, port) as server:server.ehlo()  # Can be omittedserver.starttls(context=context)server.ehlo()  # Can be omittedserver.login(sender_email, password)server.sendmail(sender_email, receiver_email, message)


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def search_wikipedia(query):
    speak('Searching Wikipedia...')
    query = query.replace("wikipedia", "")
    results = wikipedia.summary(query, sentences=3)
    speak("according to Wikipedia")
    print(results)
    speak(results)


def google_chrome():
    os.startfile(chromePath)


def youtube():
    os.startfile(chromePath)
    webbrowser.open(yt)


def music():
    songs = os.listdir(music_dir)
    print(songs)
    os.startfile(os.path.join(music_dir, songs[0]))


def time():
    str_time = datetime.datetime.now().strftime("%H:%M:%S")
    speak(f"Sir, the time is {str_time}")
    print(str_time)


def current_date():
    str_date = date.today()
    speak(f"Sir, the date today is {str_date}")
    print(f"{str_date}")


def email():
    pass


def wish_me():
    hour = int(datetime.datetime.now().hour)
    if 5 <= hour < 12:
        speak("Miłego poranka")
    elif 12 <= hour < 18:
        speak("Dzień dobry")
    elif 18 <= hour < 24:
        speak("Dobry wieczór")
    else:
        speak("Idź spać")

    speak("Hi I am Friday Sir. Please tell me how can I help you")


def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-us')
        print(f"User said: {query}\n")
    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
    return query


if __name__ == '__main__':
    chromePath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
    music_dir = "D:\\muzyka"
    yt = 'https://www.youtube.com/'
    wish_me()
    while True:
        command = input("")
        if 'wikipedia' in command:
            search_wikipedia(command)

        elif 'open chrome' or 'chrome' or 'google' or 'open google' in command.lower():
            google_chrome()

        elif 'open youtube' in command:
            youtube()

        elif 'play music' in command:
            music()

        elif 'the time' in command:
            time()

        elif 'date' in command:
            current_date()

        elif 'email' in command:
            email()

