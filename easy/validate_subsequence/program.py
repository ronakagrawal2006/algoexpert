arr = [5, 1, 22, 25, 6, -1, 8, 10]
seq = [5, 1, 22, 6, -1, 8, 10]


def isValidSubsequence(arr, seq):
    seq_i = 0
    arr_i = 0

    while seq_i < len(seq):
        seq_c = seq[seq_i]
        print(f'Searching {seq_c}')
        while arr_i < len(arr):
            arr_c = arr[arr_i]
            print(f'Array at: {arr_c}')
            if seq_c == arr_c:
                print(f'\t match ')
                seq_i += 1
                arr_i += 1
                break
            else:
                print(f'\t arr_move_next')
                arr_i += 1
            if arr_i>=len(seq):
                break
        if seq_i>=len(seq) or arr_i>=len(arr):
            break
			
    print(f'execution complete seq_index={seq_i},len(Seq): {len(seq)}')
    if seq_i == len(seq):
        return True
    else:
        return False



arr =  [1, 1, 1, 1, 1]
seq = [1, 1, 1]

isValidSubsequence(arr,seq)