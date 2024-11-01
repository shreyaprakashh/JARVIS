import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'veda' in command:
                command = command.replace('veda', '')
                print(command)
    except:
        pass
    return command


def run_veda():
    command = take_command()
    print(command)
    if 'hi veda' in command:
        talk('Hi! How may I help you?')

    elif 'alexa' in command:
        talk('who is alexa? I am veda')

    elif 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)

    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)

    elif 'date' in command:
        time = datetime.datetime.now().strftime('%B %d, %Y')
        talk('Today is ' + time)

    elif 'tell me a joke' in command:
        talk(pyjokes.get_joke())

    else:
        talk('Please say the command again.')


while True:
    run_veda()
