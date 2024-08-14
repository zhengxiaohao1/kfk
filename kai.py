def bubble_sort(arr):
    n = len(arr)
    for i in range(0, n):  # 表示排序的轮次
        is_swap = False  # 表示是否在该轮次有交换操作
        for j in range(1, n-i):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
                is_swap = True
        if not is_swap:  # 若是该轮次没有交换操作，说明所有元素已经排好序了
            return arr
    