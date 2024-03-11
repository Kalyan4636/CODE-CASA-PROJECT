import random

def get_range():
    """Get the range from the user as a tuple of integers."""
    while True:
        try:
            low, high = map(int, input("Enter a range (low high): ").split())
            if low < high:
                return (low, high)
            else:
                print("The lower bound must be less than the upper bound.")
        except ValueError:
            print("Invalid input. Please enter two integers separated by a space.")

def guess_number(low, high):
    """Choose a random number in the given range and let the user guess it."""
    target = random.randint(low, high)
    num_guesses = 0
    while True:
        guess = int(input("Guess a number in the range [%d, %d]: " % (low, high)))
        num_guesses += 1
        if guess == target:
            print("Congratulations! You guessed the number in %d guesses." % num_guesses)
            break
        elif guess < target:
            print("Too low. Try again.")
        else:
            print("Too high. Try again.")

if __name__ == "__main__":
    low, high = get_range()
    guess_number(low, high)
