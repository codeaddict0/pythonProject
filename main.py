import documents
def making_list_word(the_list):
    word = ""
    for i in the_list:
        word += i
    return(word)

def lose_point_check(chosen_word,guess):
    b = 0
    for i in chosen_word:
        if i == guess:
            pass
        else:
            b += 1
    if b == len(chosen_word):
        return("lose point")
    else:
        pass
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
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
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']



import random

chosen_word = random.choice(documents.word_list)




list = []
for i in chosen_word:
    list.append("_")

guessed_word = ""
a = 0
lose_point = -1

print(list)
while guessed_word != chosen_word:
    guess = input("Guess a letter: ").lower()
    print(guessed_word)
    if lose_point_check(chosen_word,guess) == "lose point":
        lose_point -= 1

        if lose_point == -7:
            print(stages[lose_point])
            break
        else:
            pass
    else:
        pass
    for position in range(len(chosen_word)):
        i = chosen_word[position]
        if i == guess:
            list[a] = i

        else:
            pass
        a += 1
    print(stages[lose_point])
    guessed_word = making_list_word(list)
    print(guessed_word)


    a = 0
if guessed_word == chosen_word:
    print("You won")
else:
    print("You just lose..")


