def concatenate(**kwargs):
    output = ""
    # iterate over the dictionary
    for item in kwargs.values():
        output += item
    return output

print(concatenate(a="This", sp1=" ", b="is", sp=" ", c="CityU"))
print(concatenate(a="Hello", sp=", ", whatever="do", sp2=" ", next="you", sp3=" ", final="agree?"))
