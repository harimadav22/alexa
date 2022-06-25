import speech_recognition as sr
import pyttsx3;
Listener = sr.Recognizer()
engine = pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.say('Hi iam alexa iam your assistant')
engine.runAndWait()
def take_command():
    try:
        with sr.Microphone() as source:
            print('Listening.....')
            voice = listener.listen(source)
            Command = Listener.recognize_google(voice)
            command = command.lower()
            if'alexa' in command:
                command=command.replace('alexa','')
                print(command)
    except:
        pass
def run_alexa():
    Command = take_command()
    print(Command)
    if'paly'in Command:
        song=command.replace
run_alexa()