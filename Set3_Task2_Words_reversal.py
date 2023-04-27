def reverse_string_words(input_string):
    split_string = input_string.split()
    new_string = []
    for word in split_string:
        new_string.append(word[::-1])
        output_string = ' '.join(new_string)
    print(f'"{input_string}" ==> "{output_string}"')

input_string = input("Enter your string to reverse its word: ")
reverse_string_words(input_string)

# Sample inputs____
# This is an example!
# double spaces