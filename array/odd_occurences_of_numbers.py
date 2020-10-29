def solution(arr):
    hshmap = dict()
    for i in range(len(arr)):
        hshmap[arr[i]] = hshmap.get(arr[i], 0) + 1
    for h in hshmap:
        print(h, "->", hshmap[h])
        if hshmap[h] % 2 != 0:
            return h


if __name__ == "__main__":
    arr = [2, 3, 5, 4, 5, 2, 4, 3, 5, 2, 4, 4, 2]
    print(solution(arr))
