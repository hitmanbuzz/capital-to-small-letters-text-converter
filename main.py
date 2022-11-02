# Any words or sentence/s, you can change it into small letters
# Made by Moirangthem Henthoiba / HITMAN / H I T M A N
# Same Programmer/Coder

# CODE BELOW 👇

words = open('Words.txt', 'r')
r = words.read()

lower = r.lower()
with open('Result.txt', 'w') as f:
    f.write(lower)
    f.write('\n')

# CODE DONE