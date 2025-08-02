"# Friday Virtual Assistant 🤖

A voice-activated virtual assistant inspired by Iron Man's AI assistant Friday. This Python-based project allows you to control your computer, browse the web, play media, send messages, and get information using voice commands.

## Features 🎯

### 🎤 Voice Recognition & Speech
- **Speech-to-Text**: Converts your voice commands to text using Google's speech recognition API
- **Text-to-Speech**: Responds back with synthesized voice feedback
- **Real-time Processing**: Continuously listens for voice commands

### 🎵 Media Control
- **Play Music**: Say "play [song name]" to search and play songs on YouTube
- **YouTube Integration**: Voice commands to open and close YouTube tabs
- **Automated Playback**: Seamlessly integrates with your browser for media control

### 🌐 Web Browser Automation
- **Google Control**: Open and close Google tabs with voice commands
- **YouTube Management**: Dedicated YouTube tab control
- **Chrome Integration**: Specifically designed to work with Google Chrome browser

### 📱 WhatsApp Messaging
- **Instant Messaging**: Send WhatsApp messages using voice commands
- **Voice-to-Message**: Speak your message and it gets sent automatically
- **Phone Number Integration**: GUI-based phone number entry system

### 📷 System Control
- **Camera Control**: Open and close Windows Camera application
- **Screenshot Tool**: Launch and close Windows Snipping Tool
- **Program Management**: Self-closing capability with voice commands

### 🧠 Information Assistant
- **Wikipedia Integration**: Get instant information about people, topics, and concepts
- **Time & Date**: Ask for current time or today's date
- **Random Facts**: Generate interesting random facts from Wikipedia
- **Conversational AI**: Responds to basic conversational queries

## Installation 📦

1. **Clone the repository**:
   ```bash
   git clone https://github.com/MohanadAlwahaibi/FridayProject.git
   cd FridayProject
   ```

2. **Install required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Additional Requirements**:
   - **Microphone**: Ensure your system has a working microphone
   - **Google Chrome**: The application is configured to work with Chrome browser
   - **Internet Connection**: Required for speech recognition and web features

## Usage 🚀

1. **Run the application**:
   ```bash
   python friday.py
   ```

2. **Launch the GUI**: The application window will open with a cyan and pink interface

3. **Enter Phone Number**: (Optional) Enter your phone number for WhatsApp functionality

4. **Click "Start"**: Begin voice recognition by clicking the Start button

5. **Give Voice Commands**: Speak clearly into your microphone

## Voice Commands 🗣️

### Media Commands
- `"play [song name]"` - Play music on YouTube
- `"open youtube"` - Open YouTube in browser
- `"close youtube"` - Close YouTube tab

### Web Commands
- `"open google"` - Open Google in browser
- `"close google"` - Close Google tab

### Information Commands
- `"what time is it"` or `"time"` - Get current time
- `"what is the date"` or `"date"` - Get today's date
- `"who is [person name]"` - Get Wikipedia information about a person
- `"what is [topic]"` - Get Wikipedia information about a topic
- `"give me facts"` - Get random interesting facts

### System Commands
- `"open camera"` - Launch Windows Camera app
- `"close camera"` - Close Windows Camera app
- `"open cutting tools"` - Launch Windows Snipping Tool
- `"close cutting tools"` - Close Windows Snipping Tool

### Communication Commands
- `"send whatsapp message"` - Send a WhatsApp message (requires phone number)

### Conversational Commands
- `"how are you"` - Get a friendly response
- `"what is your name"` - Learn about the assistant
- `"close program"` - Exit the application

## Technical Details 🔧

### Built With
- **Python 3.x** - Core programming language
- **SpeechRecognition** - Voice-to-text conversion
- **pyttsx3** - Text-to-speech synthesis
- **pywhatkit** - WhatsApp and YouTube automation
- **wikipedia** - Information retrieval
- **pyautogui** - GUI automation
- **tkinter** - Graphical user interface

### Architecture
- **Multi-threaded Design**: Voice recognition runs in background thread
- **Event-driven**: Responds to voice commands in real-time
- **Modular Functions**: Each feature is implemented as separate functions
- **GUI Integration**: Clean interface with status updates

## System Requirements 💻

- **Operating System**: Windows (configured for Windows-specific applications)
- **Python**: Version 3.6 or higher
- **Memory**: Minimum 4GB RAM recommended
- **Storage**: At least 100MB free space
- **Internet**: Required for speech recognition and web features
- **Hardware**: Working microphone and speakers/headphones

## File Structure 📁

```
FridayProject/
│
├── friday.py           # Main application file
├── requirements.txt    # Python dependencies
└── README.md          # Project documentation
```

## Contributing 🤝

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Create a Pull Request

## Future Enhancements 🚀

- [ ] Support for more web browsers
- [ ] Email sending capabilities
- [ ] Weather information integration
- [ ] Calendar and reminder features
- [ ] Smart home device control
- [ ] Multiple language support
- [ ] Custom wake word configuration

## Troubleshooting 🔧

### Common Issues:
1. **Microphone not working**: Check system microphone permissions
2. **Speech recognition errors**: Ensure stable internet connection
3. **Chrome not opening**: Verify Chrome installation path
4. **WhatsApp messages not sending**: Check phone number format and WhatsApp Web setup

## License 📄

This project is open source and available under the [MIT License](LICENSE).

## Author 👨‍💻

**Mohanad Alwahaibi**
- GitHub: [@MohanadAlwahaibi](https://github.com/MohanadAlwahaibi)

## Acknowledgments 🙏

- Inspired by Iron Man's Friday AI assistant
- Built with Python's amazing ecosystem of libraries
- Thanks to the open-source community for the tools and libraries used

---

*Made with ❤️ by Mohanad Alwahaibi*" 
