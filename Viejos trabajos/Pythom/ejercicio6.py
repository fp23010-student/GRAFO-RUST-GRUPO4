user_word=input("ingresa una palabra:")
user_word=user_word.upper()
for letter in user_word:
    if letter in "A,E,I,O,U":
        print(letter,"es vocal")