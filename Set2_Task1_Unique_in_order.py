#Method 1
def unique_in_order(sequence):
    new_sequence = []
    for i in sequence:
        if len(new_sequence) == 0 or i != new_sequence[-1] and i != ",":
            new_sequence.append(i)
    return new_sequence


print(f"The unique_in_order ('AAAABBBCCDAABBB') == {unique_in_order(sequence = 'AAAABBBCCDAABBB')}")
print(f"The unique_in_order ('ABBCcAD') == {unique_in_order(sequence = 'ABBCcAD')}")
print(f"The unique_in_order ([1,2,2,3,3]) == {unique_in_order(sequence = [1,2,2,3,3])}")



#Method 2 - User Input
def unique_in_order(sequence):
    new_sequence = []
    contains_digit = any(char.isdigit() for char in sequence)
    for i in sequence:
        if len(new_sequence) == 0 or i != new_sequence[-1] and i != ",":
            new_sequence.append(i)
    if contains_digit:
        new_sequence = list(map(int, new_sequence))
    return new_sequence


sequence = input("Enter the sequence: ")
print(f"The unique_in_order ({sequence}) == {unique_in_order(sequence)}")