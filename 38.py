secret_word = "giraffe"

guess = " "

while guess != secret_word:
    guess = input("Enter guess: ")
    if guess == secret_word:
        print("You Win!")
    else:
        print("Try again!")
