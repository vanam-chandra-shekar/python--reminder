from PyDictionary import PyDictionary
from plyer import notification
import random


file = open('words.txt','r')
words = file.read().split(',')
file.close()
rand_word = words[random.randrange(0,len(words)-1)].strip('\n')


dictionary = PyDictionary()
keys = list(PyDictionary.meaning(rand_word).keys())
meaning = PyDictionary.meaning(rand_word)[keys[0]][0]

notification.notify(
    title = rand_word,
    message = meaning,
    app_name = 'reminder',
    timeout = 6
)
