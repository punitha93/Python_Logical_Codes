def is_isogram(input_string):    
    new_input = input_string.lower()   
    is_isogram = len(set(new_input)) == len(input_string)
    print(f"is_isogram ({input_string}) == {is_isogram}")


input_string = input("Enter the word to check whether it is an isogram: ")
is_isogram(input_string)

# __sample inputs
# Dermatoglyphics
# aba
# moOse