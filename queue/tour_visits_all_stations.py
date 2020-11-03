class PetrolPump:
    def __init__(self, petrol, distance):
        self.petrol = petrol
        self.distance = distance


def printTour(arr):
    n = len(arr)
    start = 0
    end = 1
    current_petrol = arr[start].petrol - arr[start].distance
    while end != start or current_petrol < 0:
        while current_petrol < 0 and start != end:
            current_petrol -= arr[start].petrol - arr[start].distance
            start = (start + 1) % n
            if start == 0:
                return -1

        current_petrol += arr[end].petrol - arr[end].distance
        end = (end + 1) % n
    return start


if __name__ == "__main__":
    arr = [PetrolPump(6, 6), PetrolPump(3, 6), PetrolPump(7, 3)]
    start = printTour(arr)
    if start == -1:
        print("no solution")
    else:
        print("start=", start)
