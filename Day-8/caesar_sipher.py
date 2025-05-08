alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def caesar(word,shift,choice,ans):
    if choice == "decode":
        shift = shift * -1
    if shift == 0:
        print(word)
    else:
        for char in word:
            if char not in alphabets:
                ans += char
            else:
                new_index = alphabets.index(char) + shift
                new_index %= 26
                ans += alphabets[new_index]
        print(ans)
    

repeat = True
while repeat:
    choice = str(input("What do you want to do ? \"Encode or Decode\": ")).lower()
    word = str(input("Enter the message ")).lower()
    shift = int(input("Enter the shift number: "))
    ans = ""
    caesar(word,shift,choice,ans)
    r = str(input("Do you want to continue ? ")).lower()
    if r != 'y':
        break




