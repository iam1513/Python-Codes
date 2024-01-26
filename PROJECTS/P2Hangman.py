import random

stages = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

logo = '''
_                                             
| |                                            
| |_   _ _ _ _   _ _ _ _ __   _ _ _ _  
| '_ \ / ` | ' \ / ` | ' ` _ \ / ` | ' \ 
| | | | (| | | | | (| | | | | | | (_| | | | |
|| ||\_,|| ||\_, || || ||\_,|| ||
                    __/ |                      
                   |_/       '''

word_list = [
    "virat", "dhoni", "rohit", "sachin", "jadeja", "bumrah", "rishabh", "sehwag",
    "yuvraj", "zaheer", "raina", "chahal", "subhman", "bhuvi", "shami", "ashwin",
    "dhawan", "hardik", "shreyas", "surya", "siraj", "gambhir", "karthik", "kuldeep",
    "rahul", "kapil", "gavaskar", "kumble", "ganguly", "pujara", "axar", "kishan",
    "samson", "yusuf", "irfan", "kaif", "rahane", "shardul", "chahar", "ruturaj",
    "yashashvi", "arshdeep", "umran", "dravid", "lakshman", "krunal", "shreeshant",
    "rayudu", "ishant"
]

chosen_word = random.choice(word_list)
lives = 6

print(logo)

display = []
for _ in range(len(chosen_word)):
  display += "_"
print(display)  

end_of_game = False

while not end_of_game:
  guess = input(" Guess a letter: \n").lower()

  if guess in display:
    print(f" You have already guessed {guess} letter")
  
  for position in range(len(chosen_word)):
    letter = chosen_word[position]
    if letter == guess:
      display[position] = letter

  if guess not in chosen_word:
    print(f" You guessed {guess} , that's not in the word. You lose a life.")
    
    lives -= 1
    if lives == 0:
      end_of_game = True
      print(" You lose: ")

  print(f"{' '.join(display)}")
  
  if "_" not in display:
    end_of_game = True
    print(" You win: ")

  print(stages[lives])
