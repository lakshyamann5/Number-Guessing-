import random

def play():
    number = random.randint(1, 10)
    attempts = 0
    print("Guess the number (1–10)")

    while True:
        try:
            guess = int(input("Your guess: "))
            attempts += 1
            if guess == number:
                print(f"You got it in {attempts} tries!")
                break
            elif guess < number:
                print("Too low.")
            else:
                print("Too high.")
        except ValueError:
            print("Enter a valid number.")

if __name__ == "__main__":
    play()
