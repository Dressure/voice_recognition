#!/usr/bin/python
# -*- coding: utf-8 -*-

import speech_recognition as sr
import sys
import subprocess
import os

def open_app(r):
    with sr.Microphone() as source:
        print("Quelle application souhaitez-vous ouvrir ?")
        audio = r.listen(source)
    try:
        app = r.recognize_google(audio, language="fr-FR")
        print("J'ouvre " + app)
        os.system(app.lower())
    except sr.UnknownValueError:
        print("Je n'ai pas compris")
    except sr.RequestError as e:
        print("Le service Google Speech API ne fonctionne plus" + format(e))

# def close_app(r):
#     with sr.Microphone() as source:
#         print("Quelle application souhaitez-vous fermer ?")
#         audio = r.listen(source)
#     try:
#         app = r.recognize_google(audio, language="fr-FR")
#         print("Je ferme " + app)
#         os.system("killall" +  app)
#     except sr.UnknownValueError:
#         print("Je n'ai pas compris")
#     except sr.RequestError as e:
#         print("Le service Google Speech API ne fonctionne plus" + format(e))

def write_in_file(r, filename):
    with sr.Microphone() as source:
        print("Que dois-je ecrire dans le fichier " + filename) # problème d'accent
        audio = r.listen(source)
    try:
        input_in_file = r.recognize_google(audio, language="fr-FR")
        test_file = open(filename, "w")
        test_file.write(input_in_file)
        test_file.close()
        print(input_in_file + " has been added to file")

    except sr.UnknownValueError:
        print("Je n'ai pas compris")
    except sr.RequestError as e:
        print("Le service Google Speech API ne fonctionne plus" + format(e))


def create_file(r):
    with sr.Microphone() as source:
        print("Quel est le nom du fichier que vous souhaitez ouvrir ?")
        audio = r.listen(source)
    try:
        filename = r.recognize_google(audio, language="fr-FR")
        print("J'ouvre " + filename)
        write_in_file(r, filename)
    except sr.UnknownValueError:
        print("Je n'ai pas compris")
    except sr.RequestError as e:
        print("Le service Google Speech API ne fonctionne plus" + format(e))

def main():
    while True:
        r  = sr.Recognizer()
        with sr.Microphone() as source:
            print("Dites moi quelque chose..")
            audio = r.listen(source)
        try:
            text = r.recognize_google(audio, language="fr-FR")
            print("Vous avez dit : " + text)
            if (text == "fermer le programme"):
                print("Programme fermé !")
                sys.exit(0)
            if (text == "ouvrir une application"):
                open_app(r)
            if (text == "ouvrir un fichier"):
                create_file(r)
        except sr.UnknownValueError:
            print("Je n'ai pas compris")
        except sr.RequestError as e:
            print("Le service Google Speech API ne fonctionne plus" + format(e))

if __name__ == "__main__":
    main()