import random

word_list = ["aardvark", "baboon", "camel"]

word_generated = random.choice(word_list)
list_generated = []
for char in word_generated:
    list_generated.append(char)

ans_list = ["_"] * (len(word_generated))

tries = 6

while tries >0:
    print(f"Available Tries: {tries}")
    guess = str(input("Enter a letter: ")).lower()


    if guess in list_generated:
        for char in range(len(list_generated)):
            if guess == list_generated[char]:
                ans_list[char] = guess
                list_generated[char] = "_"
                break
    else:
        tries -= 1
    if "_" not in ans_list :
        print("YOU WON!")
        break


    print(ans_list)

else:
    print("No More Tries! YOU LOST")

