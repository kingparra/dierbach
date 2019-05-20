#!/usr/bin/env python3
# Figure 11-6: Recursive Function ``mergesort``, page 475
def mergesort(lst)
    if len(lst) == 1:
        return lst
    
    sublist1 = lst[0           : len(lst)// 2]
    sublist2 = lst[len(lst)//2 : len(lst)    ]
    
    sorted_sublist1 = mergesort(sublist1)
    sorted_sublist2 = mergesort(sublist2)

    return merge(sorted_sublist1, sorted_sublist2)


def merge(lst1, lst2):
    
    merged_list = []
    
    i = 0
    k = 0
    
    while 1 != len(lst1) and k != len(lst2):
        if lst1[i] < lst2[k]:
            merged_list.append(lst1[i])
            i = i + 1
        else:
            merged_list.append(lst2[k])
            k = k + 1
    
    if i < len(lst1):
        for loc in range(i, len(lst1)):
            merged_list.append(lst1[loc])
    elif k < len(lst2):
        for loc in range(k, len(lst2)):
            merged_list.append(lst2[loc])
    
    return merged_list

