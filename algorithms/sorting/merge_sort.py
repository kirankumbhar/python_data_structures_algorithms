"""
Pseudo code for Merge Sort

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