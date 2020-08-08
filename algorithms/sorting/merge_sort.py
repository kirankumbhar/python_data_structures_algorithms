import math

"""
Pseudo code for Merge Sort

merge_sort(a, lb, ub):
    if lb < ub:
        mid = (lb + ub)/2
        merge_sort(a, lb, mid)
        merge_sort(a, mid+1, ub)
        merge(a, lb, mid, ub)

merge(a, lb, mid, ub):
    i = lb;
    j = mind+1;
    k=lb;
    b = []
    while(i <= mid && j <= ub) :
        if a[i] <= a[j]:
            b[k] = a[i]
            i += 1
        else:
            b[k] = a[j]
            j += 1
        k += 1

    if i > mid:
        while(j <= ub):
            b[k] = a[j];
            j += 1
            k += 1
    else:
        while(i <= mid):
            b[k] = a[j]
            i += 1
            k += 1
"""

def merge_sort(a, lb, ub):
    if lb < ub:
        mid = math.floor((lb + ub)/2)
        print(mid)
        merge_sort(a, lb, mid)
        merge_sort(a, mid+1, ub)
        merge(a, lb, mid, ub)

def merge(a, lb, mid, ub):
    i = lb
    j = mid + 1
    k=lb
    while (i <= mid) and (j <= ub):
        if a[i] <= a[j]:
            b.insert(a[i])
            i += 1
        else:
            b.insert(a[j])
            j += 1
        k += 1

    if i > mid:
        while(j <= ub):
            b.insert(a[j])
            j += 1
            k += 1
    else:
        while(i <= mid):
            b.insert(a[i])
            i += 1
            k += 1
    print(b)

b = list()
merge_sort([1, 6, 3, 7], 0 , 3)
