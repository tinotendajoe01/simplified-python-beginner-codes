'''define your function for translation
   use a for loop to iterate/read letter by letter for word input in your translator
   define the mode of translation'''

def tran(word):
    translation = ""
    for letter in word:
        if letter.lower() in "aeiou":
            if letter.upper():
                translation = translation + "X"
            else:
                translation = translation + "x"

        else:
            translation = translation+ letter

    return  translation
print(tran(input("enter word: ")))