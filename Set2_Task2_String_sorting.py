#input_string = input("Enter the input String: ").strip('"').split()             --- User input
# Method 1
def string_sorting(string):
    input_string = string.split()
    new_string = [" "] * len(input_string)
    for word in input_string:
        for i in word:
            if i.isdigit():
                num = int(i) - 1
                if num <= len(input_string):
                    new_string[num] = word
    output_string = (' '.join(new_string))
    return output_string


# Method 2 : Using list comprehension method
def string_sorting2(string):
    input_string = string.split()
    new_string = [" "] * len(input_string)
    for word in input_string:
        num = next((int(c) for c in word if c.isdigit()), None)
        if num is not None and num <= len(input_string):
            new_string[num - 1] = word
    output_string = (' '.join(new_string))
    return output_string


print(f"Method1 - The sorted string \"is2 Thi1s T4est 3a\" --> , + \"{string_sorting(string = 'is2 Thi1s T4est 3a')}\"")
print(f"Method1 - The sorted string \"4of Fo1r pe6ople g3ood th5e the2\" --> , \"{string_sorting(string = '4of Fo1r pe6ople g3ood th5e the2')}\"")
print(f"Method1 - The sorted string \"\" --> , \"{string_sorting(string = '')}\"")


print(f"Method2 - The sorted string \"is2 Thi1s T4est 3a\" --> , \"{string_sorting2(string = 'is2 Thi1s T4est 3a')}\"")
print(f"Method2 - The sorted string \"4of Fo1r pe6ople g3ood th5e the2\" --> , \"{string_sorting2(string = '4of Fo1r pe6ople g3ood th5e the2')}\"")
print(f"Method2 - The sorted string \"\" --> , \"{string_sorting2(string = '')}\"")