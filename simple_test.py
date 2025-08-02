import tkinter as tk
from tkinter import messagebox
import pyttsx3

def test_tts():
    try:
        engine = pyttsx3.init()
        engine.say("Hello, Friday is working!")
        engine.runAndWait()
        messagebox.showinfo("Success", "Text-to-speech is working!")
    except Exception as e:
        messagebox.showerror("Error", f"TTS Error: {e}")

def test_mic():
    try:
        import speech_recognition as sr
        recognizer = sr.Recognizer()
        
        with sr.Microphone() as source:
            messagebox.showinfo("Info", "Speak now for 3 seconds...")
            audio = recognizer.listen(source, timeout=3)
            
        text = recognizer.recognize_google(audio)
        messagebox.showinfo("Success", f"You said: {text}")
        
    except Exception as e:
        messagebox.showerror("Error", f"Microphone Error: {e}")

# Create simple test GUI
root = tk.Tk()
root.title("Friday Test")
root.geometry("300x200")
root.configure(bg="cyan")

tk.Label(root, text="Friday Component Test", font=("Arial", 16), bg="cyan").pack(pady=20)

tk.Button(root, text="Test Text-to-Speech", command=test_tts, width=20, height=2).pack(pady=10)
tk.Button(root, text="Test Microphone", command=test_mic, width=20, height=2).pack(pady=10)

print("Test GUI starting...")
root.mainloop()
print("Test GUI closed.")
