def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    # create a dictionary for each array in arrays?
    # or create an array of dictionaries?

    length = len(arrays)
    tempDict = {}
    # print(f"length = {length}")
    # value count should be equal to length

    for array in arrays:
        for num in array:
            # if this key is NOT in the dictionary
            if num not in tempDict:
                tempDict[num] = 1
            # else, it IS in the dictionary, value += 1
            else:
                tempDict[num] += 1
        
    # print(f"tempDict = {tempDict}")
    result = []
    for key in tempDict:
        if tempDict[key] == length:
            result.append(key)

    # print(f"arr = {result}")
    # for dictionary in listOfDicts:

    return result


if __name__ == "__main__":
    # arrays = []

    # arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    # arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    # arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    arrays = [
        [1, 2, 3, 4, 5],
        [12, 7, 2, 9, 1],
        [99, 2, 7, 1,]
    ]

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