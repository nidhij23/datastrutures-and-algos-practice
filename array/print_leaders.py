def solution(arr):
    size = len(arr)
    for i in range(0, size):
        for j in range(i + 1, size):
            if arr[j] > arr[i]:
                break
        if j == size - 1:
            print(arr[i])


if __name__ == "__main__":
    arr = [16, 17, 4, 3, 5, 2]
    print(solution(arr))
