def right_justify(s):
    gap = 70 - len(s)
    space = ' ' * gap

    print(space + s)

right_justify('monty')