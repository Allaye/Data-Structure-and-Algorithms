def maximum_subarray(arr):
    current_max = 0
    highest_max = 0
    for value in arr:
        current_max += value
        if current_max < 0:
            current_max = 0
        elif current_max > highest_max:
                highest_max = current_max
    return highest_max

# testing 
maximum_subarray([2,-10,11,3,4,-5,1])
# ans = 18
maximum_subarray([1,2,-1,3,4,10,10,-10,-1])
# ans = 29