import random

def main ():
    deck = []
    for i in range(10):
        deck.append(random.randint(1, 10))
    search = random.randint(1,10)
    deck.sort()
    found = recursiveBinarySearch(deck,search)

    print("deck:", deck)
    print("search:", search)
    print("postion of search:", found)

def binarySearch(list, search):
    upper = len(list) - 1
    lower = 0
    while upper >= lower:
        mid = (upper + lower) // 2
        if search == list[mid]:
            return mid
        elif search < list[mid]:
            upper = mid - 1
        else:
            lower = mid + 1
    return -1

def recursiveBinarySearch(lst, key):
    high = len(lst) - 1
    low = 0
    return recursiveBinarySearchHelper(lst, key, low, high)

def recursiveBinarySearchHelper(lst, key, low, high):
    if low > high:
        return -1 # base case

    mid = (low + high) // 2
    if key < lst[mid]:
        return recursiveBinarySearchHelper(lst, key, low, mid - 1)

    elif key == lst[mid]:
        return mid # base case

    else:
        return recursiveBinarySearchHelper(lst, key, mid + 1, high)




main()