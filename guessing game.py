name = input("enter your name: ")
age = int(input("enter your age: "))
gender = input("enter your gender (M or F): ")
#gender.islower() or gender.isupper()
print('hello ' + name + " it is nice to know you!")
def define(name , gender):
    if gender == "m":
        print( 'Sir '+ name + (" lets play a guessing game "))
    elif gender == "f":
        print("ma'am  lets play a guesing game")
    else:
        print('please input a valid category to proceed')

define(name, gender)

print('here is the problem, x is an important number found in the range of numbers starting from 34 upto 47 can you help me to guess what the number is? ')
x = 41
guess = ''
guess_count = 0
guess_limit = 3
out_of_guesses = False
while guess != x and not out_of_guesses:
    if guess_count < guess_limit:
        guess = int(input('guess X: '))
        guess_count +=1
        if guess < x:
            print('wrong guess ' + name + ' your guess is too low try higher numbers,you have ' + str(guess_limit - guess_count) + ' guesses left, guess')
        else:
            print('wrong guess ' + name + 'your guess is too high,do try lower numbers, you have ' + str(guess_limit - guess_count) + ' guesses left,')


    else:
        out_of_guesses = True

if out_of_guesses:
    print(name + " you are out of guesses , you lied to me that you will be able to guess the value of X")
else:
    print('thank you ' + name + " seems as if my problem is solved here!")