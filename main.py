"""
import speech_recognition as sr

# Cria um reconhercedor
r = sr.Recognizer()

# Abrir o microfone para cptura
with sr.Microphone() as source:
    audio = r.listen(source)

    print(r.recognize_google(audio, language='pt'))
"""
# !/usr/bin/env python3

from vosk import Model, KaldiRecognizer
import os
import pyaudio
import pyttsx3
import json
import core
from nlu.classifier import classify
# Síntese de fala
engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[-2].id)


def speak(text):
    engine.say(text)
    engine.runAndWait()


def evaluate(text):
    entity = classify(text)
    if entity == 'time|getTime':
        speak(core.SystemInfo.get_time())
    if entity == 'time|getDate':
        speak(core.SystemInfo.get_date())
    # Abrir programas
    if entity == 'open|notepads':
        speak('Abrindo o bloco de notas')
        os.system('Notepads.exe')
    print(f'Text: {text} Entity: {entity}')


model = Model('model')
rec = KaldiRecognizer(model, 16000)

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1,
                rate=16000, input=True, frames_per_buffer=8000)
stream.start_stream()


while True:
    data = stream.read(4000, exception_on_overflow=False)
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):
        result = rec.Result()
        result = json.loads(result)
        if result is not None:
            text = result['text']
            evaluate(text)
            if text == 'pare' or text == 'fechar':
                speak('Obrigado Senhor')
                break
