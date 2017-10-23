break_loop = False
while not break_loop:
    x = int(raw_input("Enter the value for x:"))
    y = int(raw_input("Enter the value for y:"))

    if x % y == 3:
        print('ost. je 3')
    elif x % y == 0:
        break_loop = True