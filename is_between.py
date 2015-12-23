def is_between(x, y, z):
    if x <= y and y <= z:
        return True
    else:
        return False

user_x = raw_input()
user_y = raw_input()
user_z = raw_input()

print is_between(user_x, user_y, user_z)
