
# input = int list (ints are in any order), list can have up to 5 MILLION elements
# find which negative ints have positive counterparts
# return list of those ints
def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    result = []
    table = {}
    opps = {}
    # length = len(a)
    # print(f"length = {length}")
    
    # go through all nums
    for num in a:
        # if num is not in table, add its opp to another dictionary (opps)
        if num > 0:
            table[num] = 0
        else:
            opps[num] = 0
        # if num not in table:
        #     table[num] = 0
        #     opps[-(num)] = 0
        # if key IS in table, check if a positive version is in there also
        # else:
        #     table[num] += 1
    # print("lens")
    # print(len(table))
    # print(len(opps))
    # checks positive table (if its len is smaller)
    
    # for key in table:
    #     if -(key) in opps:
    #         result.append(key)
    
    for key in opps:
        if -key in table:
            result.append(-(key))

    # print(f"table = {table}")
    # print(f"opps = {opps}")

    return result
    # result = []
    # table = {}
    # opps = {}
    # length = len(a)
    # print(f"length = {length}")
    
    # # NEW
    # newResults = []
    # # go through all nums
    # for num in a:

    #     # OLD part 1
    #     # if num is not in table, add its opp to another dictionary (opps)
    #     if num not in table:
    #         table[num] = 0
    #         opps[-(num)] = 0
        
    #     # NEW
    #     if num in opps and table[num] in opps:
    #         if num > 0:    
    #             newResults.append(num)

    # # OLD part 2
    # for key in table:
    #     if key in opps and key > 0:
    #         result.append(key)

    # # NEW
    # # for key in table:
    # #     if key in opps and key > 0:
    # #         newResults.append(key)

    # print(f"table = {table}")
    # # print(f"opps = {opps}")
    # print(f"newResults = {newResults}")
    # # return result
    # return newResults


if __name__ == "__main__":
    print(has_negatives([ 1, -1, 2, 3, -4, -3, 4, -5, 6, 7 ]))