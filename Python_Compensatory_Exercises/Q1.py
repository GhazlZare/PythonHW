import random

def user_guess():
    while True:
        guess = input("Enter a three-digit number: ")
        if guess.isdigit() and len(guess) == 3:
            return int(guess)
        else:
            print("Error: You must enter exactly three digits.")

def main():

    number = random.randint(100,999)
    print(number)
    attemp = 0
    while attemp < 6 :
        guess = user_guess()
        attemp += 1
        if guess < number :
            print("Too low")
        elif guess > number:
            print("Too high")
        else:
            print(f"Correct! you guess the right number in {attemp} times ")
            break
    if attemp == 6 and guess != number:
        print(f"You've used all your chances. The correct number is {number}.")

if __name__ == "__main__":
    main()