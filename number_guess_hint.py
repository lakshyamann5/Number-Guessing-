
import random

def play_with_hints():
    number = random.randint(1, 50)
    attempts = 0
    print("Guess the number (1–50). You'll get higher/lower hints.")

    while True:
        try:
            guess = int(input("Your guess: "))
            attempts += 1
            if guess == number:
                print(f"Nice! You got it in {attempts} attempts.")
                break
            print("Higher!" if guess < number else "Lower!")
        except ValueError:
            print("Please enter a valid whole number.")

if __name__ == "__main__":
    play_with_hints()