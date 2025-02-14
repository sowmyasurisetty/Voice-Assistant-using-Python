import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import requests
import random

# Initialize the speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    """Speak the given text."""
    print(f"🤖 Assistant: {audio}")  # Debugging
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    """Greets the user based on the time of day."""
    hour = int(datetime.datetime.now().hour)
    if hour < 12:
        greeting = "Good Morning!"
    elif 12 <= hour < 18:
        greeting = "Good Afternoon!"
    else:
        greeting = "Good Evening!"

    speak(greeting)
    speak("I am your AI Assistant. How can I help you?")

def takeCommand():
    """Listens to user input and returns recognized text."""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Listening...")
        r.adjust_for_ambient_noise(source, duration=1)
        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=5)
            print("🔍 Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"👤 User: {query}")
            return query.lower()
        except sr.UnknownValueError:
            print("❌ Could not understand.")
            speak("Sorry, I could not understand. Please say that again.")
            return "None"
        except sr.RequestError:
            print("❌ No internet connection.")
            speak("I am having trouble connecting. Please check your internet.")
            return "None"

def getWeather(city):
    """Fetches weather details using OpenWeatherMap API."""
    api_key = "your_openweathermap_api_key"  # Replace with your API key
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    try:
        complete_url = f"{base_url}q={city}&appid={api_key}&units=metric"
        response = requests.get(complete_url)
        weather_data = response.json()
        
        if weather_data["cod"] != "404":
            temp = weather_data["main"]["temp"]
            desc = weather_data["weather"][0]["description"]
            report = f"The temperature in {city} is {temp} degrees Celsius with {desc}."
            speak(report)
        else:
            speak("City not found, please try again.")
    except:
        speak("Sorry, I couldn't fetch the weather data.")

def openWebsite(site, name):
    """Opens a website."""
    webbrowser.open(site)
    speak(f"Opening {name}")

def main():
    wishMe()

    while True:
        query = takeCommand()

        if query == "none":
            continue  # Skip if input is invalid

        # Greeting responses
        if any(word in query for word in ["hello", "hi", "hey", "good morning", "good afternoon", "good evening"]):
            speak("Hello! How can I assist you?")

        elif 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            try:
                results = wikipedia.summary(query, sentences=2)
                speak(f"According to Wikipedia: {results}")
            except:
                speak("Sorry, I couldn't find anything on Wikipedia.")

        elif 'open youtube' in query:
            openWebsite("https://www.youtube.com", "YouTube")

        elif 'open google' in query:
            openWebsite("https://www.google.com", "Google")

        elif 'open stackoverflow' in query:
            openWebsite("https://www.stackoverflow.com", "Stack Overflow")

        elif 'play music' in query:
            music_dir = "C:\\Users\\YourUser\\Music"  # Change this path
            songs = os.listdir(music_dir)
            if songs:
                os.startfile(os.path.join(music_dir, random.choice(songs)))
                speak("Playing music.")
            else:
                speak("No music files found.")

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")

        elif 'weather' in query:
            speak("Which city?")
            city = takeCommand()
            if city != "none":
                getWeather(city)

        elif 'exit' in query or 'quit' in query:
            speak("Goodbye! Have a nice day.")
            break

        else:
            speak("I'm not sure how to help with that.")

if __name__ == "__main__":
    main()
