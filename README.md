# PYTHON-  

# TASK 1 --- NUMBER GUESSING GAME ----
Create a guessing game where the player must choose a range.
Assume that the user choose a range, say, from A to B, where A and B are integers.
The user must estimate the given random integer in the fewest possible guesses once the system selects it.


# TASK 2 --- PASSWORD GENERATOR USING PYTHON  ---- 
A powerful and random password generator is a helpful tool that produces passwords for users. The goal of this project is to use Python to construct an application that generates passwords and lets users set the password's difficulty and length.
INPUT: Ask the user to indicate how long they would like their password to be.
Create Password: To create a password of the required length, mix and match random characters.
Show the Password : - The generated password will print on the screen.


# TASK 3 --- WORD COUNTER USING PYTHON  ---- 
 A word counter in Python is a program that takes a text input, counts the frequency of each word in the text, and then displays the count for each word. Here's a simple explanation of how to implement a word counter in Python.
 **Explanation:**

1. We define a function called word_counter that takes a string text as input.
2. Inside the function, we initialize an empty dictionary called word_count to store the counts of each word.
3. We split the input text into individual words using the split() method, which returns a list of words.
4. We iterate through each word in the list and perform some preprocessing:
5. We convert each word to lowercase using the lower() method to ensure case-insensitive counting.
6. We use the strip() method to remove any leading or trailing punctuation marks.
7. We check if the word is already present in the word_count dictionary. If it is, we increment its count. If not, we add it to the dictionary with a count of 1.
   Finally, we return the word_count dictionary containing the counts of each word.
8. We provide an example text and call the word_counter function with this text. The result is stored in the word_counts variable.
   We iterate through the word_counts dictionary and print each word along with its count.
   
# TASK 4 --- ROCK PAPER SICESSORS ----
**Rock, Paper, Scissors is a simple hand game played between two people. The game has three possible outcomes: a player can win, lose, or tie with their opponent.**

Here's how the game is typically played:

# Setup: Two players (usually represented by hand gestures) simultaneously choose one of three options: rock, paper, or scissors.

$ Rules:

- Rock beats scissors (rock crushes scissors)
- Scissors beats paper (scissors cut paper)
- Paper beats rock (paper covers rock)
- Outcome:

- If both players choose the same option, the game is a tie.
- Otherwise, the winner is determined by the rules mentioned above.
- Repeat: Players can play multiple rounds to determine an overall winner.

**Implementing Rock, Paper, Scissors in Python involves creating a program that allows two players to input their choices and then determines the winner based on the rules mentioned above. Here's a basic example of how you can implement it:** 

# Explanation:

-> The determine_winner function takes the choices of both players and returns the result based on the rules of Rock, Paper, Scissors.
-> The main function allows two players to input their choices, generates a random choice for the computer (player 2), determines the winner, and asks if the players want to play again.
-> The program uses a while loop to continue playing rounds until one of the players decides not to play anymore.
-> The if __name__ == "__main__": block ensures that the main function is executed when the script is run directly, but not when it's imported as a module into another script.







