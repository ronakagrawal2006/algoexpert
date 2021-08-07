

def sortedSquaredArray(arr):
    res=[]
    for i in arr:
        res.append(i*i)
	res.sort()
    return res


arr =  [1, 2, 3, 5, 6, 8, 9]
