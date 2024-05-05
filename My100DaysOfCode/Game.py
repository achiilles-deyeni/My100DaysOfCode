#THE HANGMAN GAME

# import random
# word_list = ["cat", "dog", "mouse"]
# chosen_word = random.choice(word_list)

# lives = 6


# display = []
# for _ in range(len(chosen_word)):
#     display += "_"
# print(display)




# end_of_game = False
# while not end_of_game:
#     guess = input("Guess a letter: ").lower()
#     for position in range(len(chosen_word)):
#         letter = chosen_word[position]
#         if letter == guess:
#             display[position] = letter
#     print(display)
#     if guess not in chosen_word:
#         lives -= 1
#         if lives == 0:
#             end_of_game = True
#             print("Number of guesses reached! You lose! ")
#     if "_" not in display:
#         end_of_game = True


#         print("You Win.")




#CEASER CIPHER
# import math
# def area(width, height, cover):
#     area = height * width
#     yes = math.ceil(area/cover)
#     print(f"You'll need {yes} cans of paint")
# width = int(input("Enter the width of the wall: "))
# height = int(input("Enter the height of the wall: "))
# cover = 5


# area(width= width, height =height, cover= cover )

#PRIME NUMBER CHECKER

# def prime(number):
#     if n % 2 == 1:
#         print(f"{n} is a prime number")
#     else:
#         pass
# n = int(input("Enter a number: "))
# prime(number= n)


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
            'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
              'w', 'x', 'y', 'z']
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message: \n").lower()
shift = int(input("Type the shift number: \n"))

def encrypt(plain_text, shift_amount):
    cipher_text =""
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        new_letter = alphabet[new_position]
        cipher_text += new_letter
    print(f"The encoded text is {cipher_text}")

encrypt(plain_text=text, shift_amount=shift)

def decrypt(cipher_text, shift_amount):
    plain_text = ""
    for letter in cipher_text:
        position = alphabet.index(letter)
        new_position = position - shift_amount
        plain_text += alphabet[position]
    print(f"The decoded word is {plain_text}")

decrypt(cipher_text = text, shift_amount = shift)

    



if direction == "encrypt":
    encrypt(plain_text=text, shift_amount=shift)
elif direction == "decode":
    decrypt(cipher_text = text, shift_amount = shift)


