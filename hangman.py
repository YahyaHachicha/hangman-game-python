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

# print hangman function
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
    if(errors > 6):
        print('Game Over!');
    elif (errors < 6):
        for i in range(errors + 1, 7):
            hangman= hangman.replace(str(i), " ");
    hangman = hangman.replace("1", "O");
    hangman = hangman.replace("2", "/");
    hangman = hangman.replace("3", "|");
    hangman = hangman.replace("4", "\\");
    hangman = hangman.replace("5", "/");
    hangman = hangman.replace("6", "\\");
    print(hangman);
# end of function

print_hangman(4);
