def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        tmp = arr[i]   # 将当前要比较的未排序元素存到临时变量tmp，方便后移
        j = i - 1
        while j >= 0 and arr[j] > tmp:   # 从后往前遍历已排序元素，若是大于tmp，就往后移一位，否则，就将tmp插到该元素后面
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = tmp 
    return arr 