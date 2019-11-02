# Biggie Size - Given a list, write a function that changes all positive numbers in the list
#  to "big".Example: biggie_size([-1, 3, 5, -5]) returns that same list, but whose values
#  are now [-1, "big", "big", -5]
def biggie_size(my_list):
    for i in range(len(my_list)-1):
        if my_list[i]>0:
            my_list[i] = 'big'
    return my_list
print(biggie_size([-1,3,5,-5]))

# Count Positives - Given a list of numbers, create a function to replace the last value with the
#  number of positive values. (Note that zero is not considered to be a positive number).
# Example: count_positives([-1,1,1,1]) changes the original list to [-1,1,1,3] and returns it
# Example: count_positives([1,6,-4,-2,-7,-2]) changes the list to [1,6,-4,-2,-7,2] and returns
#  it

def count_positives(my_list):
    count =0
    for i in range(len(my_list)):
        if my_list[i]>0:
            count += 1
        my_list[-1] = count
    return my_list

print(count_positives([1,6,-4,-2,-7,-2]))

# Sum Total - Create a function that takes a list and returns the sum of all the values in the 
# array. Example: sum_total([1,2,3,4]) should return 10
# Example: sum_total([6,3,-2]) should return 7

def sum_total(list):
    sum =0
    for i in range(0,len(list)) :
        sum += list[i]
    return sum
print(sum_total([1,2,3,4]))
print(sum_total([6,3,-2]))

# Average - Create a function that takes a list and returns the average of all the values.
# Example: average([1,2,3,4]) should return 2.5

def average(list):
    sum =0
    for i in range(len(list)):
        sum += list[i]
    return sum/len(list)

print(average([1,2,3,4]))


# Length - Create a function that takes a list and returns the length of the list.
# Example: length([37,2,1,-9]) should return 4
# Example: length([]) should return 0

def length(list):
    count =0
    for i in list:
        count +=1
    return count
print(length([1,2,3,4]))

# Minimum - Create a function that takes a list of numbers and returns the minimum value in 
# the list. If the list is empty, have the function return False.
# Example: minimum([37,2,1,-9]) should return -9
# Example: minimum([]) should return False
def minimum(list):
    if len(list)==0:
        return  False
    min = list[0]
    for num in list:
        if  num<min:
            min = num
    return min
print(minimum([37,2,1,-9]))
print(minimum([]))

# Maximum - Create a function that takes a list and returns the maximum value in the array.
#  If the list is empty, have the function return False.
# Example: maximum([37,2,1,-9]) should return 37
# Example: maximum([]) should return False
def maximum(list):
    if len(list)==0:
        return False
    max = list[0]
    for num in list:
        if num>max:
            max = num
    return max
print(maximum([37,2,1,-9]))
print(maximum([]))

# Ultimate Analysis - Create a function that takes a list and returns a dictionary that has the 
# sumTotal, average, minimum, maximum and length of the list.
# Example: ultimate_analysis([37,2,1,-9]) should return {'sumTotal': 31, 'average': 7.75, 
# 'minimum': -9, 'maximum': 37, 'length': 4 }
def ultimate_analysis(list):
    sum = 0
    min = list[0]
    max = list[1]
    for num in list:
        sum += num
        if num>max:
            max = num
        if num<min:
            min = num
    avg = sum/len(list)
    result ={'sum':sum,'avg':avg,'min':min,'max':max,'length':len(list)}
    return result

print(ultimate_analysis([37,2,1,-9]))

# Reverse List - Create a function that takes a list and return that list with values reversed.
#  Do this without creating a second list. (This challenge is known to appear during basic
#   technical interviews.)
# Example: reverse_list([37,2,1,-9]) should return [-9,1,2,37]
def reverse_list(list):
    # for i in range(0,len(list)-1):
    #     if list[i]<len(list)-1:
    #         temp =list[i]
    #         list[i] = list[len(list)-1-i]
    #         list[len(list)-1-i] = temp
    # return list

    left =0
    right = len(list)-1
    while left<right:
        temp = list[left]
        list[left]= list[right]
        list[right] = temp
        left +=1
        right -= 1
    return list

print(reverse_list([37,1,2,-9]))
print(reverse_list([1,2,3,4,5,6,7]))

def beCheerful(name='pramila', repeat=2):		# set defaults when declaring the parameters
	print(f"good morning {name}\n" * repeat)
beCheerful()