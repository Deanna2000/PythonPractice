# Prompt the user to enter a word and assign to variable
userWord = input("Please enter a word: ")
# Make the word uppercase
userWord = userWord.upper()
nonvowels = []
print(userWord)

# Loop over the letters in the word
# Do not print vowels
# Add consonants to a list
# Print list of consonants
for letter in userWord:
    vowels = ['A','E','I','O','U']
    if letter in vowels:
        continue
    nonvowels.append(letter)
print(' '.join(nonvowels))