def queue_time(input_list, no_of_tills):
    tills = [0] * no_of_tills
    for time in input_list:        
            tills.sort()
            tills[0] += time

    return max(tills)


#This lines in command can be used to get user input and to print the corresponding output
# input_list, no_of_tills = (list(map(int,input("Enter the customers' checkout time in list format:").split()))), int(input("Enter the no of tills: "))
# total_time = queue_time(input_list, no_of_tills)
# print(f"The total time required for the queue({input_list} with {no_of_tills} till(s)) to checkout: ", total_time)
total_time1 = queue_time([5,3,4], 1)
total_time2 = queue_time([10,2,3,3], 2)
total_time3 = queue_time([2,3,10], 2)
print("The total time required for the queue([5,3,4] with 1 till(s)) to checkout: ", total_time1)
print("The total time required for the queue(([10,2,3,3] with 2 till(s)) to checkout: ", total_time2)
print("The total time required for the queue([2,3,10], with 2 till(s)) to checkout: ", total_time3)