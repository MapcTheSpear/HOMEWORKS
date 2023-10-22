def selection_sort(alist):
    for i in range(0, len(alist) - 1):
        minimum = i
        for j in range(i + 1, len(alist)):
            if alist[j] < alist[minimum]:
                minimum = j
        alist[i], alist[minimum] = alist[minimum], alist[i]
    return alist
unsorted_list = [12, 54, 14, 63, 178, 98, 1, 0]
selection_sort(unsorted_list)
print(unsorted_list)

def binary_search(list1, N):
    ResultOk = False
    first = 0
    last = len(list1)-1
    while first <= last and not ResultOk:
        middle = (first + last) // 2
        val = list1[middle]
        if val == N:
          ResultOk = True
        if val > N:
            last = middle - 1
        else:
            first = middle + 1
    return ResultOk

llist = [1, 2, 3, 4 ,5 ,6 ,7, 8, 9, 9, 10, 12 ,123, 900]
value = 10
result = binary_search(llist, value)
if result:
    print(f'Element {value} is found!')
else:
    print(f'Element {value} not found!')
