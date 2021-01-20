import random
import time
import math
import matplotlib.pyplot as plt
import matplotlib.animation  as animation

def swap(array, i, j):
    if i != j:
        array[i], array[j] = array[j], array[i]

#Bubble sort
def Bubblesort(array):
    n = len(array)

    if n == 1:
        return

    optimized = True

    for i in range(n - 1):
        if not optimized:
            break
        optimized = False

        for j in range(0, n-i-1):
            if array[j] > array[j+1]:
                swap(array, j, j + 1)
                optimized = True
            yield array

#Merge sort
def Mergesort(array, start, end):
    if end <= start:
        return

    mid = start + ((end - start + 1) // 2) - 1
    yield from Mergesort(array, start, mid)
    yield from Mergesort(array, mid + 1, end)
    yield from merge(array, start, mid, end)
    yield array

def merge(array, start, mid, end):
    merged = []
    leftindex = start
    rightindex = mid + 1
    
    while leftindex <= mid and rightindex <= end:
        if array[leftindex] < array[rightindex]:
            merged.append(array[leftindex])
            leftindex += 1
        else:
            merged.append(array[rightindex])
            rightindex += 1

    while leftindex <= mid:
        merged.append(array[leftindex])
        leftindex += 1

    while rightindex <= mid:
        merged.append(array[rightindex])
        rightindex += 1

    for i, sorted_val in enumerate(merged):
        array[start + i] = sorted_val
        yield array

#Quicksort
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
    if low < high:
        pi = QuickPartition(array, low, high)

        yield from Quicksort(array, low, pi - 1)
        yield from Quicksort(array, pi + 1, high)
        yield array

#Insertion sort
def Insertionsort(array):
    for i in range(1, len(array)):
        j = i
        while j > 0 and array[j] < array[j - 1]:
            swap(array, j, j-1)
            j -= 1
            yield array

#Selection sort
def Selectionsort(array): #this is completely fucked lmao
    if len(array) == 1:
        return

    for i in range(len(array)):
        mini_element = i
        for j in range(i + 1, len(array)):
            if array[mini_element] > array[j]:
                mini_element = j
            swap(array, i, mini_element)
    yield array
        
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
        yield array

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

        yield array

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
        yield array

#bucket sort
def Bucketsort(array):
    bucket = []

    for i in range(len(array)):
        bucket.append([])

    for j in array:
        index_bucket = 0
        bucket[index_bucket].append(j)

    for i in range(len(array)):
        bucket[i] = sorted(bucket[i])

    k = 0
    for i in range(len(array)):
        for j in range(len(bucket[i])):
            array[k] = bucket[i][j]
            k += 1
    yield array

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
    yield array

#radix sort
def RadixCountingsort(array, exp1):
    output_array = [0] * (element)
    count_array = [0] * (10)

    for i in range(0, element):
        index = (array[i] / exp1)
        count_array[int(index % 10)] += 1

    for i in range(1, 10):
        count_array[i] += count_array[i - 1]

    i = element - 1
    while i > 0:
        index = (array[i] / exp1)
        output_array[count_array[int(index % 10)] - 1] = array[i]
        count_array[int(index % 10)] -= 1
        i -= 1

    i = 0
    for i in range(0, len(array)):
        array[i] = output_array[i]
def Radixsort(array):
    max1 = max(array)
    exp = 1
    while max1 / exp > 0:
        RadixCountingsort(array, exp)
        exp *= 10

    yield array

#Recursive bubble sort
def RecursiveBubblesort(array, n):
    if n == 1:
        return

    for i in range(n - 1):
        if array[i] > array[i + 1]:
            array[i], array[i + 1] = array[i + 1], array[i]

    if n - 1 > 1:
        RecursiveBubblesort(array, n - 1)

    yield array
    yield from RecursiveBubblesort(array, n - 1)

while True:
    if __name__ == "__main__":
        def remove(choice):
            return choice.replace(" ", "")

        #element = int(input("Enter the number of elements for the array: "))
        element = 500
        print("(Bubble) Sort, (Merge) Sort, (Quick) Sort, (Insertion) Sort,")
        print("(Selection) Sort, (Heap) Sort, (Shell) Sort, (Comb) Sort,")
        print("(Bucket) Sort, (Counting) Sort, (Radix) Sort,")
        print("(Recursive Bubble) Sort, OR (Quit)")
        choice_msg = "What algorithm do you want to use?: "
        choice = input(choice_msg)

        #random list of int
        array = [x + 1 for x in range(element)]
        random.seed(time.time())
        random.shuffle(array)
        
        if remove(choice.lower()) == "bubble":
            title = "Bubble sort"
            animation_generator = Bubblesort(array)
            print("\n")
        elif remove(choice.lower()) == "merge":
            title = "Merge sort"
            animation_generator = Mergesort(array, 0, element - 1)
            print("\n")
        elif remove(choice.lower()) == "quick":
            title = "Quick sort"
            animation_generator = Quicksort(array, 0, element - 1)
            print("\n")
        elif remove(choice.lower()) == "insertion":
            title = "Insertion sort"
            animation_generator = Insertionsort(array)
            print("\n")
        elif remove(choice.lower()) == "selection":
            title = "Selection sort"
            animation_generator = Selectionsort(array)
            print("\n")
        elif remove(choice.lower()) == 'heap':
            title = 'Heap Sort'
            animation_generator = Heapsort(array)
            print("\n")
        elif remove(choice.lower()) == 'shell':
            title = "Shell Sort"
            animation_generator = Shellsort(array)
            print("\n")
        elif remove(choice.lower()) == 'comb':
            title = "Comb Sort"
            animation_generator = Combsort(array)
            print("\n")
        elif remove(choice.lower()) == 'bucket':
            title = "Bucket Sort"
            animation_generator = Bucketsort(array)
            print("\n")
        elif remove(choice.lower()) == 'counting':
            title = "Counting Sort"
            animation_generator = Countingsort(array)
            print("\n")
        elif remove(choice.lower()) == 'radix':
            title = "Radix Sort"
            animation_generator = Radixsort(array)
            print("\n")
        elif remove(choice.lower()) == "recursivebubble":
            title = "Recursive bubble sort"
            n = len(array)
            animation_generator = RecursiveBubblesort(array, n)
            print("\n")
        elif remove(choice.lower()) == "quit":
            break
        else:
            print("That is not a choice\n")
            continue

        figure, axis = plt.subplots()
        axis.set_title(title)

        bar_rects = axis.bar(range(len(array)), array, align = 'edge')

        axis.set_xlim(0, element)
        axis.set_ylim(0, int(1.07 * element))

        text = axis.text(0.02, 0.95, "", transform = axis.transAxes)

        iteration = [0]
        def update_figure(array, rects, iteration):
            for rect, val in zip(rects, array):
                rect.set_height(val)
            iteration[0] += 1
            text.set_text("Number of operations: {}".format(iteration[0]))

        anim = animation.FuncAnimation(figure,
                                       func = update_figure,
                                       fargs = (bar_rects, iteration),
                                       frames = animation_generator,
                                       interval = 1,
                                       repeat = False)
        
        plt.show()
