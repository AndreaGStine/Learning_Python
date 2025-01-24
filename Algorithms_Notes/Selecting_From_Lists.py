'''
So we can sort lists, but how might we find the nth item in the sorted list?

There is a class of slower answers: First, sort the entire list, then simply choose the nth item in that list
But is there any faster approach?
Yes! Yes there is. The following algorithms explore this.
'''
import Sorting_Lists as sl

def sort_first(l,n):
    #Can replace sl.heap_sort with any of the other sorting algorithms in Sorting_Lists
    sorted = sl.heap_sort(l)
    return sorted[n]

def selection_sort_flavor(l,n):
    eligible = l
    i = 0
    j = 0
    while True:
        eligible.pop()
