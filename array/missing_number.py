def solution(arr):
    n = len(arr)
    sum = n * (n + 1) / 2
    actual_sum = 0
    for i in range(n - 1):
        actual_sum = actual_sum + arr[i]
    return sum - actual_sum


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 10]
    print(solution(arr))
