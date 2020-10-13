import random
import time

'''
show time complexity
'''

array = [423,5643,2345786,345,567,43,6,23,87,4,783,7]
#array = [423,5643,2345786,-345,567,43,-6,23,87,-4,783,7]#negatives
#array = [423,5643,234.5786,345,56.7,43,6,23,87,4,783,7]#floats
element = len(array)

def TimeComplex():


    pass

def swap(array, i, j):
    if i != j:
        array[i], array[j] = array[j], array[i]

def Bubblesort(array):
    if element == 1:
        return

    optimized = True

    for i in range(element - 1):
        if not optimized:
            break
        optimized = False

        for j in range(0, element - i - 1):
            if array[j] > array[j + 1]:
                swap (array, j, j + 1)
                optimized = True

def Mergesort(array):
    if len(array) > 1: 
        middle = len(array) // 2
        left = array[:middle]
        right = array[middle:]
  
        Mergesort(left)
        Mergesort(right)
  
        i = j = k = 0

        while i < len(left) and j < len(right): 
            if left[i] < right[j]: 
                array[k] = left[i] 
                i += 1
            else: 
                array[k] = right[j] 
                j += 1
            k += 1

        while i < len(left): 
            array[k] = left[i] 
            i += 1
            k += 1
          
        while j < len(right): 
            array[k] = right[j] 
            j += 1
            k += 1

def QuickPartition(array, low, high):
    i = (low - 1)
    pivot = array[high]

    for j in range(low, high):
        if array[j] < pivot:
            i = i + 1
            array[i], array[j] = array[j], array[i]

    array[i + 1], array[high] = array[high], array[i + 1]
    return(i + 1)
def Quicksort(array, low, high):
    if low >= high:
        return
    if low < high:
        pi = QuickPartition(array, low, high)

        Quicksort(array, low, pi - 1)
        Quicksort(array, pi + 1, high)

def Insertionsort(array):
    for i in range(1, element):
        j = i
        while j > 0 and array[j] < array[j - 1]:
            swap(array, j, j - 1)
            j -= 1

#selection sort
def Selectionsort(array):
    if element == 1:
        return

    for i in range(element):
        mini_element = i
        for j in range(i + 1, len(array)):
            if array[mini_element] > array[j]:
                mini_element = j
            swap(array, i, mini_element)

#heap sort
def heapify(array, element, i):
    high = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < element and array[i] < array[left]:
        high = left
    if right < element and array[high] < array[right]:
        high = right

    swap(array, i, high)
    if high != i:
        #array[i], array[high] = array[high], array[i]
        heapify(array, element, high)
