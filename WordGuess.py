# Online Python-3 Compiler (Interpreter)
import random

# List of words with corresponding hints for the game
words_with_hints = [
    ("python", "A popular programming language."),
    ("hangman", "A classic word-guessing game."),
    ("challenge", "A task that tests your skills or knowledge."),
    ("programming", "The process of writing computer software."),
    ("developer", "A person who writes and maintains code."),
    ("algorithm", "A step-by-step procedure for solving a problem."),
    ("variable", "A storage location in programming with a name."),
    ("internet", "A global network connecting millions of computers."),
    ("function", "A block of code that performs a specific task."),
    ("hardware", "The physical parts of a computer system."),
    ("software", "Programs and other operating information used by a computer."),
    ("database", "An organized collection of structured information or data."),
    ("encryption", "The process of converting information into code to prevent unauthorized access."),
    ("javascript", "A programming language commonly used to create interactive effects within web browsers."),
    ("machine", "A device that performs a specific task, often using mechanical or electrical power."),
    ("binary", "A system of numbers using only two digits: 0 and 1."),
    ("compiler", "A program that converts code into machine language."),
    ("network", "A group of interconnected computers and devices."),
    ("syntax", "The set of rules that defines the combinations of symbols considered valid in a programming language."),
    ("recursion", "A programming technique where a function calls itself."),
    ("iteration", "The repetition of a process or set of instructions in programming."),
    ("pixel", "The smallest unit of a digital image."),
    ("cybersecurity", "The practice of protecting systems, networks, and programs from digital attacks."),
    ("data", "Information, especially facts or numbers, collected for analysis."),
    ("compiler", "A program that translates source code into executable code."),
    ("firewall", "A network security system that monitors and controls incoming and outgoing network traffic."),
    ("cache", "A hardware or software component that stores data to serve future requests faster."),
    ("bootstrap", "A popular front-end framework for developing responsive web designs."),
    ("debugging", "The process of identifying and removing errors from computer hardware or software."),
    ("iteration", "The repetition of a process in computer programming."),
    ("boolean", "A data type with two possible values: true or false."),
    ("pixel", "The smallest element of an image displayed on a screen."),
    ("cloud", "A network of remote servers that store, manage, and process data."),
    ("authentication", "The process of verifying the identity of a user or process."),
    ("bit", "The smallest unit of data in computing, representing a single binary value."),
    ("byte", "A group of eight bits, commonly used to represent a character."),
    ("router", "A device that forwards data packets between computer networks."),
    ("loop", "A programming construct that repeats a set of instructions."),
    ("array", "A collection of elements, each identified by an index or key."),
    ("git", "A version control system for tracking changes in code."),
    ("constructor", "A special function in object-oriented programming used to initialize objects."),
    ("inheritance", "A mechanism in object-oriented programming where a class can inherit properties and methods from another class.")
]

# Function to display the current state of the word
def display_word(word, guessed_letters):
    return " ".join(letter if letter in guessed_letters else "_" for letter in word)

# Function to play Hangman
def play_hangman():
    # Select a random word and its hint from the list
    word, hint = random.choice(words_with_hints)
    guessed_letters = set()
    incorrect_guesses = 0
    max_incorrect_guesses = 9  # You can change this number to set the limit on incorrect guesses

    print("Welcome to Hangman!")
    print(f"Hint: {hint}")  # Display the hint

    while incorrect_guesses < max_incorrect_guesses:
        # Display the current state of the word
        current_display = display_word(word, guessed_letters)
        print(f"Word: {current_display}")
        print(f"Incorrect guesses left: {max_incorrect_guesses - incorrect_guesses}")

        # Get a guess from the player
        guess = input("Guess a letter: ").lower()

        # Check if the input is valid
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        # Check if the letter has already been guessed
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        # Add the letter to guessed_letters
        guessed_letters.add(guess)

        # Check if the guessed letter is in the word
        if guess in word:
            print("Good guess!")
        else:
            print("Incorrect guess.")
            incorrect_guesses += 1

        # Check if the player has won
        if all(letter in guessed_letters for letter in word):
            print(f"Congratulations! You guessed the word: {word}")
            break
    else:
        print(f"Sorry, you've run out of guesses. The word was: {word}")

# Start the game
play_hangman()
