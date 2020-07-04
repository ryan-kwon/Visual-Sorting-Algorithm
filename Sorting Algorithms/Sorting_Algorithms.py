'''This is a collection of sorting algorithms
*** All types of sorting algorithms ***
- Bubble sort
First Pass:
( 5 1 4 2 8 ) –> ( 1 5 4 2 8 ), Here, algorithm compares the first two elements, and swaps since 5 > 1
( 1 5 4 2 8 ) –>  ( 1 4 5 2 8 ), Swap since 5 > 4
( 1 4 5 2 8 ) –>  ( 1 4 2 5 8 ), Swap since 5 > 2
( 1 4 2 5 8 ) –> ( 1 4 2 5 8 ), Now, since these elements are already in order (8 > 5), algorithm does not swap them

Second Pass:
( 1 4 2 5 8 ) –> ( 1 4 2 5 8 )
( 1 4 2 5 8 ) –> ( 1 2 4 5 8 ), Swap since 4 > 2
( 1 2 4 5 8 ) –> ( 1 2 4 5 8 )
( 1 2 4 5 8 ) –>  ( 1 2 4 5 8 )
Now, the array is already sorted, but our algorithm does not know if it is completed
The algorithm needs one whole pass without any swap to know it is sorted

Third Pass:
( 1 2 4 5 8 ) –> ( 1 2 4 5 8 )
( 1 2 4 5 8 ) –> ( 1 2 4 5 8 )
( 1 2 4 5 8 ) –> ( 1 2 4 5 8 )
( 1 2 4 5 8 ) –> ( 1 2 4 5 8 )

- Merge sort
MergeSort(arr[], l,  r)
If r > l
     1. Find the middle point to divide the array into two halves:  
             middle m = (l+r)/2
     2. Call mergeSort for first half:   
             Call mergeSort(arr, l, m)
     3. Call mergeSort for second half:
             Call mergeSort(arr, m+1, r)
     4. Merge the two halves sorted in step 2 and 3:
             Call merge(arr, l, m, r)

- Quicksort
QuickSort is a Divide and Conquer algorithm
It picks an element as pivot and partitions the given array around the picked pivot
There are many different versions of quickSort that pick pivot in different ways

Always pick first element as pivot
Always pick last element as pivot (implemented below)
Pick a random element as pivot
Pick median as pivot

The key process in quickSort is partition()
Target of partitions is, given an array and an element x of array as pivot,
put x at its correct position in sorted array and put all smaller elements (smaller than x) before x,
and put all greater elements (greater than x) after x. All this should be done in linear time

PARTITION PSEUDO CODE
This function takes last element as pivot,
places the pivot element at its correct position in sorted array,
and places all smaller (smaller than pivot) to left of pivot and
all greater elements to right of pivot
partition (arr[], low, high)
{
    // pivot (Element to be placed at right position)
    pivot = arr[high];  
 
    i = (low - 1)  // Index of smaller element

    for (j = low; j <= high- 1; j++)
    {
        // If current element is smaller than the pivot
        if (arr[j] < pivot)
        {
            i++;    // increment index of smaller element
            swap arr[i] and arr[j]
        }
    }
    swap arr[i + 1] and arr[high])
    return (i + 1)
}

- Insertion sort
Algorithm
// Sort an arr[] of size n
insertionSort(arr, n)
Loop from i = 1 to n-1
……a) Pick element arr[i] and insert it into sorted sequence arr[0…i-1]

Example:
12, 11, 13, 5, 6

Let us loop for i = 1 (second element of the array) to 4 (last element of the array)

i = 1. Since 11 is smaller than 12, move 12 and insert 11 before 12
11, 12, 13, 5, 6

i = 2. 13 will remain at its position as all elements in A[0..I-1] are smaller than 13
11, 12, 13, 5, 6

i = 3. 5 will move to the beginning and all other elements from 11 to 13 will move one position ahead of their current position.
5, 11, 12, 13, 6

i = 4. 6 will move to position after 5, and elements from 11 to 13 will move one position ahead of their current position.
5, 6, 11, 12, 13

- Recursive bubble sort
Recursive Bubble Sort has no performance/implementation advantages,
but can be a good question to check one’s understanding of Bubble Sort and recursion

If we take a closer look at Bubble Sort algorithm,
we can notice that in first pass, we move largest element to end (Assuming sorting in increasing order)
In second pass, we move second largest element to second last position and so on

*Recursion Idea*
Base Case: If array size is 1, return
Do One Pass of normal Bubble Sort. This pass fixes last element of current subarray
Recur for all elements except last of current subarray
'''

'''
FOR TESTING CODES

'''

'''
FOR SAVING CODES
'''

import random
import time
import matplotlib.pyplot as plt
import matplotlib.animation  as animation

#import itertools
#import sys

'''What kind of fucking bypass loop is this lol
import sys

sys.setrecursionlimit(10**6)
'''
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

        element = int(input("Enter the number of elements for the array: "))
        print("(Bubble) Sort, (Merge) Sort, (Quick) Sort, (Insertion) Sort,")
        print("(Recursive Bubble) Sort, (Selection) Sort")
        choice_msg = "What algorithm do you want to use?: "
        choice = input(choice_msg)

        #random list of int
        array = [x + 1 for x in range(element)]
        random.seed(time.time())
        random.shuffle(array)
        
        if remove(choice.lower()) == "bubble":
            title = "Bubble sort"
            animation_generator = Bubblesort(array)
        elif remove(choice.lower()) == "merge":
            title = "Merge sort"
            animation_generator = Mergesort(array, 0, element - 1)
        elif remove(choice.lower()) == "quick":
            title = "Quick sort"
            animation_generator = Quicksort(array, 0, element - 1)
        elif remove(choice.lower()) == "insertion":
            title = "Insertion sort"
            animation_generator = Insertionsort(array)
        elif remove(choice.lower()) == "recursivebubble":
            title = "Recursive bubble sort"
            n = len(array)
            animation_generator = RecursiveBubblesort(array, n)
        elif remove(choice.lower()) == "selection":
            title = "Selection sort"
            animation_generator = Selectionsort(array)
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

    user = input("Run again?(y/n): ")
    print("\n")
    if user.lower() == 'n':
        break