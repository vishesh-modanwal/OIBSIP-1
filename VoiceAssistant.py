import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser

# Initialize the voice engine
engine = pyttsx3.init()
engine.setProperty("rate", 150)  # Speed of speech
engine.setProperty("volume", 0.9)  # Volume 0-1

def speak(text):
    """Converts text to speech"""
    engine.say(text)
    engine.runAndWait()

def take_command():
    """Takes voice input from the user and converts it to text"""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)
    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language="en-in")
        print(f"User said: {query}\n")
    except Exception as e:
        print("Sorry, I didn't catch that. Could you say it again?")
        return None
    return query.lower()

def greet_user():
    """Greets the user based on the time of day"""
    hour = datetime.datetime.now().hour
    if hour < 12:
        speak("Good morning!")
    elif hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    speak("I am your virtual assistant. How can I help you?")

def main():
    greet_user()
    while True:
        query = take_command()
        if query is None:
            continue
        
        # Basic commands
        if "time" in query:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {current_time}")
        
        elif "date" in query:
            current_date = datetime.datetime.now().date()
            speak(f"Today's date is {current_date}")
        
        elif "open google" in query:
            speak("Opening Google")
            webbrowser.open("https://www.google.com")
        
        elif "search" in query:
            speak("What would you like to search for?")
            search_query = take_command()
            if search_query:
                speak(f"Searching for {search_query}")
                webbrowser.open(f"https://www.google.com/search?q={search_query}")
        
        elif "exit" in query or "stop" in query:
            speak("Goodbye!")
            break

if __name__ == "__main__":
    main()
