# Prompt the user to enter a word and assign to variable
userWord = input("Please enter a word: ")
# Make the word uppercase
userWord = userWord.upper()
print(userWord)

# Loop over the letters in the word
# Do not print vowels
# Print consonants
for letter in userWord:
    vowels = ['A','E','I','O','U']
    if letter in vowels:
        continue
    print(letter)