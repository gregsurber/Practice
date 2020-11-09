letters = ["City University"]
output_list = []

for letter in letters:
    if letter.isupper() == True:
        output_list.append(letter)


print(output_list)


print('this is CityU'.upper().lower())