turnDict = {0 : 'A', 1 : 'B'} # 0 : A, 1 : B
turn = 0

num = 1
nummax = 31

while num < nummax :
    command = input(f"{turnDict[turn]}, input s to +1 or m to x2 : ")
    if command == 's' :
        num += 1
        print(f"conducted +1, now num is '{num}'")
    elif command == 'm' :
        num *= 2
        print(f"conducted x2, now num is '{num}'")