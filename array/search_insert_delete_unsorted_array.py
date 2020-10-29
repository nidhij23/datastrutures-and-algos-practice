def findElement(arr,key):
    for i in range(len(arr)):
        if arr[i]==key:
            return i

if __name__=="__main__":
    arr = [12, 34, 10, 6, 40]
    key = 40
    n = len(arr)
    index = findElement(arr,  key)
    print(index)

