import random
import time
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
def Quicksort(array, low, high):
    if low >= high:
        return
    pivot = array[high]
    pivotindex = low

    for i in range(low, high):
        if array[i] < pivot:
            swap(array, i, pivotindex)
            pivotindex += 1
        yield array
    swap(array, high, pivotindex)
    yield array
    yield from Quicksort(array, low, pivotindex - 1)
    yield from Quicksort(array, pivotindex + 1, high)

#Insertion sort
def Insertionsort(array):
    for i in range(1, len(array)):
        j = i
        while j > 0 and array[j] < array[j - 1]:
            swap(array, j, j-1)
            j -= 1
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
    yield from RecursiveBubblesort(array, n -1)

#Selection sort
def Selectionsort(array):
    if len(array) == 1:
        return

    for i in range(len(array)):
        mini_element = i
        for j in range(i + 1, len(array)):
            if array[mini_element] > array[j]:
                mini_element = j
            yield array
        swap(array, i, mini_element)
        yield array


while True:
    if __name__ == "__main__":
        def remove(choice):
            return choice.replace(" ", "")

        #element = int(input("Enter the number of elements for the array: "))
        element = 300
        print("(Bubble) Sort, (Merge) Sort, (Quick) Sort, (Insertion) Sort,")
        print("(Recursive Bubble) Sort, (Selection) Sort, OR (Quit)")
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
        elif remove(choice.lower()) == "recursivebubble":
            title = "Recursive bubble sort"
            n = len(array)
            animation_generator = RecursiveBubblesort(array, n)
            print("\n")
        elif remove(choice.lower()) == "selection":
            title = "Selection sort"
            animation_generator = Selectionsort(array)
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
