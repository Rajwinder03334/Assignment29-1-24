r= input("Enter gender only M or F: ")
blood = float(input("blood value: "))

if r == 'M':
    if 134 <= blood <= 167:
        print("normal level of blood (males).")
    elif blood < 134:
        print("low level of blood (males).")
    else:
        print("high level of blood (males).")
elif r == 'F':
    if 117 <= blood <= 155:
        print("normal level of blood  (females)")
    elif blood < 117:
        print("low level of blood (females)")
    else:
        print("high level of blood (females)")
else:
    print("please provide correct gender")