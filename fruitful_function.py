def compare(x, y):
    if x > y:
        return 1
    elif x == y:
        return 0
    else:
        return -1


user_x = raw_input('Bitte eine Zahl eingeben: ')
user_y = raw_input('Bitte eine weitere Zahl eingeben: ')
print compare(user_x, user_y)
