"""
I feel like I'm supposed to do some weird ass lisence thing so uhh here ig

Made by Squirrel Gay Acorns. Uhhh lisenced under uhh nothing I think

You can use this or some shit, I don't give a fuck LMFAO
"""

import speech_recognition as sr
import pyttsx3
import time
import threading


recognizer = sr.Recognizer()
engine = pyttsx3.init()


engine.setProperty('rate', 150)
engine.setProperty('volume', 1)


def speak(text):
    engine.say(text)
    engine.runAndWait()


def listen():
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Listening... Say something.")
        speak("Listening... Say something...")
        
        while True:
            try:
                audio = recognizer.listen(source, timeout=5)
                print("Recognizing...")
                text = recognizer.recognize_google(audio)
                print(f"You said: {text}")
                speak(f"You said: {text}")


                if 'stop' in text.lower():
                    print("Stopping...")
                    speak("bai")
                    break

                elif 'hello' in text.lower():
                    speak("hai!")
                elif 'how are you' in text.lower():
                    speak("I'm uhh python..")
                
            except sr.UnknownValueError:
                print("I didn't understand..")
                speak("didn't understand..")
            except sr.RequestError:
                print("I couldn't connect to the speech recognition service.")
                speak("I couldn't connect to the speech recognition service.")
            except Exception as e:
                print(f"An error occurred: {e}")
                speak("error..")
            

            time.sleep(1)


if __name__ == "__main__":
    threading.Thread(target=engine.runAndWait).start()
    listen()
