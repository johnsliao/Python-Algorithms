unsorted_list = [5,1,4,2,3]

def selectionSort(list):
    # Loop through each value in the list (index x)

        # Keep track of current min index, set to x by default

        # Loop through each value starting from x+1
            # IF list[y] < list[min]
                # min = y

        # IF min != x (new min found)
            # swap

    list_length = len(list)

    for x in range(list_length-1):
        min = x

        for y in range(x+1, list_length):
            if list[y] < list[min]:
                min = y

        if min != x:
            temp = list[x]
            list[x] = list[min]
            list[min] = temp

    return list

print selectionSort(unsorted_list)