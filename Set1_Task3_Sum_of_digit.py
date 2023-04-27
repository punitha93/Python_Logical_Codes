#Method1
def sum_of_digits(n):
    while n > 9:
        digits_sum = sum(int(digit) for digit in str(n))
        n = digits_sum
    return n

inputdigit = input("Enter a input digit: ")
if inputdigit.isdigit():
    n = int(inputdigit)
    sum_digit = 0
    sum_digit = sum_of_digits(n)
    print("The sum of input digit (method 1): ", sum_digit)
else:
    print("Enter a valid input in non-negative integer format!")



#Method2
# inputdigit = input("Enter the input digit: ")
if inputdigit.isdigit():
    if len(inputdigit) > 1:
        n = int(inputdigit)
        while n > 9:
            j=0
            my_sum = 0
            for i in str(n):
                j+=1
                r = int(i)
                my_sum+=r
            n = my_sum
        print("The sum of input digit (method 2): ", n)
    else:
        print("The sum of input digit (method 2): ",inputdigit)
else:
    print("Please enter a valid input (method 2): ")



# Method3
def Sum_of_Digits(n):
    while n > 9:
        my_list = []
        my_sum = 0
        for digit in str(n):
            my_list.append(int(digit))
        for num in my_list:
            my_sum += num
        n = my_sum
    return n


# inputdigit = input("Enter the input digit: ")
if inputdigit.isdigit():
    n = int(inputdigit)
    Final_Sum = Sum_of_Digits(n)
    print("The sum of input digit (method 3): ", Final_Sum)
else:
    print("Please enter a valid input")