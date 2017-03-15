def maxSequence(arr):
    max_ending_here = 0; max_so_far = 0
    for each_list_item in arr:
        max_ending_here = max_ending_here + each_list_item
        max_ending_here = max(0, max_ending_here)
        max_so_far = max(max_ending_here, max_so_far)
    return max_so_far
