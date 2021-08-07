arr = [5, 1, 22, 25, 6, -1, 8, 10]
seq = [5, 1, 22, 6, -1, 8, 10]


def isValidSubsequencev2(arr, seq):
    arr_i = 0
    seq_i = 0
    while arr_i < len(arr):
        arr_curr = arr[arr_i]
        print(f'Array at {arr_curr}')
        seq_curr = seq[seq_i]
        print(f'Seq at {seq_curr}')
        if arr_curr == seq_curr:
            arr_i += 1
            seq_i += 1
        else:
            arr_i += 1
        if seq_i == len(seq):
            return True
        if arr_i == len(arr):
            return False

isValidSubsequencev2(arr,seq)