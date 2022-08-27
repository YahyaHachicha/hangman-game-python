from random import randint;

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

# check if the character exists in the word
def check_if_error(char, word):
    return char in word
# end of function

# print secret word
def get_secret(word, c, s): 
    secret = s;
    for i in range(0, len(word)):
        if(word[i] == c):
            secret = secret[0:i*2] + c + secret[i*2+1:]
    return secret;
# end of function


words = ['automn', 'spring', 'winter', 'summer'];
index = randint(0, len(words)-1);
word = words[index];
count_errors = 0;
game_over = False;

secret = "";
for _ in range(0, len(word)):
    secret += "_ ";

while(not game_over):
    char = input("Insert your character:");
    check = check_if_error(char, word)
    if(check):
        secret = get_secret(word, char, secret);
        if "_" not in secret:
            game_over = True;
            print("Congratulations. You found the secret word!")
        else:
            print(secret);
    else: 
        count_errors += 1;
        print_hangman(count_errors);
        if(count_errors >= 6):
            print("Game Over. You lost!");
            game_over = True
