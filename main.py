from pyfiglet import Figlet
import random
f = Figlet(font='small')
print(f.renderText('GUESS  THE  NUMBER'))
a=random.randint(1,100)
n=1
choice=[]
chances=10
while (n):
    print ()
    n=int(input("Enter the number"))
    if (n==a):
        print()
        print(f.renderText("Congratulations, you win the game"))
        break
    elif (n>a):
        print ()
        print("Your guess is too high")
    else:
        print ()
        print("Your guess is too low")
    choice.append(n)
    print ()
    print ("Your choices are ",", ".join(map(str, choice)))
    chances-=1
    print ()
    print("you have",chances,"chances left")
    if (chances==0):
        print (f.renderText("Sorry, you lose the game"))