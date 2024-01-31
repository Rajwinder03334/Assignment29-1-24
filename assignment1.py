cabinn = input("Enter cabin class in capital letter ")

if cabinn == 'LUX':
    print("Upper-deck cabin with a balcony.")
elif cabinn == 'A':
    print("Above the car deck, equipped with a window.")
elif cabinn == 'B':
    print("Windowless cabin above the car deck.")
elif cabinn == 'C':
    print("Windowless cabin below the car deck.")
else:
    print("Invalid class.")