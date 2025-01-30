import random

# List of words to choose from
words = ["python", "java", "swift", "ruby", "javascript", "html", "css", "django"]

# Pick a random word from the list
word = random.choice(words)

# Shuffle the letters of the word to create an anagram
anagram = ''.join(random.sample(word, len(word)))

# Prompt the user to guess the original word
print("Welcome to the Anagram Game!")
print("Here's your anagram:", anagram)

# Allow the user to guess
guess = input("Guess the word: ").lower()

# Check if the guess is correct
if guess == word:
    print("Correct! Well done.")
else:
    print(f"Oops! The correct word was: {word}")
