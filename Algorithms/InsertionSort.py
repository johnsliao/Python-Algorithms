unsorted_list = [5,1,4,2,3]

def insertionSort(list):
    # Go through each element in the list, index x

        # keep index i = x
        # WHILE list[i] < list[i-1] and i>0
            # swap

    list_length = len(list)

    for x in range(list_length):
        i = x

        while i > 0 and list[i] < list[i-1]:
            temp = list[i-1]
            list[i-1] = list[i]
            list[i] = temp
            i -= 1

    return list

print insertionSort(unsorted_list)