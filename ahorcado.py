import random

# This is a tuple with a bunch of triple quotes strings that will display in order
HANGMAN = (
"""
 ------
|     |
|
|
|
|
|
|
|
----------
"""
    ,
"""
 ------
|     |
|     0
|
|
|
|
|
|
----------
"""
   ,
"""
 ------
|     |
|     0
|     +
|
|
|
|
|
----------
"""
    ,
"""
 ------
|     |
|     0
|    -+
|
|
|
|
|
----------
"""
    ,
"""
 ------
|     |
|     0
|    -+-
|
|
|
|
|
----------
"""
    ,
"""
 ------
|     |
|     0
|   /-+-
|
|
|
|
|
----------
"""
    ,
"""
 ------
|     |
|     0
|   /-+-/
|
|
|
|
|
----------
"""
    ,
"""
 ------
|     |
|     0
|   /-+-/
|     |
|
|
|
|
----------
"""
    ,
"""
 ------
|     |
|     0
|   /-+-/
|     |
|     |
|
|
|
----------
"""
    ,
"""
 ------
|     |
|     0
|   /-+-/
|     |
|     |
|    |
|    |
|
----------
"""
    ,
"""
 ------
|     |
|     0
|   /-+-/
|     |
|     |
|    | |
|    | |
|
----------
"""
)

# This is because the first pic is already there at the start of the program
MAX_WRONG = len(HANGMAN) - 1

try:
    with open("ahorcado.txt", "r") as palabras:
        word = random.choice(palabras.readlines()).upper()[:-1]
except FileNotFoundError as fnfe:
    print("El archivo 'ahorcado.txt' no se encuentra en el mismo directorio que este script")
    exit(1)

# one dash for each letter in word to be guessed except the last character (newline)
so_far = "_" * len(word)

wrong = 0  # number of wrong guesses player has already made
used = []  # letters already guessed
print("Bienvenido al juego del Ahorcado. Buena suerte!")

# the program will continue while there are still guesses left and the player didn't guess the word
while wrong < MAX_WRONG and so_far != word:
    print(HANGMAN[wrong])
    print("\nLetras usadas hasta ahora:\n", used)
    print("\nHasta el momento, la palabra es:\n", so_far)

    guess = input("\n\nIngrese una letra: ")
    # this will convert the guess to all uppercase becasue that's how it it is in the tuple
    guess = guess.upper()

    # if they guess the same letter twice, this will print
    while guess in used:
        print("La letra {} ya fue ingresada anteriormente".format(guess))
        guess = input("Ingrese una letra: ")
        guess = guess.upper()
    # whatever's guessed, gets added to the used list 
    used.append(guess)
    # if the guess is correct, it will print the following
    if guess in word:
        print("\nSi! La letra ", guess, " se encuentra en la palabra!")
        # create new so_far to include guess
        # this means it will replace the blank with the letter
        new = ""
        for i in range(len(word)):
            if guess == word[i]:
                new += guess
            else:
                new += so_far[i]
        # this redefines so_far to include the letter guessed correctly
        so_far = new
    # if the guess is wrong, then it will print the following
    else:
        print("\nNo, la letra ", guess, "no se encuentra en la palabra.")
        # this adds a wrong try
        wrong += 1

# if the number of tries reaches the limit, meaning the hangman is hanged, it prints the following
if wrong == MAX_WRONG:
    print(HANGMAN[wrong])
    print("\nAhorcado!")
# otherwise, the person got the word right
else:
    print("\n\nGanaste!")
print("\nLa palabra era: ", word)
input("\n\nPresione la tecla 'enter' para salir.")

