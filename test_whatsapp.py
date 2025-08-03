import pywhatkit
import datetime

# Test the pywhatkit functionality
print("Testing pywhatkit functionality...")

# Test phone number (replace with a real number for testing)
test_phone = "+1234567890"  # Replace with your actual phone number
test_message = "Test message from Friday assistant"

# Get current time and schedule for 1 minute later
now = datetime.datetime.now()
hour = now.hour
minute = now.minute + 1

if minute >= 60:
    minute = minute - 60
    hour = hour + 1

if hour >= 24:
    hour = 0

print(f"Current time: {now.hour}:{now.minute}")
print(f"Scheduling message for: {hour}:{minute}")
print(f"Phone: {test_phone}")
print(f"Message: {test_message}")

try:
    # This will open WhatsApp Web and schedule the message
    # pywhatkit.sendwhatmsg(test_phone, test_message, hour, minute)
    print("Test completed successfully (commented out actual sending)")
except Exception as e:
    print(f"Error: {e}")

print("\nMake sure to:")
print("1. Have WhatsApp Web logged in")
print("2. Replace test_phone with a real number") 
print("3. Uncomment the sendwhatmsg line to test")
