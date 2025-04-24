def merge(arr1,arr2):
    listSorted = []
    pointerA = arr1[0]
    pointerB = arr2[0]
    while len(arr1) > 0 and len(arr2) > 0:
        if pointerA < pointerB:
            listSorted.append(pointerA)
            pointerA = arr1[1]
            arr1.pop()
        elif pointerB < pointerA:
            listSorted.append(pointerB)
            pointerB = arr2[1]
            arr2.pop()


list1 = ["G","H"]
list2 = ["E","F"]
print(merge(list1,list2))