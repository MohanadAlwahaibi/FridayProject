import pywhatkit

# Test to see the correct function signature
print("Available pywhatkit functions:")
print([func for func in dir(pywhatkit) if 'whats' in func.lower()])

# Check the function signature
import inspect
try:
    sig = inspect.signature(pywhatkit.sendwhatmsg_instantly)
    print(f"sendwhatmsg_instantly signature: {sig}")
except Exception as e:
    print(f"Error getting signature: {e}")

# Try to get documentation
print("\nFunction documentation:")
print(pywhatkit.sendwhatmsg_instantly.__doc__)
