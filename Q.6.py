import pygame
import time
import random

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Typing Speed Test")

# Set up fonts and colors
font = pygame.font.SysFont("Arial", 30)
big_font = pygame.font.SysFont("Arial", 40)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# List of sentences to type
sentences = [
    "The quick brown fox jumps over the lazy dog.",
    "Python is a powerful programming language.",
    "Pygame makes it easy to build games and graphical applications.",
    "Good programmers write clean, readable code.",
    "Practice makes perfect, especially with typing."
]

# Function to calculate typing speed
def calculate_wpm(start_time, typed_text, sentence):
    elapsed_time = time.time() - start_time  # Time taken in seconds
    words = len(typed_text.split())
    wpm = (words / elapsed_time) * 60  # Words per minute
    return wpm

# Main game function
def typing_test():
    # Choose a random sentence
    sentence = random.choice(sentences)

    # Render sentence to display
    sentence_text = font.render(sentence, True, BLACK)
    input_text = ""

    # Game loop
    running = True
    start_time = None
    clock = pygame.time.Clock()

    while running:
        screen.fill(WHITE)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                else:
                    input_text += event.unicode

        # Start the timer once the user starts typing
        if start_time is None and input_text:
            start_time = time.time()

        # Display the sentence and user input
        screen.blit(sentence_text, (50, 100))
        typed_text = font.render(input_text, True, BLACK)
        screen.blit(typed_text, (50, 200))

        # If user typed the sentence correctly, stop the game
        if input_text == sentence:
            wpm = calculate_wpm(start_time, input_text, sentence)
            result_text = f"Congratulations! Your typing speed: {wpm:.2f} WPM"
            result_surface = big_font.render(result_text, True, BLACK)
            screen.blit(result_surface, (50, 300))
            pygame.display.update()
            pygame.time.wait(3000)  # Wait for 3 seconds before closing
            running = False

        # Update the display
        pygame.display.update()

        # Limit the frame rate
        clock.tick(60)

# Run the typing test
typing_test()

# Quit pygame
pygame.quit()

