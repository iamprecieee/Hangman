import random
from words import words
from ascii import header, hangman

print(f"WELCOME ANON TO THE ONE AND ONLY:\n{header}\n\nJUST ONE RULE!\nGUESS WRONG AND LOSE A LIFE!")
contract = input("\nDO YOU ACCEPT THESE TERMS?\nYes or No\n").lower()
exclam = ["GOOD JOB!", "EXCELLENT!", "GREAT!", "INTERESTING!", "AWESOME!", "NICE!"]

#create a failsafe in case user gives a wrong input
while contract not in ["yes", "no"]:
  contract = input("\nDO YOU ACCEPT THIS?\nYes or No\n").lower()

if contract == "yes":
  print(f"\nBEWARE, THE HANGMAN'S NOOSE!\n{hangman[6]}")
  difficulty = input("\nPLEASE CHOOSE YOUR PREFERRED DIFFICULTY LEVEL:\nEasy or Intermediate or Hard\n").lower()
  while difficulty not in words:
    difficulty = input("\nPLEASE CHOOSE YOUR PREFERRED DIFFICULTY LEVEL:\nEasy or Intermediate or Hard\n").lower

  #randomly pick any word from the list of possible words depending on difficulty level
  random_word = random.choice(words[difficulty])

  #create a blank list to match the random word letter for letter, such that the letters are replaced by "_"
  blank = ["_" for _ in random_word]

  #set a looping condition using while and declare total number of lives
  status = False
  lives = 6

  print(f"\nA word has been picked from the cookie jar.\n{' '.join(blank)}")

  while not status:
    
    #ask the player to guess a letter from the random word
    guess = input("\nGuess a letter from this word:\n").lower()
    if guess in blank:
        print(f"\nYOU HAVE ALREADY GUESSED {guess}!")

    #compare the random word with a guess and fill in the blank if it matches
    for x, letter in enumerate(random_word):
            if letter.lower() == guess:
                blank[x] = letter

    if guess in random_word.lower() and len(guess) == 1:
      print(f"\n{random.choice(exclam)}")
    print(f"\n{' '.join(blank)}")

    #check nuumber of lives left and end game when there are no more lives
    if guess not in random_word.lower():
      print(f"\nTHE LETTER {guess} IS NOT IN THIS WORD. YOU LOSE A LIFE!")
      lives -=1
      if lives == 0:
        status = True
        print("\nYOU LOSE!")

      elif lives == 1:
        print("\nLAST CHANCE!\n")
    #display hangman status
    print(hangman[lives])  

    #check if all letters have been field and end game if satisfied
    if "_" not in blank:
      status = True
      print("\nYOU WIN!")
else:
  print("\nYOU CANNOT GAIN ACCESS TO THIS GAME THEN, GOODBYE!")