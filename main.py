#-*- coding: utf-8 -*-
'''
from chatterbot import ChatBot

bot = ChatBot('RuhJay')
bot = ChatBot(
    'Norman',
    storage_adapter='chatterbot.storage.JsonFileStorageAdapter',
    input_adapter='chatterbot.input.TerminalAdapter',
    output_adapter='chatterbot.output.TerminalAdapter',
    logic_adapters=[
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.TimeLogicAdapter'
    ],
    database='./database.json'
)


while True:
    try:
     bot_input = bot.get_response("3 + 7")

    except(KeyboardInterrupt, EOFError, SystemExit):
        break
'''

# TIME AND MATHEMATICAL ANALYSIS
# -*- coding: utf-8 -*-
'''
from chatterbot import ChatBot
import logging


# Uncomment the following line to enable verbose logging
# logging.basicConfig(level=logging.INFO)

# Create a new instance of a ChatBot
bot = ChatBot("Terminal",
    storage_adapter="chatterbot.storage.JsonFileStorageAdapter",
    logic_adapters=[
        "chatterbot.logic.MathematicalEvaluation",
        "chatterbot.logic.TimeLogicAdapter",
        "chatterbot.logic.BestMatch"
    ],
    input_adapter="chatterbot.input.TerminalAdapter",
    output_adapter="chatterbot.output.TerminalAdapter",
    database="../database.db"
)

print("Type something to begin...")

# The following loop will execute each time the user enters input
while True:
    try:
        # We pass None to this method because the parameter
        # is not used by the TerminalAdapter
        bot_input = bot.get_response(None)

    # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        break
'''

# -*- coding: utf-8 -*-
'''
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

chatterbot = ChatBot("Training Example")
chatterbot.set_trainer(ListTrainer)

chatterbot.train([
    "Hi there!",
    "Hello",
])

chatterbot.train([
    "Greetings!",
    "Hello",
])

print chatterbot.get_response("Hi there!")
'''

# -*- coding: utf-8 -*-
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer
import csv

chatterbot = ChatBot("RuhJay")
chatterbot.set_trainer(ChatterBotCorpusTrainer)
chatterbot.set_trainer(ListTrainer)

#!/usr/bin/env python3

# NOTE: this example requires PyAudio because it uses the Microphone class

import speech_recognition as sr

'''
name = raw_input("Hello ! Welcome to RuhJay Bot ! What is your name ?")
account_no = raw_input("What is your account number ?")
account_balance = raw_input("What is my account balance ?")

if account_no == 12345 :
    bro_acc_no = 5439435
    bro_acc_bal = 450.65

if account_no == 54321 :
    bro_acc_no = 3244113
    bro_acc_bal = 110.67
    '''

account = raw_input("What is your account number ?")


with open('bank.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in reader:
         if account == row['account'] :
             name = row['name']
             bal = row['bal']

while True:
    chatterbot.train([
        "What is my account number ?",
            account ,
    ])

    chatterbot.train([
        "What is my name ?",
        name,
    ])

    chatterbot.train([
        "What is my account balance ?",
        bal,
    ])

    chatterbot.train([
        "I want to tranfer data",
        "No",
    ])
    chatterbot.train([
        "I want to transfer",
        "Enter Account number"
    ])

    # obtain audio from the microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)# obtain audio from the microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Hi How Can I Help You ?")
        audio = r.listen(source)

    # recognize speech using Google Speech Recognition
    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        print chatterbot.get_response(r.recognize_google(audio))
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
