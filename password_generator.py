import string
import random

password = ("")
characters = 16
for i in range(characters) :
    password += (random.choice(string.punctuation + string.digits + string.ascii_letters))