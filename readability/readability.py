from cs50 import get_string
from cs50 import get_float

#Initializing variables
words = 0
sentence = 0
char = 0

# Recieving the text
text = input("Text: ")

#incrementint the first word
words += 1

# interating on the text and couting the Characters, Words and Sentences
for i in range(len(text)):
    if text[i].isalpha():
        char += 1
    elif text[i] == ' ' and text[i+1] != ' ':
        words += 1
    elif (text[i] == '?') or (text[i] == '.') or (text[i] == '!'):
        sentence += 1
    else: # if the text is equals to other symbols
        if words > char: # if only symbols are entered
            words = 0

# to unable the division by 0, wish returns error. Calculating the grade
if words != 0:
    L = (char*100)/words
    S = (sentence*100)/words
    index = round(((0.0588 * L) - (0.296 * S) - 15.8))

    #Grade result
    if (index < 1):
        print("Before Grade 1\n")
    elif (index > 16):
        print("Grade 16+")
    else:
        print(f"Grade {index}")