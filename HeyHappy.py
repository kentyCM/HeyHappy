import speech_recognition as aa
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import time

# Initialization
listener = aa.Recognizer()
machine = pyttsx3.init()

# Define a function to speak text
def talk(text):
    machine.say(text)
    machine.runAndWait()

# Function to get instruction
def input_instruction():
    global instruction
    try:
        with aa.Microphone() as origin:
            print("Listening...")
            speech = listener.listen(origin)
            instruction = listener.recognize_google(speech)  # waiting to capture user's voice
            instruction = instruction.lower()  # Make input received locked to lowercase
            if "happy" in instruction:
                instruction = instruction.replace('happy', " ")
                print(instruction)  # any instruction with "happy" will respond if not it won't
    except:
        pass
    return instruction

# Function to handle commands
def play_Happy():
    instruction = input_instruction()  # Call the function to get the instruction
    print(instruction)
    if "play" in instruction:  # Plays a song if "play" is mentioned
        song = instruction.replace('play', "")
        talk("playing " + song)
        pywhatkit.playonyt(song)

    elif 'time' in instruction:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)

    elif 'date' in instruction:
        date = datetime.datetime.now().strftime('%d/%m/%Y')
        talk("Today's date is " + date)

    elif 'how are you' in instruction:
        talk("I am fine, how about you?")
    
    elif 'what is your name' in instruction:
        talk('I am Happy, what can I do for you?')

    elif 'who is' in instruction:
        human = instruction.replace('who is', " ")
        info = wikipedia.summary(human, 1)
        print(info)
        talk(info)
    
    elif 'set reminder' in instruction:
        set_reminder()

    elif 'manage schedule' in instruction:
        manage_schedule()

    elif 'ask' in instruction:
        answer_query(instruction)
    
    else:
        talk('Please repeat')

# Function to set a reminder 
def set_reminder():
    talk("What would you like to be reminded about?")
    reminder = input_instruction()
    talk("In how many seconds should I remind you?")
    delay = int(input_instruction())
    talk(f"Reminder set for {reminder} in {delay} seconds")
    time.sleep(delay)
    talk(f"Reminder: {reminder}")

# Function to manage schedule
def manage_schedule():
    talk("Please say the task you want to add to your schedule.")
    task = input_instruction()
    # Here you might save the task to a file or a database
    talk(f"Task '{task}' added to your schedule.")
    # For simplicity, we'll just confirm it was "added."

# Function to answer general queries
def answer_query(instruction):
    query = instruction.replace("ask", "")
    talk(f"Searching for {query}")
    # Search Wikipedia for the query (1 sentence)
    info = wikipedia.summary(query, sentences=1)
    print(info)
    talk(info)

play_Happy()
