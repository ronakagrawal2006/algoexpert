arr = [-3, 1, 2]

def sortedSquaredArray(arr):
    start_i = 0
    end_i = len(arr)-1

    res = [None]*len(arr)#empty array
    for i in range(len(arr)-1, -1, -1):
        if abs(arr[start_i]) > abs(arr[end_i]):# get the index of largetst abs value or element that will come at the end
            sq_i = start_i
            start_i += 1
        else:
            sq_i = end_i
            end_i -= 1
        res[i] = arr[sq_i]*arr[sq_i]
    return res

    