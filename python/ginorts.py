def string_manner(char):
    print(char)
    if char.islower():
        return (1, char)
    elif char.isupper():
        return (2, char)
    elif char.isdigit() and int(char) % 2 != 0:
        return (3, char)
    elif char.isdigit() and int(char) % 2 == 0:
        return (4, char)
    else:
        return (5, char)


input_string = input()

sorted_string = ''.join(sorted(input_string, key=string_manner))
print(sorted_string)

