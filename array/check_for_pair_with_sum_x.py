def solution(arr, sum):
    s = set()
    for i in range(len(arr)):
        num = sum - arr[i]
        if num in s:
            return [arr[i], num]
        s.add(arr[i])


if __name__ == "__main__":
    A = [1, 4, 45, 6, 10, -8]
    sum = 16
    print(solution(A, sum))
