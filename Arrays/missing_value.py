def finder(arr1, arr2):
    if len(arr1) != len(arr2)+1:
        print('second array must be one less than the first')
        return -1
    for item in arr1:
        if item in arr2:
            arr2.remove(item)
        else:           
            break
    return item

def finder1(arr1, arr2):
    arr1.sort()
    arr2.sort()
    for a,b in zip(arr1, arr2):
        if a != b:
            return a
    remark = 'no missing value'
    return remark

# testing solutions
aaa = [1,2,3,4,5,6,7,8,9,0]
bbb = [3,0,5,1,2,6,7,9,8]
finder1(aaa, bbb)