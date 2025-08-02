import tkinter as tk
import threading
import time

def test_function():
    print("Button clicked!")
    
def background_task():
    while True:
        print("Background task running...")
        time.sleep(2)

def start_background():
    thread = threading.Thread(target=background_task)
    thread.daemon = True
    thread.start()

# Create GUI
root = tk.Tk()
root.geometry("400x200")
root.title("Friday Test")
root.configure(background="cyan")

# Add label
label = tk.Label(root, text="Friday Test", font=("Times New Roman", 20), fg="black", bg="pink")
label.pack(pady=20)

# Add button
button = tk.Button(root, text="Test", command=test_function, width=10, height=2)
button.pack(pady=10)

# Add background button
bg_button = tk.Button(root, text="Start Background", command=start_background, width=15, height=2)
bg_button.pack(pady=10)

print("Starting GUI...")
root.mainloop()
print("GUI closed.")
