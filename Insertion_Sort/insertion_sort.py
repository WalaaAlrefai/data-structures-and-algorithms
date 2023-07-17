def insertion_sort(arr: int) -> list:

    for i in range(1,len(arr)):
        temp_i = arr[i]
        j = i - 1
        while j >= 0 and temp_i < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
            arr[j + 1] = temp_i
    return arr



if __name__ == "__main__":
    print(insertion_sort([4, 8, 23, 42, 16, 15]))