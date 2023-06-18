from win32com.client import Dispatch

speak = Dispatch("SAPI.SpVoice").Speak
print("Hii, I'm your Dev Speaker")

while True:
    inp = input("What shall I speak for you: ")
    if inp == 'bye':
        speak("Bye buddy")
        break
    speak(inp)
