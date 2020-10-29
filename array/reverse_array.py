def solution(arr):
    start = 0
    end = len(arr) - 1
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
    return arr


if __name__ == "__main__":
    arr = [3, 5, 12, 0, 89, 34, 14, 7]
    print(solution(arr))
