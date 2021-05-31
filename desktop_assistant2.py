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
    speak("Hello!")
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour==12:
        speak("Good Noon!")

    elif hour>12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")
        
    speak("I am Jessie sir. Please tell me how may i help you?")

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
    server.login('<enter-your-email>', '<enter-your-password>')
    server.sendmail('<enter-your-email>',to, content)
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

        elif 'kaise ho aap' in query or 'how are you' in query:
            speak("I am absolutly fine sir. Thank you for asking sir.")

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query or 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'whatsapp' in query or 'whats app' in query:
            webbrowser.open("web.whatsapp.com")

        elif 'play music' in query:
            music_dir = "<location-of-your-music-folder>"
            songs = os.listdir(music_dir)
            n = random.randint(0,len(songs)-1)
            os.startfile(os.path.join(music_dir, songs[n]))

        elif 'the time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir,the time is {strtime}")

        elif 'open visual studio code' in query or 'open code' in query:
            code_path = "<Path-of-the-visual-studio-code>"
            os.startfile(code_path)

        elif 'send email' in query:
            try:
                to = '<receivers email address>'
                speak("What do you wanna say?")
                content = takeCommand()
                sendEmail(to, content)
                speak("Email has been sent successfully")

            except Exception as e:
                print(e)
                speak("Sorry, i am unable to send the email.")

        elif 'favourite shows' in query:
            fav_path = "<path-of-your-favourite-shows-folder>"
            os.startfile(fav_path)
            
        
        elif 'quit' in query or 'exit' in query:
            speak("Thank you sir. Have a great day!")
            exit()