def solution(arr):
    incl = 0
    excl = 0
    sum = 0
    for i in arr:
        incl = excl + i
        excl = sum
        sum = max(incl, excl)
    return sum


if __name__ == "__main__":
    arr = [5, 5, 10, 100, 10, 5]
    print(solution(arr))
