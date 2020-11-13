# pip install SpeechRecognition
import speech_recognition as sr

r = sr.Recognizer()

# Script without any function
with sr.Microphone() as source:
        print("\nSpeak something...")
        audio = r.listen(source)

        try:
            text = r.recognize_google(audio)
            print("You said : " + text)

        except Exception as e:
            print(e)
            print("Error, couldn't recognize your voice.")

# Script with a function
def take_my_command():
    with sr.Microphone() as source:
        print("\nSpeak something...")
        audio = r.listen(source)

        try:
            text = r.recognize_google(audio)
            print("You said : " + text)

        except Exception as e:
            print(e)
            print("Error, couldn't recognize your voice.")

take_my_command()
