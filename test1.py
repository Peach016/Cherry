file_name = input()
file = open(file_name, "r")
text = file.read()
if "print" in text:
    value = text.split("\"")
    try:
        print(value[1])
    except IndexError:
        print()