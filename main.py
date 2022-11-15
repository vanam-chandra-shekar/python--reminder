from PyDictionary import PyDictionary
from plyer import notification
import random
import time


file = open('words.txt','r')
words = file.read().split(',')
file.close()


def nofify_word(sec:int):
    rand_word = words[random.randrange(0,len(words)-1)].strip('\n')
    dictionary = PyDictionary()
    print(rand_word)
    keys = list(dictionary.meaning(rand_word).keys())
    meaning = dictionary.meaning(rand_word)[keys[0]][0]

    notification.notify(
        title = rand_word,
        message = meaning,
        app_name = 'reminder',
        timeout = 6
    )
    time.sleep(sec)

def reminder(sec:int,mssg:str):
    time.sleep(sec)
    notification.notify(
        title = 'Reminder',
        message = mssg,
        timeout = 4
    )


command = str(input('> '))

if 'remind' in command or 'Remind' in command:
    command = command.split(' ',2)
else:
    command = command.split(' ')


if (command[0] == 'remind' or command[0] == 'Remind') and len(command) ==3:
    if command[1].isdigit():
        reminder(int(command[1]),command[2])
    else:
        print('Enter valid parameters')
elif command[0] == 'remindword' and len(command) == 2:
    if command[1].isdigit():
        while True:
            nofify_word(int(command[1]))
else:
    print('enter a valid command')