def generate_acronym(phrase):
    # Split the phrase into words and take the first letter of each word
    words = phrase.split()
    acronym = ''.join(word[0].upper() for word in words)  # Convert to uppercase
    return acronym

# Get user input
user_input = input("Enter a phrase to generate an acronym: ")

# Generate and display the acronym
acronym = generate_acronym(user_input)
print(f"The acronym for '{user_input}' is: {acronym}")
