The AI Voice Assistant is a real-time voice interaction system built using Python. This assistant is capable of understanding and responding to various voice commands, making it a versatile tool for a variety of tasks such as web searches, playing music, and fetching real-time information.

Features:
Real-time speech recognition and response: The assistant listens to the user's voice commands and responds promptly.
Wikipedia search functionality: Search and retrieve summaries from Wikipedia.
Open websites: Quickly open websites like YouTube, Google, and Stack Overflow.
Play music: Play music from a specified directory on your computer.
Tell the current time: Inform the user of the current time.
Fetch weather details: Provide current weather details for a specified city using the OpenWeatherMap API.

Installation-
To run this project on your local machine, follow these steps:
-Clone the repository
-Create a virtual environment
-Install the required packages
-Replace the placeholder with your OpenWeatherMap API key in the getWeather function.
-Run the application: python main.py

Usage:
After running the application, the AI Voice Assistant will greet you based on the time of day and start listening for commands. Speak your command clearly into the microphone, and the assistant will respond accordingly.

Example Commands
Here are some example commands you can try with the AI Voice Assistant:
Greetings: "Hello", "Hi", "Hey"
Search Wikipedia: "Search Wikipedia for Python"
Open Websites: "Open YouTube", "Open Google", "Open Stack Overflow"
Play Music: "Play music"
Get Time: "What is the time?"
Get Weather: "What's the weather in New York?"
Exit: "Quit"

How It Works-
Initialization: The assistant initializes the speech engine and sets up voice properties.
Greeting: It greets the user based on the time of day.
Listening for Commands: The assistant continuously listens for voice commands using the microphone.
Processing Commands: Once a command is detected, it processes the command to determine the appropriate action.
Executing Actions: The assistant executes the required action, such as opening a website, playing music, or fetching weather details.
Responding: It provides a verbal response to the user, confirming the action or providing the requested information.

Limitations-
The assistant requires an active internet connection for certain functionalities like Wikipedia searches and fetching weather details.
The accuracy of speech recognition may vary based on the clarity of speech and ambient noise.

Future Enhancements-
Adding more functionalities and commands.
Improving speech recognition accuracy.
Integrating with other APIs for more diverse information retrieval.

The Voice Assistant is a versatile and interactive system that leverages Python's capabilities to provide real-time voice interaction. It showcases the integration of various libraries and APIs to perform tasks efficiently.
