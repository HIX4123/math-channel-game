import random as rand

turnDict = {0 : 'A', 1 : 'B'} # 0 : A, 1 : B
turn = 0

num = 1
nummax = rand.randint(10, 10000)

wrong = 0

print(f"The given number is '{nummax}'. Do not make it!")
while num < nummax :
    command = input(f"{turnDict[turn]}, input s to +1 or m to x2 : ")
    if command == 's' :
        num += 1
        print(f"conducted +1, now num is '{num}'\n")
    elif command == 'm' :
        num *= 2
        print(f"conducted x2, now num is '{num}'\n")
    else :
        print("you gave me something wrong, input s to +1 or m to x2 again\n")
        wrong += 1
        if wrong >= 3 :
            print("Jesus f**k, Quit Turkey your trolling. You loser, B**h")
            quit()
        continue
    wrong = 0
    turn = (turn + 1) % 2
print(f"Game is over for {turnDict[(turn + 1) % 2]} to overflow the given number '{num}'.\nThe winner is {turnDict[turn]}!")