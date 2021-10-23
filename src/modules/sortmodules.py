import random

class Sort:

    def __init__(self, list):
        self.__list = list

    def selectionSort(self):
        currentMinIndex = 0
        for i in range(len(self.__list) - 1):
            currentMinIndex = i
            for j in range(i + 1, len(self.__list)):
                if self.__list[currentMinIndex] > self.__list[j]:
                    currentMinIndex = j

            if currentMinIndex != i:
                self.__list[i], self.__list[currentMinIndex] = self.__list[currentMinIndex], self.__list[i]
        return self.__list

    def insertionSort(self):
        for i in range(1, len(self.__list)):
            currentElement = self.__list[i]
            j = i - 1
            while j >= 0 and self.__list[j] > currentElement:
                self.__list[j + 1] = self.__list[j]
                print(self.__list)
                j -= 1
            self.__list[j + 1] = currentElement
            print(self.__list)
        return self.__list

    def bubbleSort(self):
        didSwap = True
        sortCount = 1

        while didSwap == True:
            didSwap = False


            for i in range(len(self.__list) - sortCount):
                if self.__list[i] > self.__list[i + 1]:
                    self.__list[i], self.__list[i + 1] = self.__list[i + 1], self.__list[i]
                    didSwap = True
            sortCount += 1
        return self.__list

def test():
    lst1 = []

    for i in range(10):
        lst1.append(random.randint(10, 99))
    print("Original List:", lst1)
    list = Sort(lst1)
    # print("Selection Sort:", list.selectionSort())
    # print("Insertions Sort:", list.insertionSort())
    print("Bubble Sort:", list.bubbleSort())
    lst1.sort()
    print("Sort Function:", lst1)