#!/usr/bin/env python3
"""
Simple test script to check Friday components
"""

print("Testing Friday components...")

# Test 1: Import check
try:
    import speech_recognition as sr
    print("✓ SpeechRecognition imported successfully")
except ImportError as e:
    print(f"✗ Error importing SpeechRecognition: {e}")

try:
    import pyttsx3
    print("✓ pyttsx3 imported successfully")
except ImportError as e:
    print(f"✗ Error importing pyttsx3: {e}")

try:
    import pywhatkit
    print("✓ pywhatkit imported successfully")
except ImportError as e:
    print(f"✗ Error importing pywhatkit: {e}")

try:
    import wikipedia
    print("✓ wikipedia imported successfully")
except ImportError as e:
    print(f"✗ Error importing wikipedia: {e}")

try:
    import pyautogui
    print("✓ pyautogui imported successfully")
except ImportError as e:
    print(f"✗ Error importing pyautogui: {e}")

# Test 2: Text-to-speech
print("\nTesting Text-to-Speech...")
try:
    engine = pyttsx3.init()
    print("✓ TTS engine initialized")
    # Test voice
    engine.say("Hello, this is a test")
    engine.runAndWait()
    print("✓ TTS test completed")
except Exception as e:
    print(f"✗ TTS error: {e}")

# Test 3: Speech Recognition setup
print("\nTesting Speech Recognition setup...")
try:
    recognizer = sr.Recognizer()
    print("✓ Speech recognizer created")
    
    # Check microphone
    mic_list = sr.Microphone.list_microphone_names()
    print(f"✓ Found {len(mic_list)} microphones")
    for i, mic in enumerate(mic_list):
        print(f"  {i}: {mic}")
        
except Exception as e:
    print(f"✗ Speech recognition error: {e}")

# Test 4: GUI
print("\nTesting GUI...")
try:
    import tkinter as tk
    root = tk.Tk()
    root.withdraw()  # Hide the window
    print("✓ Tkinter GUI working")
    root.destroy()
except Exception as e:
    print(f"✗ GUI error: {e}")

print("\nTest completed!")
