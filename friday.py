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
try:
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    if voices:
        engine.setProperty('voice', voices[0].id)  # Set the desired voice
    print("Text-to-speech engine initialized successfully")
except Exception as e:
    print(f"Error initializing text-to-speech: {e}")
    engine = None

# Set up flag variables
google_opened = False
youtube_opened = False
play_opened = False

# Global variable for storing the user's phone number
user_phone_number = ""


def talk(text):
    try:
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        print(f"Error in text-to-speech: {e}")


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
    try:
        # Ensure phone number format is correct (with + prefix for pywhatkit)
        if not phone_number.startswith('+'):
            phone_number = '+' + phone_number
        
        # First, open WhatsApp Web to ensure it's ready
        talk("Opening WhatsApp Web. Please make sure you're logged in.")
        webbrowser.open("https://web.whatsapp.com")
        time.sleep(3)  # Give time for page to load
        
        talk("Sending your message. Please wait.")
        update_status_text("Sending WhatsApp message...")
        print(f"Sending message to: {phone_number}")
        print(f"Message: {message}")
        
        # Use scheduled message instead of instant (more reliable)
        now = datetime.datetime.now()
        hour = now.hour
        minute = now.minute + 1  # Send 1 minute from now
        
        # Handle minute overflow
        if minute >= 60:
            minute = minute - 60
            hour = hour + 1
        
        # Handle hour overflow (24-hour format)
        if hour >= 24:
            hour = 0
        
        talk(f"Scheduling message to send at {hour}:{minute:02d}. Please keep WhatsApp Web open.")
        
        # Send scheduled message
        pywhatkit.sendwhatmsg(phone_number, message, hour, minute)
        print("Message scheduled successfully")
        talk("Message has been scheduled and will be sent automatically.")
        
    except Exception as e:
        print(f"Error sending WhatsApp message: {str(e)}")
        talk("Sorry, there was an error sending the message.")
        
        # Try alternative approach with sendwhatmsg_instantly as backup
        try:
            talk("Trying instant send method...")
            update_status_text("Trying instant send...")
            
            # Give more time for WhatsApp Web to be ready
            talk("Please make sure WhatsApp Web is open and logged in. Sending in 10 seconds.")
            time.sleep(10)
            
            pywhatkit.sendwhatmsg_instantly(phone_number, message, 15, True)
            print("Message sent via instant method")
            talk("Message sent successfully via instant method")
            
        except Exception as e2:
            print(f"Both methods failed: {str(e2)}")
            talk("Both sending methods failed. Please check your WhatsApp Web connection and make sure you're logged in.")


def get_user_phone_number():
    global user_phone_number
    phone_number = phone_entry.get().strip()
    
    # Validate phone number format
    if not phone_number:
        talk("Please enter a phone number.")
        return False
        
    # Remove any spaces or special characters except + and digits
    cleaned_number = ''.join(char for char in phone_number if char.isdigit() or char == '+')
    
    # Ensure it starts with + (add if missing)
    if not cleaned_number.startswith('+'):
        # Assume it's missing the country code prefix
        if len(cleaned_number) == 10:  # US number without country code
            cleaned_number = '+1' + cleaned_number
        else:
            cleaned_number = '+' + cleaned_number
    
    if len(cleaned_number) < 12:  # Minimum: +XX XXXXXXXXX
        talk("Please enter a valid phone number with country code. Example: +1234567890")
        return False
        
    user_phone_number = cleaned_number
    print(f"Phone number set to: {user_phone_number}")
    return True


def get_user_message():
    talk("What message do you want to send? Please speak your message now.")
    update_status_text("Speak your message...")
    
    try:
        with sr.Microphone() as source:
            print("Listening for message...")
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            audio = recognizer.listen(source, timeout=10)  # 10 second timeout
            try:
                message = recognizer.recognize_google(audio)
                message = message.strip()
                print(f"Message received: {message}")
                update_status_text(f"Message: {message}")
                return message
            except sr.UnknownValueError:
                talk("I didn't hear a message clearly. Please try again.")
                update_status_text("Message not understood")
                return None
    except sr.RequestError as e:
        print(f"Error occurred during speech recognition: {str(e)}")
        talk("Sorry, there was an error with speech recognition.")
        return None
    except sr.WaitTimeoutError:
        talk("I didn't hear anything. Please try again.")
        update_status_text("No message heard")
        return None