def Heapsort(array):
    for i in range(element // 2 - 1, -1, -1):
        heapify(array, element, i)

    for i in range(element - 1, 0, -1):
        swap(array, i, 0)
        #array[i], array[0] = array[0], array[i]
        heapify(array, i, 0)

#shell sort
def Shellsort(array):
    gap = element//2

    while gap > 0:
        for i in range(gap, element):
            temporary = array[i]

            j = i
            while j >= gap and array[j - gap] > temporary:
                array[j] = array[j - gap]
                j -= gap
            array[j] = temporary
        gap //= 2

#comb sort
def Nextgap(gap):
    gap = (gap * 10)//13
    if gap < 1:
        return 1
    return gap
def Combsort(array):
    gap = element
    swapped_value = True

    while gap != 1 or swapped_value == 1:
        gap = Nextgap(gap)
        swapped_value = False

        for i in range(0, element - gap):
            if array[i] > array[i + gap]:
                array[i], array[i + gap] = array[i + gap], array[i]
                swapped_value = True

#bucket sort
'''

'''
def InsertionBucketsort(bucket):
    for i in range(1, len(bucket)):
        up = bucket[i]
        j = i - 1
        while j >= 0 and bucket[j] > up:
            bucket[j + 1] = bucket[j]
            j -= 1
        bucket[j + 1] = up
    return bucket

def Bucketsort(array):
    temp_array = []
    slot = 10

    for i in range(slot):
        temp_array.append([])

    for j in array:
        #index_bucket = slot * j
        index_bucket = int(slot * j) #IndexError: list index out of range
        array[index_bucket].append(j)
    for i in range(slot):
        temp_array[i] = InsertionBucketsort(temp_array[i])

    k = 0
    for i in range(slot):
        for j in range(len(temp_array[i])):
            array[k] = temp_array[i][j]
            k += 1
    return array

#counting sort
def Countingsort(array):
    maximum = int(max(array))
    minimum = int(min(array))
    range_max_min = maximum - minimum + 1

    count_array = [0 for _ in range(range_max_min)]
    out_array = [0 for _ in range(element)]

    for i in range(0, element):
        count_array[array[i] - minimum] += 1
    for i in range(1, len(count_array)):
        count_array[i] += count_array[i - 1]
    for i in range(element - 1, -1, -1):
        out_array[count_array[array[i] - minimum] - 1] = array[i]
        count_array[array[i] - minimum] -= 1
    for i in range(0, element):
        array[i] = out_array[i]
    return array

#radix sort
def Radixsort(array):
    pass

def RecursiveBubblesort(array, n):
    if n == 1:
        return

    for i in range(n - 1):
        if array[i] > array[i + 1]:
            array[i], array[i + 1] = array[i + 1], array[i]

    if n - 1 > 1:
        RecursiveBubblesort(array, n - 1)
    RecursiveBubblesort(array, n - 1)

run = True
while run:
    if __name__ == '__main__':
        def remove(choice):
            return choice.replace(" ", "")

        print("(Bubble) Sort, (Merge) Sort, (Quick) Sort, (Insertion) Sort,")
        print("(Selection) Sort, (Heap) Sort, (Shell) Sort, (Comb) Sort,")
        print("(Bucket) Sort, (Counting) Sort, (Radix) Sort,")
        print("(Recursive Bubble) Sort, OR (Quit)")
        choice_msg = "What algorithm do you want to use?: "
        choice = input(choice_msg)
        
        if remove(choice.lower()) == "bubble":
            print("Unsorted array: ", array)
            Bubblesort(array)
            print("Sorted array: ", array)
            print("\n")
            array = [423,5643,2345786,345,567,43,6,23,87,4,783,7]
            element = len(array)
        elif remove(choice.lower()) == "merge":
            print("Unsorted array: ", array)
            Mergesort(array)
            print("Sorted array: ", array)
            print("\n")
            array = [423,5643,2345786,345,567,43,6,23,87,4,783,7]
            element = len(array)
        elif remove(choice.lower()) == "quick":
            print("Unsorted array: ", array)
            Quicksort(array, 0, element - 1)
            print("Sorted array: ", array)
            print("\n")
            array = [423,5643,2345786,345,567,43,6,23,87,4,783,7]
            element = len(array)
        elif remove(choice.lower()) == "insertion":
            print("Unsorted array: ", array)
            Insertionsort(array)
            print("Sorted array: ", array)
            print("\n")
            array = [423,5643,2345786,345,567,43,6,23,87,4,783,7]
            element = len(array)
        elif remove(choice.lower()) == "selection":
            print("Unsorted array: ", array)
            Selectionsort(array)
            print("Sorted array: ", array)
            print("\n")
            array = [423,5643,2345786,345,567,43,6,23,87,4,783,7]
            element = len(array)
        elif remove(choice.lower()) == "heap":
            print("Unsorted array: ", array)
            Heapsort(array)
            print("Sorted array: ", array)
            print("\n")
            array = [423,5643,2345786,345,567,43,6,23,87,4,783,7]
            element = len(array)
        elif remove(choice.lower()) == "shell":
            print("Unsorted array: ", array)
            Shellsort(array)
            print("Sorted array: ", array)
            print("\n")
            array = [423,5643,2345786,345,567,43,6,23,87,4,783,7]
            element = len(array)
        elif remove(choice.lower()) == "comb":
            print("Unsorted array: ", array)
            Combsort(array)
            print("Sorted array: ", array)
            print("\n")
            array = [423,5643,2345786,345,567,43,6,23,87,4,783,7]
            element = len(array)
        elif remove(choice.lower()) == "bucket":
            print("Unsorted array: ", array)
            Bucketsort(array)
            print("Sorted array: ", array)
            print("\n")
            array = [423,5643,2345786,345,567,43,6,23,87,4,783,7]
            element = len(array)
        elif remove(choice.lower()) == "counting":
            print("Unsorted array: ", array)
            Countingsort(array)
            print("Sorted array: ", array)
            print("\n")
            array = [423,5643,2345786,345,567,43,6,23,87,4,783,7]
            element = len(array)
        elif remove(choice.lowewr()) == 'radix':
            print("Unsorted array: ", array)
            Radixsort(array)
            print("Sorted array: ", array)
            print("\n")
            array = [423,5643,2345786,345,567,43,6,23,87,4,783,7]
            element = len(array)
        elif remove(choice.lower()) == "recursivebubble":
            n = len(array)
            print("Unsorted array: ", array)
            RecursiveBubblesort(array, n)
            print("Sorted array: ", array)
            print("\n")
            array = [423,5643,2345786,345,567,43,6,23,87,4,783,7]
            element = len(array)
        elif remove(choice.lower()) == "quit":
            run = False
            break
        else:
            print("That is not a choice\n")
            continue