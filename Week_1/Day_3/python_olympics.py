# Given an array and x -> paramert list
# return that same array 
# with each value multiplied by x

def arr_mult(arr,x):
    for i in range(len(arr)):
        arr[i]*=x    # arr[i] = arr[i]*x
    return arr

# print(arr_mult([1,2,3],2))


###############################################################################################
# Given an array and y
# return a count of all 
# values greater than y

def greater_y(arr,y):
    sum=0
    for i in range(len(arr)):
         #value greater than y
        if arr[i]>y:
            sum=sum+1 #sum+=1 => Ok,  sum++ => NOT OK
    return sum

# print(greater_y([3,7,4,0],5))



###############################################################################################
# Given an array of strings, return the same array with each string being replaced by it’s length.
# ex.
# [“Hello”, “World”] => [5, 5]

def replace_word_with_length(arr):
    for i in range(len(arr)):
        arr[i] = len(arr[i])
    return arr

# print(replace_word_with_length(["Hello", "World"]))

# Given an array of positive and negative numbers, return that same array with all values turned positive

def neg_to_pos(arr):
    for i in range(len(arr)):
        if arr[i]<0:
            arr[i]*=-1
        else:
            pass
    return arr

# print(neg_to_pos([-3,5,1,-10]))


###############################################################################################
# Given an array of strings, return that same array with each string replaced by it’s first letter
# ex.
# [“Hello”, “World”, “pie"] => [“H”, “W”, “p”]

def first_letter(arr):
    for i in range(len(arr)):
        arr[i] = arr[i][0]
    return arr

# print(first_letter(["Hello", "World", "pie"]))

###############################################################################################
# Given an array of strings, return the average length of the strings in the array

# [“Hello”, “P”] => 3

def avg_string_length(arr):
    sum = 0
    for i in range(len(arr)):
        sum+=len(arr[i])
    # avg = sum / len(arr)
    # return avg
    return sum/len(arr)

# print(avg_string_length(["Hello", "World", "pie"]))

###############################################################################################
# Given an array, reverse it in place and return the array
        #   01234        
        # ["Hello"]

def reverse(arr):
    i=0
    # print(int(len(arr)/2))
    while(i<int(len(arr)/2)):
    # for i in range(int(len(arr)/2)):
        temp = arr[len(arr)-1-i]
        arr[len(arr)-1-i] = arr[i]
        arr[i] = temp
        i+=1
    return arr

# print(reverse([1,2,3,4,5]))

###############################################################################################
# Write a function that takes degrees and isCels - a boolean True or False.
# If True, return the degrees in Fahrenheit, if false, assume the degrees are already Fahrenheit, and return celsius instead.
# F = C * 9/5 + 32

#          num   bool
def C_to_F(deg, isCels):
    if isCels:
        return deg * 9 / 5 + 32
    else:
        return deg


# print(C_to_F(30, True))

###############################################################################################
# Given a string, return a new string without the first and last letters

# “Hello” => “ell”

def part_of_string(str):
    return str[1:len(str)-1]
    # return str[0] + str[len(str)-1] => first and last

print(part_of_string("Hello"))


###############################################################################################
# Given an array of strings, return a new array with only even-length strings remaining, in their original order

def only_even(arr):
    new_arr = []
    for i in range(len(arr)):
        if len(arr[i]) % 2 ==0:
            new_arr.append(arr[i])
    return new_arr

print(only_even(["Hello", "World", ""]))


###############################################################################################
