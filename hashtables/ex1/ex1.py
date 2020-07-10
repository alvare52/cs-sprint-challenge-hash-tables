# weights = list of weights
# length = size of weights list 
# limit = maximum weight allowed
# find sum of 2 items in weights list that equal the limit
# returns a tuple of ints like this
# (zero, one) where zero = high valued index and one = low valued index
# returns None if no such pair exists (MUST be LINEAR time)
def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here

    table = {}

    # fill up table dict with weight as key and limit - weight as value
    # OR just the index as the key, and the weight as a value
    # print("Filling in dictionary")

    for i in range(length):
        # print(f"key = {i} value = {weights[i]}")
        # table[weights[i]] = i
        table[i] = weights[i]

    high = None
    low = None
    matches = []
    
    # print(f"table starts = {table}")
    for key in table:
        # if value is equal to a KEY in the table dict
        # OR if 
        if limit - table[key] in table.values():
            # print(f"match found, {table[key]}")
            matches.append(key)
            # print(table[key])
    
    # print(f"matches = {matches}")
    # print(f"table = {table}")

    matches.sort()
    # now [low, high]
    if len(matches) == 2:
        high = matches[1]
        low = matches[0]
        return [high, low]
    
    
    if high == None and low == None:
        # print("NO PAIR FOUND")
        return None
    
# print("\n---START---")
# print(get_indices_of_item_weights([4, 6, 10, 15, 16], 5, 21))

#     #         weights_2 = [4, 4]
#     #         answer_2 = get_indices_of_item_weights(weights_2, 2, 8)
#     #         self.assertTrue(answer_2[0] == 1)
#     #         self.assertTrue(answer_2[1] == 0)
# print("2nd\n")
# print(get_indices_of_item_weights([4, 4], 2, 8))