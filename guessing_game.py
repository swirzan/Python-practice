secret_word = "MSPM"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not (out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Guess the secret word: ")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("Out of guesses, YOU LOSE!")

else:
    print("You win")

# Output
# Guess the secret word: Good
# Guess the secret word: Hello
# Guess the secret word: MSPM
# You win

# Guess the secret word: hello
# Guess the secret word: World
# Guess the secret word: hi
# Out of guesses, YOU LOSE!
