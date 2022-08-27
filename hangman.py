from random import randint;

words = ['automn', 'spring', 'winter', 'summer'];
index = randint(0, len(words)-1);
print (index);
word = words[index];
print(word);
hangman = """
|-----------------|
|                 |
|  |----|         |
|  |    |         |
|  |    1         |
|  |   234        |
|  |    3         |
|  |   5 6        |
|  |              |
|  |--------      |
|                 |
|-----------------|
"""
print(hangman)

def print_hangman(errors):
    hangman = """
|-----------------|
|                 |
|  |----|         |
|  |    |         |
|  |    1         |
|  |   234        |
|  |    3         |
|  |   5 6        |
|  |              |
|  |--------      |
|                 |
|-----------------|
"""
    hangman= hangman.replace("1"," ");
    hangman= hangman.replace("2"," ");
    hangman= hangman.replace("3"," ");
    hangman= hangman.replace("4"," ");
    hangman= hangman.replace("5"," ");
    hangman= hangman.replace("6"," ");
    print(hangman);
print_hangman(3);
