import pyttsx3
import speech_recognition as sr 
import datetime
import wikipedia
import webbrowser
import os
#import smtplib
import pyjokes

#from wikipedia import exceptions


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice' , voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def WishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else: 
        speak("good evening!") 
    speak("Sir ! I am jarvis , Please tell me how can I help you ?")       

def takeCommand():
    # it takes microphone  input from the user and returns string output 
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening ....")  
        r.pause_threshold = 1
        r.energy_threshold = 500
     #  r.pause_threshold = 2
        audio = r.listen(source)

    try:
        print("Recognising...")
        query = r.recognize_google(audio , language= 'en-in')
        print(f"User said :{ query}\n")                                                                                 
  

    except Exception as e:
        #print(e)
        print("Say that again please")
        return "None"
    return query

#def sendEmail(to , content):
 #  server.ehlo()
 #  server.starttls()
 #   server.login('mohakchutani1@gmail.com' , 'mohak@000 ')
  #  server.send('mohakchutani1@gmail.com', to , content)
   # server.close()





if __name__ == "__main__":
    WishMe()
    while True:
     if 1:
       query =takeCommand().lower()
       
       if 'wikipedia' in query:
           speak("searching wikipedia")
           query = query.replace("wikipedia" , "")
           results = wikipedia.summary(query , sentences=2)
           speak("According to wikipedia")
           print(results)
           speak (results)


       elif 'open youtube' in query:
           webbrowser.open("youtube.com")

       elif 'open google' in query:
           webbrowser.open("google.com") 

       elif 'play music'  in query:    
           music_dir = 'C:\\Users\\mohak\\Desktop\\JARVIS\\songs'
           songs = os.listdir(music_dir)
           print(songs)
           os.startfile(os.path.join(music_dir , songs[0]))

       elif 'the time' in  query:
           strTime = datetime.datetime.now().strftime("%H:%M:%S")
           speak(f"  Sir the time is {strTime}") 

            
       elif 'open code' in query :
           codePath = "C:\\Users\\mohak\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
           os.startfile(codePath) 

      # elif ' send an email' in query:
       #    try:
        #        speak("what should I say")
        #        content = takeCommand()
         #       to = "xxmohak@gmail.com"
          #      sendEmail(to, content)
           #     speak("Email has been sent")
          # except Exception as e:
           #    print(e) 
            #   speak("Sorry sir , I am not able to send this email ")  

       elif 'are you single' in query:
           speak("no , i am relationship with wifi") 

       elif 'joke' in query:
           speak(pyjokes.get_joke())    
       elif 'exit' in query:
           exit()