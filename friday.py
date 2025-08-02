import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import subprocess
import webbrowser
import os
import random
import pyautogui
import tkinter as tk
import threading
import time
from tkinter import *


# Set up speech recognition engine
recognizer = sr.Recognizer()

# Set up text-to-speech engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # Set the desired voice

# Set up flag variables
google_opened = False
youtube_opened = False
play_opened = False

# Global variable for storing the user's phone number
user_phone_number = ""


def talk(text):
    engine.say(text)
    engine.runAndWait()


def input_instruction():
    global instruction
    try:
        with sr.Microphone() as source:
            print("Listening...")
            update_status_text("Listening...")
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            audio = recognizer.listen(source)
            try:
                instruction = recognizer.recognize_google(audio)
            except sr.UnknownValueError:
                instruction = ''
            instruction = instruction.lower()
            print("You said:", instruction)
            update_status_text("You said: " + instruction)
    except sr.RequestError as e:
        print("Error occurred during speech recognition:", str(e))
        instruction = ''
    return instruction


def send_whatsapp_message(phone_number, message):
    pywhatkit.sendwhatmsg_instantly(f"+{phone_number}", message)
    print("Message sent")
    talk("Message sent")


def get_user_phone_number():
    global user_phone_number
    phone_number = phone_entry.get()
    user_phone_number = phone_number.strip()


def update_status_text(text):
    status_label.config(text=text)


def play_friday():
    instruction = input_instruction()
    if instruction == '':
        print("Invalid command")
        talk('Invalid command. Say "Friday" first.')
    else:
        print(instruction)
        global google_opened, youtube_opened, play_opened
        
        if "play" in instruction and not play_opened:
            song = instruction.replace('play', " ")
            talk("Playing" + song)
            pywhatkit.playonyt(song)
            webbrowser.get('chrome').open_new_tab(song)
            play_opened = True
            
        elif 'time' in instruction:
            current_time = datetime.datetime.now().strftime('%I:%M%p')
            talk('Current time is ' + current_time)
            
        elif 'date' in instruction:
            current_date = datetime.datetime.now().strftime('%d /%m /%Y')
            talk("Today's date is " + current_date)
            
        elif 'how are you' in instruction:
            talk('I am fine, how about you?')
            
        elif 'what is your name' in instruction:
            talk('I am Friday, how can I help you?')
            
        elif 'who is' in instruction:
            instruction = instruction.replace('who is', " ")
            results = wikipedia.summary(instruction, sentences=2)
            talk("According to Wikipedia")
            print(results)
            talk(results)
            
        elif 'what is' in instruction:
            instruction = instruction.replace('what is', " ")
            results = wikipedia.summary(instruction, sentences=2)
            talk("According to Wikipedia")
            print(results)
            talk(results)
            
        elif 'open camera' in instruction:
            talk('Okay')
            subprocess.run('start microsoft.windows.camera:', shell=True)
        elif 'close camera' in instruction:
            talk('Right away')
            subprocess.run('Taskkill /IM WindowsCamera.exe /F', shell=True)
            
        elif 'open google' in instruction and not google_opened:
            talk("Opening Google...")
            url = "https://www.google.com"
            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
            webbrowser.get('chrome').open_new_tab(url)
            google_opened = True
            
        elif 'close google' in instruction and google_opened:
            pyautogui.hotkey('ctrl', 'w')
            google_opened = False
            talk("Closing Google tab.")
            
        elif 'open youtube' in instruction and not youtube_opened:
            talk("Opening YouTube...")
            url = "https://www.youtube.com/"
            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
            webbrowser.get('chrome').open_new_tab(url)
            youtube_opened = True
            
        elif 'close youtube' in instruction and youtube_opened:
            pyautogui.hotkey('ctrl', 'w')
            youtube_opened = False
            talk("Closing YouTube tab.")
            
        elif 'open cutting tools' in instruction:
            talk("Opening snip application...")
            os.startfile('SnippingTool.exe')
            
        elif 'close cutting tools' in instruction:
            talk("Closing snip application...")
            os.system('taskkill /f /im SnippingTool.exe')
            
        elif 'give me facts' in instruction:
            wikipedia_page = wikipedia.random()
            summary = wikipedia.summary(wikipedia_page, sentences=1)
            print(summary)
            talk(summary)
            
        elif 'send whatsapp message' in instruction:
            get_user_phone_number()
            talk("What message do you want to send?")
            message = input_instruction()
            
            send_whatsapp_message(user_phone_number, message)

            
        elif 'close program' in instruction:
            talk("Closing Friday program...")
            quit()


def run_program():
    while True:
        play_friday()
        time.sleep(0.1)


def start_program():
    global program_thread
    program_thread = threading.Thread(target=run_program)
    program_thread.start()


root = tk.Tk()
root.geometry("550x300")
root.title("Virtual Assistant Friday")
Label = tk.Label(root, text="Virtual Assistant Friday", font=("Times new romain", 25), fg="black", bg="pink")
Label.pack()
root.configure(background="cyan")

status_label = tk.Label(root, text="Listening...", font=("Times New Roman", 14), fg="black", bg="cyan")
status_label.pack(pady=20, side="bottom")

start_button = tk.Button(root, text="Start", command=start_program, width=6, height=2)
start_button.pack(side="left", padx=100, pady=5)
update_status_text("Listening...")

phone_frame = tk.Frame(root, bg="cyan")
phone_frame.pack(pady=10)

phone_label = tk.Label(phone_frame, text="Phone Number:", font=("Times New Roman", 14), bg="cyan")
phone_label.pack(side="left")

phone_entry = tk.Entry(phone_frame, font=("Times New Roman", 14))
phone_entry.pack(side="left")


root.mainloop()
