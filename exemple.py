print("Hello");

# data structures
name = "Yahya";
char = '9';
a = -10;
seasons = ['automn', 'spring', 'winter', 'summer'];
isYellow = True # False

# operations
if a < 100:
# str is used to tranform integer a in a string
msg = str(a) + " is smaller then 100";
print(msg);

# for loop to iterate through the array
msg = "In a year there are four seasons: ";
for x in seasons:
msg += x + " ";
print(msg);

# incrementation und decrementation
a = 10;
b = 5;

a = a + 3;
print(a); # 13
a += 1;
print(a); # 14
b += 2;
print(b); # 7
b -= 5;
print(b); # 2
b *= 6;
print(b); # 12

for c in name:
print(c);

# task1: is a word a palindrome??
def isPalindrome(word):
str1 = "";
for c in word:
# reverting the word
str1 = str(c) + str1;
return str1 == word;

def isPalindrome2(word):
check = True;
for index in range(0, len(word) // 2):
check = word[index] == word[len(word) - 1 - index];
return check;


words = ["kayak", "yahya", "refer", "rotor", "aymen"];
# task 2: how many of these words are palindrome
for word in words:
check = isPalindrome(word);
print(word + " " + str(check));



