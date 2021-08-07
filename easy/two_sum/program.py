array = [3, 5, -4, 8, 11, 1, -1, 6]
target_sum = 10


def twoNumberSum(array, target_sum):
    for first_int in array:
        for second_int in array[1:]:
            if first_int == second_int:
                continue
            if first_int + second_int == target_sum:
                return [first_int, second_int]
    return []


# HashSet - Key
# HashMap - key,value
def twoNumberSum_2(array, target_sum):
    array = set(array)
    for current_int in array:
        expected_num = target_sum - current_int
        if expected_num == current_int:
            continue
        if expected_num in array:
            return [current_int, expected_num]
    return []


def binary_search(arr, search_term):
    print(f'{arr, search_term}')
    import math
    if len(arr) == 0:
        return None  # element not present
    mid_element_index = math.floor(len(arr) / 2)
    if search_term == arr[mid_element_index]:
        return mid_element_index
    elif search_term <= arr[mid_element_index]:
        print(f'passing array, left : {arr[:mid_element_index]}')
        sub_index = binary_search(arr[:mid_element_index], search_term)
        if sub_index is not None:
            return sub_index + mid_element_index
        else:
            None
    elif search_term > arr[mid_element_index]:
        print(f'passing array, right :{arr[mid_element_index + 1:]}')
        sub_index = binary_search(arr[mid_element_index + 1:], search_term)
        if sub_index is not None:
            return sub_index + mid_element_index
        else:
            None


binary_search([2, 4, 6, 8, 10], 8)
binary_search([2, 4, 6, 8, 10], 7)


def twoNumberSum_3(array, target_sum):
    # sort the array(nlogn = assuming quick sort), and do binary search - log2n
    array.sort()
    for current_int in array:
        expected_num = target_sum - current_int
        if expected_num == current_int:
            continue
        if binary_search(array, expected_num) is not None:
            return [current_int, expected_num]
    return []


#
#
array = [4, 6, 1]
target_sum = 5
twoNumberSum_2(array, target_sum)
twoNumberSum_3(array, target_sum)
#
# twoNumberSum(array, target_sum)
