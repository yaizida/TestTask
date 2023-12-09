def max_sorted_blocks(arr):
    max_blocks = 1
    n = len(arr)

    if n == 0 or n == 1:
        return n

    left_max = arr[0]
    right_min = arr[-1]

    for i in range(1, n):
        left_max = max(left_max, arr[i])
        right_min = min(right_min, arr[n - 1 - i])

        if arr[i] < right_min:
            continue
        if arr[n - 1 - i] > left_max:
            continue

        max_blocks = max(max_blocks, 2)

    return max_blocks


if __name__ == '__main__':
    arr = list(map(int, input().split()))
    print(max_sorted_blocks(arr))
