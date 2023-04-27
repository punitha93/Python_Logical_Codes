#Method 1 : Using Regular Expression
import re
inputstring = input("Enter your input string: ")
outputstring = re.split('_|-', inputstring)
print("String split using method 1 : ", outputstring)

#Method 2
intermediate_string = inputstring.split("_")
outstring=[]
for word in intermediate_string:
    if "-" in inputstring:        
        newword = word.split("-")
        outstring+=newword
        word =""
    else:
        outstring.append(word)
print("String split using method 2 : ", outstring)