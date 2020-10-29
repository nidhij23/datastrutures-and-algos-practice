def solution(arr, key, low, high):
    if high < low:
        return -1
    mid = int((high + low) / 2)
    if key == arr[mid]:
        return mid
    if key < arr[mid]:
        return solution(arr, key, low, mid - 1)
    else:
        return solution(arr, key, mid + 1, high)


if __name__ == "__main__":
    arr = [1, 4, 5, 6, 7, 10, 28, 56, 89, 91]
    key = 100
    print(solution(arr, key, 0, len(arr) - 1))
