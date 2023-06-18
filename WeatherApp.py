import threading
import pythoncom
import requests
import json
from win32com.client import Dispatch

def speak_text(text):
    speak = Dispatch("SAPI.SpVoice").Speak
    speak(text)

def get_input():
    city = input("Which city are you looking for: ")
    return city

def results(city):
    address = f'https://api.weatherapi.com/v1/current.json?key=b13989793f184149a91141538230103&q={city}'
    req = requests.get(address)
    dic = json.loads(req.text)
    temp = dic['current']['temp_c']
    cond = dic['current']['condition']['text']
    humid = dic['current']['humidity']
    speak_text(f"It is {temp} degrees Celsius in {city} currently. The condition is {cond} with {humid} humidity")

def speech_thread():
    pythoncom.CoInitialize()
    speak_text("Which city are you looking for")

def main():
    t = threading.Thread(target=speech_thread)
    t.start()
    city = get_input()
    t.join()
    results(city)

if __name__ == '__main__':
    main()
