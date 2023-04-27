numberlist = []
n = int(input("Enter Number of Elements in List: "))    
for i in range(n):    
    number = int(input("Enter number: "))
    numberlist.append(number)
print("Your input list of Numbers: ", numberlist)
finalnumlist = list(set(numberlist))
sorted_numberlist = sorted(finalnumlist,reverse=True)  
print("The second largest number in the given list is : ", sorted_numberlist[1])

