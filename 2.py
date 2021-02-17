# ____________ Write a code to count the number of capital letters in the “drivers_table.csv” file._________

with open('drivers_table.csv') as file:
    count_of_capital_letters = sum(character.isupper() for character in set(file.read()))
    print("The number of capital letters in the file is:",count_of_capital_letters)
