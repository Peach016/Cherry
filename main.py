file_name = input()
file = open(file_name, "r")
text = file.readlines()
vars = {
}
for i in text:
    if "consp" in i:
        value = i.split("\"")
        try:
            print(value[1])
        except IndexError:
            newval = value[0].split()
            for l in vars:
                if l == newval[1]:
                    print(vars[l])
           
    if "int" in i:
        value = i.split()
        if value[0] == "int" and value[2] == "=":
            try:
                vars[value[1]] = int(value[3])
            except ValueError:
                print("This is not a integer!")
          
    if "str" in i:
        value = i.split()
        if value[0] == "str" and value[2] == "=" and "\"" in value[3]:
            vars[value[1]] = value[3].split("\"")[1]