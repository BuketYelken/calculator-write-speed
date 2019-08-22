
from datetime import datetime

text = "People have to make a choice between happiness and freedom and most of them were choosing happiness"
print("Welcome...\nPlease write that: " + text)

timestart = datetime.now()

typing = input()

if text == typing:
    timefinish = datetime.now()
else:
    text == typing

difference = timefinish-timestart

print("Your speed of writing: {}".format(difference))

