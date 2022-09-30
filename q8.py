
def isNums(arr):
    for element in arr:
        is_int = isinstance(element, int)
        is_float = isinstance(element, float)
        if not (is_int or is_float):
            return False
    return True


def isStrings(arr):
    for element in arr:
        if not isinstance(element, str):
            return False
    return True


def countOdds(arr):
    count = 0
    for num in arr:
        if num % 2 != 0:
            count += 1
    return count


def displayReverse(arr):
    for i in range(len(arr)-1, -1, -1):
        print(arr[i], end=" ")
    print()


def find(arr, x):
    if x not in arr:
        return -1
    return arr.index(x)


def deleteElement(arr, x):
    if x not in arr:
        print(f"Can't remove {x} from list as it doesn't exist")
        return
    arr.remove(x)
    print(f"Removed {x} from list : {arr}")


def common_members(arr1, arr2):
    common_elements = []
    for element in arr1:
        if element in arr2 and element not in common_elements:
            common_elements.append(element)
    return common_elements




