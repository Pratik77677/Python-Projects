import pyttsx3 #Text to speech conversion library
import speech_recognition as sr # required to use library pyaudio if taken input fron microphone
import datetime # provides date and time functionalities
import wikipedia # fetch wikipedia article 
import webbrowser # open webrowser links
import os # provides function to interact with operating system
import smtplib # used to send emails using smtp

engine = pyttsx3.init('sapi5') # sapi5 is a speech api used to take an inbuilt voice male or female
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# function to convert string value to audio 
def speak(audio):
    engine.say(audio) # takes string value and speaks it up
    engine.runAndWait()

# function to wish user according to current time
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Pratik Sir. Please tell me how may I help you")       

#It takes microphone input from the user and returns string output
def takeCommand():

    r = sr.Recognizer() # recognize speech from audio source with API support
    with sr.Microphone() as source: # microphone is used to specify input audio time,loudness etc.
        print("Listening...")
        r.pause_threshold = 0.9
        audio = r.listen(source)
# Exception block to handle error if the input string provided as audio is not available in program
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e: 
        print("Repeat please...")  
        return "None"
    return query

#function to send email
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587) #587 is a port no. for smtp
    server.ehlo() # pyhton start simple http server
    server.starttls() # put the smtp connection into tls(transport layer security) mode
    server.login('pratikadangale77@gmail.com', '*******')
    server.sendmail('pratikadangale77@gmail.com', to, content) # send email
    server.close() # closes the operation

if __name__ == "__main__":
    wishMe()
    while True:

        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'play music' in query:
            music_dir = 'C:\\Users\\Pratik Adangale\\Music'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\Pratik Adangale\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code"
            os.startfile(codePath)

        elif 'email to pratik' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "pratikadangale77@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend. I am not able to send this email")    
