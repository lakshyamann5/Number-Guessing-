mport random

def play_with_hints():
    number = random.randint(1, 50)
    attempts = 0
    max_attempts = 7
    print("Guess the number between 1 and 50. You have 7 tries!")

    while attempts < max_attempts:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess == number:
                print(f"  You guessed correctly in {attempts} tries!")
                break
            elif guess < number:
                print("Hint: the number is higher.")
            else:
                print("Hint: the number is lower.")
        except ValueError:
            print("Please enter a valid number.")

    else:
        print(f" Out of tries! The correct number was {number}.")

    # Ask to play again
    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again == "yes":
        play_with_hints()

if __name__ == "__main__":
    play_with_hints()
