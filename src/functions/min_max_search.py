def min_max_search(arr):

    if not arr:
        return None, None

    def min_max_recursive(arr, start, end):
        if end - start == 1:
            return arr[start], arr[start]

        if end - start == 2:
            return min(arr[start], arr[start+1]), max(arr[start], arr[start+1])

        mid = start + (end - start) // 2
        left_min, left_max = min_max_recursive(arr, start, mid)
        right_min, right_max = min_max_recursive(arr, mid, end)

        return min(left_min, right_min), max(left_max, right_max)

    return min_max_recursive(arr, 0, len(arr))
