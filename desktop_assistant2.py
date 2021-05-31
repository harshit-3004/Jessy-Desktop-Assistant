import wikipedia
import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser
import os
import random
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour==12:
        speak("Good Noon!")

    elif hour>12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")
        
    speak("I am Jessy sir. Please tell me how may i help you?")

def takeCommand():
    # it takes microphone input from the user and convert it into string 
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing......")
        query = r.recognize_google(audio, language="en-in")
        print("User Said : ",query)

    except Exception as e:
        print("Say that again please...")
        return "None"

    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('<Enter-you-email>','<your-password>')      #you can save your password in a text file and can read it here 
    server.sendmail('Enter-your-email',to, content)
    server.close()


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        # execution the command spoken 
        if 'wikipedia' in query:
            speak("Searching wikipedia")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            music_dir = "<Enter-the-path-of-your-songs-folder>"
            songs = os.listdir(music_dir)
            n = random.randint(0,len(songs)-1)
            os.startfile(os.path.join(music_dir, songs[n]))

        elif 'the time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir,the time is {strtime}")

        elif 'open code' in query:
            code_path = "<path-of-you-visual-studio-code>"
            os.startfile(code_path)

        elif 'send email' in query:
            try:
                speak("To whom you want to send email sir?")
                to = <enter the email to whom you want to send>             #you can make a dictionary which has the name as the key and email as the values
                speak("What do you wanna say?")
                content = takeCommand()
                sendEmail(to, content)
                speak("Email has been sent successfully")

            except Exception as e:
                print(e)
                speak("Sorry, i am unable to send the email.")
        
        elif 'quit' or 'exit' in query:
            exit()