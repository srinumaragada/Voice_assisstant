import speech_recognition as sr
import datetime
import webbrowser
import pyttsx3

r = sr.Recognizer()
engine = pyttsx3.init()

def respond(audio):
    print(audio) 
    engine.say(audio)
    engine.runAndWait()

def welcome():
    respond("Hello, how can I help you?")

def time():
    time = datetime.datetime.now().strftime("%I:%M:%S") 
    respond(f"The current time is {time}")

def date():
    date = datetime.date.today()
    respond(f"Today's date is {date}")
    
def search():
    respond("What do you want to search for?")
    search = r.listen(source)
    url = f"https://google.com/search?q={search}"
    webbrowser.get().open(url)
    respond(f"Here are the search results for {search}")

while True:
    
    respond("Listening...")
    with sr.Microphone() as source:
        audio=r.listen(source)

    try:
        statement = r.recognize_google(audio)
        
        if statement == "hello":
            welcome()
        elif statement == "what time is it" or statement == "what is the time":
            time()
        elif statement == "what is today's date" or statement == "what date is it":
            date()
        elif "search" in statement:
            search()
            
        else:
            respond("I'm still learning new commands!")
            
    except:
       respond("Sorry, I didn't get that. Can you repeat?")