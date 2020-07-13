def intersection(arrays):

    """
    YOUR CODE HERE
    """
    # go throught just the first array, fill a dict with it
    # and for the rest just check if it has something in common with intial dict?

    length = len(arrays)
    # value count should be equal to length

    # this is filled with the first array numbers, so matches MUST be in here at first
    firstDict = {}
    result = []
    # go through each array in arrays

    # array 1
    for thing in arrays[0]:
        firstDict[thing] = 1
    
    # arrays 2-10
    for i in range(1, length):
        for num in arrays[i]:
            if num in firstDict and firstDict[num] == i:
                firstDict[num] += 1
                    
    for key in firstDict:
        if firstDict[key] == length:
            result.append(key)
        # result.append(key)

    return result


if __name__ == "__main__":
    # arrays = []

    # arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    # arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    # arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    # arrays = [
    #     [1, 2, 3, 4, 5],
    #     [12, 7, 2, 9, 1],
    #     [99, 2, 7, 1,]
    # ]

    arrays = []
    arrays.append(list(range(1000000, 2000000)) + [5, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 3, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])


    print(intersection(arrays))

# [
#     [1, 2, 3, 4, 5],
#     [12, 7, 2, 9, 1],
#     [99, 2, 7, 1,]
# ]
# ```

# And we need to compute the _intersection_, that is, numbers that exist
# in all lists.

# From the above input, the return value will be:

# ```
# [1, 2]

# length = len(arrays)
#     tempDict = {}
#     # value count should be equal to length

#     # go through each array in arrays
#     for i in range(length):

#         # go through each number in current array
#         for num in arrays[i]:
#             # if this key is NOT in the dictionary
#             if num not in tempDict:
#                 tempDict[num] = 1
#             # else, it IS in the dictionary, value += 1
#             else:
#                 tempDict[num] += 1
        
#     result = []
#     for key in tempDict:
#         if tempDict[key] == length:
#             result.append(key)

#     return result