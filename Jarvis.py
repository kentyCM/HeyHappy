import speech_recognition as aa
import pyttsx3
import pywhatkit
import datetime
import wikipedia

#initialisation
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
            print("Listening")
            speech = listener.listen(origin)
            instruction = listener.recognize_google(speech)  # waiting to capture user's voice
            
            instruction = instruction.lower()  # Make input received locked to lowercase
            if "jarvis" in instruction:
                instruction = instruction.replace('jarvis', " ")
                print(instruction)  # any instruction with "Jarvis" will respond if not it won't

    except:
        pass
    return instruction

# Function to handle commands
def play_Jarvis():
    instruction = input_instruction()  # Call the function to get the instruction
    print(instruction)
    if "play" in instruction:  # Performs the functionalities if there's play
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
        talk('I am Jarvis, what can I do for you?')

    elif 'who is' in instruction:
        human = instruction.replace('who is', " ")
        info = wikipedia.summary(human, 1)
        print(info)
        talk(info)
    
    else:
        talk('Please repeat')

play_Jarvis()
