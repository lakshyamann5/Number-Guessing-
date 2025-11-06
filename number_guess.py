import random

def play():
    level = input("Choose difficulty (easy/hard): ").strip().lower()
    max_num = 10 if level == "easy" else 20

    number = random.randint(1, max_num)
    attempts = 0
    print(f"Guess the number (1–{max_num})")

    while True:
        try:
            guess = int(input("Your guess: "))
            attempts += 1
            if guess == number:
                print(f"Correct in {attempts} tries!")
                break
            elif guess < number:
                print("Too low.")
            else:
                print("Too high.")
        except ValueError:
            print("Enter a valid number.")

if __name__ == "__main__":
    play()
