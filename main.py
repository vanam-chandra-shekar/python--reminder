from PyDictionary import PyDictionary
from plyer import notification
import random
import time


file = open('words.txt','r')
words = file.read().split(',')
file.close()


def nofify(sec:int):
    rand_word = words[random.randrange(0,len(words)-1)].strip('\n')
    dictionary = PyDictionary()
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




remind_word = False

if __name__ == '__main__':
    while True:
        if remind_word:
            nofify(10)