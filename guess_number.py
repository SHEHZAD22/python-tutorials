#Guessing the number
#SHEHZAD
n=18
print("You have given no. of guess is 5. if you guess the exact number then you will win this game.\n\"You will get the shoutout by codewithHarry sir.\"\nSo, let's started.....")
a = 1
while(a<=5):
    g=int(input("\nGuess the number: "))
    if g>18 :
        print("The number guessed by you is greater. Please input less and guess the right number")
    elif g<18:
        print("The number guessed by you is less. Please input greater and Guess the right number")
    else:
        print("Congratulations! \"You are winner\"")
        print("You won this game with",a,"guess")

        break
    print("You have left with",5-a,"guess")
    a = a + 1
if a>5:
    print("\nNo. of guesses finished\nBetter luck next time...")