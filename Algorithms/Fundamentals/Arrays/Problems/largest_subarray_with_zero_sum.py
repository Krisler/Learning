def largest_subarray_with_zero_sum(arr):
    hash_map = {}
    max_len = 0
    curr_sum = 0
    for i in range(len(arr)):
        curr_sum += arr[i]
        if curr_sum == 0:
            max_len = i + 1
        elif curr_sum in hash_map:
            max_len = max(max_len, i - hash_map[curr_sum])
        else:
            hash_map[curr_sum] = i
    return max_len

arr = [15, -2, 2, -8, 1, 7, 10, 23]
print(largest_subarray_with_zero_sum(arr))  # Output: 5

