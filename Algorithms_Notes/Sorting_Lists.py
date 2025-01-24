'''
All algorithms below are attempts at solving a common problem: Putting a list in a correct order, from smallest to largest
Input: A list of items and a natural ordering of those items by which one may say one
item is less than another (ie items in the list implicitly are equipped with a total ordering)
Output: The items listed in order, from smallest to largest

The following algorithms are implemented, in order:
Selection sort
Insertion sort
Merge sort
Quick sort
Quick sort with checking
Quick sort using Hoare's inversions method for pivoting
Heap sort

All have been written by myself personally, although many were written in reference to pseudocode found online.
'''

import math
import numpy
import time
import random
import heapq

#Selection sort algorithm for sorting a list:
#Finds smallest element in the list
def find_smallest(l):
    if l == []:
        return None
    smallest = [0, 0]
    for i in range(0,len(l)):
        if i == 0:
            smallest = [l[0],0]
        elif l[i] <= smallest[0]:
            smallest = [l[i],i]
    return smallest

def selection_sort(l):
    #Common to all implementations of these sorting algorithms: If the list is trivially short, just return the list itself.
    if len(l) == 0 or len(l) == 1:
        return l
    #Otherwise, construct a sorted list, and one-by-one remove the smallest element from the unsorted list.
    unsorted = list(l)
    sorted = []
    while unsorted != []:
        smallest = find_smallest(unsorted)
        sorted.append(smallest[0])
        unsorted.pop(smallest[1])

    return sorted



#Insert sort algorithm for sorting a list:
#Counts how many items are smaller than or equal to a given item in the list
def find_location(l,n):
    loc = 0
    for i in range(0,len(l)):
        if l[i] <= n:
            loc += 1
    return loc

def insert_sort(l):
    if len(l) == 0 or len(l) == 1:
        return l
    unsorted = list(l)
    sorted = []

    #Inserts item into the kth index of the sorted list where k is the number of items smaller than or equal to it
    #Accommodates equalities by inserting the item rather than replacing a 'None' in a pre-indexed list
    for x in unsorted:
        sorted.insert(find_location(sorted,x),x)

    return sorted



#Merge sort algorithm for sorting a list:
#Input of merge: Two lists, assumed to already be sorted
#Output of merge: One list consisting of items of the two original lists, sorted as compared between lists.
def merge(l,r):
    result = []
    left, right = list(l), list(r)
    #Compare an item of the left list to an item on the right. Append the smaller item. Repeat.
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            result.append(left[0])
            left.pop(0)
        else:
            result.append(right[0])
            right.pop(0)
    #Leftovers get stuck at the end.
    while len(left) > 0:
        result.append(left[0])
        left.pop(0)
    while len(right) > 0:
        result.append(right[0])
        right.pop(0)

    return result

def merge_sort(l):
    #Base
    if len(l) == 1 or len(l) == 0:
        return l

    #Sort each half-size list, assemble by sorting between lists
    m2 = math.floor(len(l) / 2)
    left = merge_sort(l[:m2])
    right = merge_sort(l[m2:])

    return merge(left,right)



#Quick sort algorithm for sorting a list:
#Most basic pivot: Indexed at -1, each item is compared to the pivot and sorted to be on either the left or right of it.
def pivot(l):
    unpivoted = list(l)
    #r = random.randint(0,len(unpivoted)-1)
    p = unpivoted.pop(-1)
    pivoted = [p]
    q = 0
    for i in unpivoted:
        if i <= p:
            pivoted.insert(0,i)
            q += 1
        else:
            pivoted.append(i)
    return (pivoted, q)

#The algorithm: Pick the last element as pivot, sort items to either side of it, and then repeat on each side
def quick_sort(l):
    if len(l) == 1 or len(l) == 0:
        return l
    p = pivot(l)

    q = quick_sort(p[0][:p[1]])
    q.extend(quick_sort(p[0][p[1]:]))
    return q


#Introducing a check-if-done feature for mostly-sorted lists
def is_sorted(l):
    for i in range(0,len(l)-1):
        if l[i] > l[i+1]:
            return False
    return True

