import pyttsx3  # Text-to-speech conversion library
import speech_recognition as sr  # Library for performing speech recognition
import datetime  # Library to work with date and time
import wikipedia  # Library to fetch information from Wikipedia
import webbrowser  # Library to open web browsers
import os  # Library to interact with the operating system
import time  # Library to work with time-related tasks
import subprocess  # Library to run subprocesses

class VoiceAssistant:
    def __init__(self, master):
        # Initialize the voice assistant with the master's name
        self.master = master
        self.engine = pyttsx3.init('sapi5')
        voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', voices[0].id)

    def speak(self, text):
        # Function to make the assistant speak
        self.engine.say(text)
        self.engine.runAndWait()

    def wish_me(self):
        # Function to greet the master based on the current time
        hour = int(datetime.datetime.now().hour)
        print(hour)
        if hour >= 0 and hour < 12:
            self.speak("Good morning " + self.master)
        elif hour >= 12 and hour < 18:
            self.speak("Good afternoon " + self.master)
        else:
            self.speak("Good evening " + self.master)

    def take_command(self):
        # Function to listen to the master's command
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")
        except Exception as e:
            print("Say that again please")
            query = None
        return query

    def search_wikipedia(self, query):
        # Function to search Wikipedia
        self.speak('Searching Wikipedia...')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        self.speak(results)

    def open_website(self, url):
        # Function to open a website
        webbrowser.open(url)

    def open_application(self, path):
        # Function to open an application
        os.startfile(path)

    def chrome_voice_search(self, query):
        # Function to search Google using Chrome
        self.speak(f"Searching for {query} on Google.")
        webbrowser.open(f"https://www.google.com/search?q={query}")
        time.sleep(3)  # Wait for the browser to open

    def run(self):
        # Main function to run the voice assistant
        self.speak("Initializing Maxx...")
        self.wish_me()
        while True:
            query = self.take_command()
            if query:
                query_lower = query.lower()
                if 'wikipedia' in query_lower:
                    self.search_wikipedia(query)
                elif 'the time' in query_lower:
                    str_time = datetime.datetime.now().strftime("%H:%M:%S")
                    self.speak(f"{self.master}, the time is {str_time}")
                elif 'open vs code' in query_lower:
                    self.open_application("C:\\Users\\shukl\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")
                elif 'open powerpoint' in query_lower:
                    self.open_application("C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE")
                elif 'open excel' in query_lower:
                    self.open_application("C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE")
                elif 'open word' in query_lower:
                    self.open_application("C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE")
                elif 'open chrome' in query_lower:
                    self.open_application("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
                elif 'open edge' in query_lower:
                    self.open_application("C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe")
                elif 'open adobe acrobat' in query_lower:
                    self.open_application("C:\\Program Files\\Adobe\\Acrobat DC\\Acrobat\\Acrobat.exe")
                elif 'open calculator' in query_lower:
                    os.system("calc.exe")
                elif 'open notepad' in query_lower:
                    os.system("notepad.exe")
                elif 'open file explorer' in query_lower:
                    os.system("explorer.exe")
                elif 'open camera' in query_lower:
                    os.system("start microsoft.windows.camera:")
                elif 'open paint' in query_lower:
                    subprocess.run(["mspaint.exe"], shell=True)
                elif 'search' in query_lower:
                    search_query = query.replace("search", "")
                    self.chrome_voice_search(search_query)
                elif 'stop' in query_lower or 'exit' in query_lower:
                    self.speak("Goodbye!")
                    break

if __name__ == "__main__":
    # Initialize and run the voice assistant
     assistant = VoiceAssistant("Jayesh")
     assistant.run()