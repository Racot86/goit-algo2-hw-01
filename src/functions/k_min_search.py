def k_min_search(arr, k):

    if not arr:
        return None

    if k < 0 or k >= len(arr):
        return None

    def _quickselect(arr, left, right, k):
        if left == right:
            return arr[left]

        pivot_index = partition(arr, left, right)

        if k == pivot_index:
            return arr[k]
        elif k < pivot_index:
            return _quickselect(arr, left, pivot_index - 1, k)
        else:
            return _quickselect(arr, pivot_index + 1, right, k)

    def partition(arr, left, right):
        pivot = arr[right]
        i = left

        for j in range(left, right):
            if arr[j] <= pivot:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1

        arr[i], arr[right] = arr[right], arr[i]
        return i

    return _quickselect(arr, 0, len(arr) - 1, k)