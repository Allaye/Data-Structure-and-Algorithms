def pair_sum(arr, summation):
    '''
    given an integer array, sum up the specific pair that add up to summation, only unique pair
    '''
    # edge case check
    if len(arr) < 2:
        print('No pair sum found!')
        return 
    array_pair = []
    arr = list(set(arr))
    for i in range(0, len(arr)):
        for j in arr[i:]:
            if arr[i]+j == summation:
                array_pair.append([i,j])
    print(f'Total pair sum is {len(array_pair)}')
    return array_pair

// Test cases
 
arr = [0, 1, 3, 3, 3, 4, 5, 5, 6, 7, 9]
arr1 = [0, 1, 3, 3, 3, 4, 5, 5, 6, 7, 9]
arr2 = [0, 1, 3, 3, 3, 4, 5, 5, 6, 7, 9]
arr3 = [0, 1, 3, 3, 3, 4, 5, 5, 6, 7, 9]
pair_sum(arr, 9)