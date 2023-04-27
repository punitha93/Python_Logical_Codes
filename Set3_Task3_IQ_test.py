def iq_test(input_list):
    even = []
    odd = []
    new_list = list(map(int, input_list.strip("").split()))
    for i in new_list:
        if i%2 ==0:
            even.append(i)
        else:
            odd.append(i)
    if len(even) == 1:
        index = new_list.index(even[0])
        return index+1
    if len(odd) == 1:
        index = new_list.index(odd[0])
        return index+1


#This lines in command can be used to get user input and to print the corresponding output
# input_list = input("Enter the numbers with space: ")
# number_position = iq_test(input_list)
# print(f'The position of a number that is different from others in the given numbers ("{input_list}") => {number_position}')

output1 = iq_test("2 4 7 8 10")
output2 = iq_test("1 2 1 1")
output3 = iq_test("1 2 2")
output4 = iq_test("8 30 2 1")
print('iq_test("2 4 7 8 10") => ', output1)
print('iq_test("1 2 1 1") => ', output2)
print('iq_test("1 2 2") => ', output3)
print('iq_test("8 30 2 1") => ', output4)