first_name = "Reiko"
last_name = "Matsuki"


def password_generator(first_name, last_name):
    first = len(first_name)
    last = len(last_name)
    password = first_name[first-3:] + last_name[last-3:]
    return password


temp_password = password_generator(first_name, last_name)

print(temp_password)
