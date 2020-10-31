from sys import maxsize


def solution(a):
    size = len(a)
    max_so_far = -maxsize - 1
    max_ending_here = 0
    for i in range(0, size):
        max_ending_here = max_ending_here + a[i]
        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
        if max_ending_here < 0:
            max_ending_here = 0
    return max_so_far


if __name__ == "__main__":
    a = [-13, -3, -25, -20, -3, -16, -23, -12, -5, -22, -15, -4, -7]
    print(solution(a))
    b=[-2,-3,4,-1,-2,1,5,-3]
    print(solution(b))
