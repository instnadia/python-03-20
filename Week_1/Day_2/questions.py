
students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
# def iteratedDictionary(some_list):
#     for i in range(len(some_list)):
#         for key in some_list[i]:
#             print(key, '-', some_list[i][key])
# iteratedDictionary()


     

# Reverse List - Create a function that takes a list and return that list with values reversed. Do this without creating a second list. (This challenge is known to appear during basic technical interviews.)

#     Example: reverse_list([37,2,1,-9]) should return [-9,1,2,37]
def reverse_list(arr):
    test = 0
    for i in range(int(len(arr)/2)):
    # while test < len(arr)/2:
        last = arr[len(arr)-1-test]
        arr[len(arr)-1-test] = arr[test]
        arr[test] = last
        test+=1
    return arr

print(reverse_list([37,2,1,-9]))

balance = 100

print("balance is ${}".format(balance))