def update_status_text(text):
    status_label.config(text=text)


def play_friday():
    instruction = input_instruction()
    if instruction == '':
        print("Invalid command")
        talk('Invalid command. Say "Friday" first.')
        update_status_text("Listening...")
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
            try:
                query = instruction.replace('who is', "").strip()
                results = wikipedia.summary(query, sentences=2)
                talk("According to Wikipedia")
                print(results)
                talk(results)
            except Exception as e:
                print(f"Wikipedia error: {e}")
                talk("Sorry, I couldn't find information about that.")
            
        elif 'what is' in instruction:
            try:
                query = instruction.replace('what is', "").strip()
                results = wikipedia.summary(query, sentences=2)
                talk("According to Wikipedia")
                print(results)
                talk(results)
            except Exception as e:
                print(f"Wikipedia error: {e}")
                talk("Sorry, I couldn't find information about that.")
            
        elif 'open camera' in instruction:
            talk('Okay')
            subprocess.run('start microsoft.windows.camera:', shell=True)
        elif 'close camera' in instruction:
            talk('Right away')
            subprocess.run('Taskkill /IM WindowsCamera.exe /F', shell=True)
            
        elif 'open google' in instruction and not google_opened:
            talk("Opening Google...")
            url = "https://www.google.com"
            try:
                webbrowser.open(url)
                google_opened = True
            except Exception as e:
                print(f"Error opening Google: {e}")
                talk("Sorry, I couldn't open Google.")
            
        elif 'close google' in instruction and google_opened:
            try:
                pyautogui.hotkey('ctrl', 'w')
                google_opened = False
                talk("Closing Google tab.")
            except Exception as e:
                print(f"Error closing Google: {e}")
            
        elif 'open youtube' in instruction and not youtube_opened:
            talk("Opening YouTube...")
            url = "https://www.youtube.com/"
            try:
                webbrowser.open(url)
                youtube_opened = True
            except Exception as e:
                print(f"Error opening YouTube: {e}")
                talk("Sorry, I couldn't open YouTube.")
            
        elif 'close youtube' in instruction and youtube_opened:
            try:
                pyautogui.hotkey('ctrl', 'w')
                youtube_opened = False
                talk("Closing YouTube tab.")
            except Exception as e:
                print(f"Error closing YouTube: {e}")
            
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
            try:
                if get_user_phone_number():
                    # Get the message via dedicated voice input
                    message = get_user_message()
                    if message:
                        print(f"Sending WhatsApp message: '{message}' to {user_phone_number}")
                        send_whatsapp_message(user_phone_number, message)
                        talk("Message sent. Ready for next command.")
                        update_status_text("Ready for commands")
                    else:
                        talk("No message received. Ready for next command.")
                        update_status_text("Ready for commands")
                else:
                    talk("Please enter a valid phone number first.")
            except Exception as e:
                print(f"WhatsApp error: {e}")
                talk("Sorry, I couldn't send the WhatsApp message. Make sure WhatsApp Web is logged in.")
                update_status_text("WhatsApp error - Ready for commands")

            
        elif 'close program' in instruction:
            talk("Closing Friday program...")
            quit()
        
        # Reset status to listening after each command (except WhatsApp which handles its own status)
        if 'send whatsapp message' not in instruction:
            update_status_text("Listening...")


def run_program():
    while True:
        play_friday()
        time.sleep(0.1)


def start_program():
    global program_thread
    program_thread = threading.Thread(target=run_program)
    program_thread.start()


root = tk.Tk()
root.geometry("600x300")
root.title("Virtual Assistant Friday")
Label = tk.Label(root, text="Virtual Assistant Friday", font=("Times New Roman", 25), fg="black", bg="pink")
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

# Add instruction label
instruction_label = tk.Label(root, text="Instructions: 1. Enter phone number 2. Say 'Friday send whatsapp message' 3. Speak your message when prompted", 
                           font=("Times New Roman", 10), bg="cyan", fg="darkblue", wraplength=600)
instruction_label.pack(pady=20)


root.mainloop()
