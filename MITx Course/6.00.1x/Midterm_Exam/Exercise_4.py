# Write a Python function that returns a list of keys in 
# aDict with the value target. The list of keys you return 
# should be sorted in increasing order. The keys and values 
# in aDict are both integers. (If aDict does not contain the 
#                              value target, you should return an empty list.)

# This function takes in a dictionary and an integer and returns a list.

# def keysWithValue(aDict, target):
#     '''
#     aDict: a dictionary
#     target: an integer
#     '''
#     # Your code here  

def keysWithValue(aDict, target):
    '''
    aDict: a dictionary
    target: an integer
    Returns a list of keys in aDict with the value target, sorted in increasing order.
    '''
    result = []
    for key in aDict:
        if aDict[key] == target:
            result.append(key)
    result.sort()
    return result