#An attempt to make quick sort quicker by introducing an nlog(n) checker if the list (or a sublist) is already sorted
#To hopefully reduce computations.
#It seems to sometimes be a little slower, but often either a little or significantly faster
def quick_sort_checking(l):
    if len(l) == 1 or len(l) == 0:
        return l
    p = pivot(l)
    if is_sorted(p[0]):
        return p[0]

    q = quick_sort_checking(p[0][:p[1]])
    q.extend(quick_sort_checking(p[0][p[1]:]))
    return q


#Quick sort algorithm using Hoare's pivoting method:
#Brief Googling yielded that this is actually the fastest way to swap list items
def swap(l,i,j):
    c = l[i]
    l[i] = l[j]
    l[j] = c

#Hoare pivot method: Start at the low and high end, specified in the inputs, of your list, and choose
#The middle item as a pivot. Move inwards, comparing each item to the middle item until there's an inversion:
#Two elements, one greater than the pivot on the left and less than the pivot on the right
#I'm not totally sure why we'd want to count inversions for reasons other than sorting,
#but a quick modification of the pivot part of this algorithm would let us do that.
def hoare_pivot(l, lo, hi):
    #p is the pivot
    p = l[(hi - lo)//2 + lo]
    #The i and j are called 'pointers'
    i = lo - 1
    j = hi + 1

    while True:
        #Continue to move i and j forward automatically after a swap happens
        i += 1
        j -= 1
        #Move i and j forward until an eligible swap is found
        while (l[i] < p):
            i += 1
        while (l[j] > p):
            j -= 1
        #If the pointers move past each other, all eligible swaps have happened and so the loop may end,
        #Returning the new location of the pivot p
        if (i >= j):
            return j
        swap(l,i,j)

#Iterate over all sub-lists to either side of a given pivot until the sub-lists are too fine-grained to not be already sorted
def hoare_sort(l, lo, hi):
    if (lo < hi):
        p = hoare_pivot(l, lo, hi)
        hoare_sort(l, lo, p)
        hoare_sort(l, p + 1, hi)

#Since the convention for all my other sorting algorithms has been to have a single input of a list, this
#function specifies the inputs for the Hoare quick sort
def hoare_quick_sort(l):
    hoare_sort(l,0,len(l)-1)
    return list(l)



#Heap sort algorithm for sorting a list:
#This one's scarily-simple because it uses the architecture of heaps, and is similar to selection sort:
#The first item in a heap is the smallest, and heaps can efficiently find a new first item, meaning a new smallest item,
#So turn your list into a heap and then repeatedly remove the first item! Donezo.
#I must be doing something kinda inefficient with the quicksorts because this is way faster than Hoare's quick sort
def heap_sort(l):
    h = list(l)
    heapq.heapify(h)
    sorted = []
    while h != []:
        s = heapq.heappop(h)
        sorted.append(s)
    return sorted

#Two other important sorting algorithms: Counting sort and Radix sort. I'm not doing them, though
#Because I've been advised that sorting algorithms is a very deep rabbit hole that newby programmers can fall down.

def compare_times(n):
    l = numpy.random.rand(n)
    start_time = time.time()
    selection_sort(l)
    print('Selection sort took: ', time.time() - start_time)
    start_time = time.time()
    insert_sort(l)
    print('Insert sort took: ', time.time() - start_time)
    start_time = time.time()
    merge_sort(l)
    print('Merge sort took: ', time.time() - start_time)
    start_time = time.time()
    quick_sort(l)
    print('Quick sort took: ', time.time() - start_time)
    start_time = time.time()
    quick_sort_checking(l)
    print('Quick sort checking took: ', time.time() - start_time)
    start_time = time.time()
    hoare_quick_sort(l)
    print('Hoare quick sort took: ', time.time() - start_time)
    start_time = time.time()
    heap_sort(l)
    print('Heap sort took: ', time.time() - start_time)

if __name__ == "__main__":
    compare_times(4000)