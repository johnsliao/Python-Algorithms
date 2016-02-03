unsorted_list = [5,1,4,2,3]

def bubbleSort(list):
    done = False

    # WHILE list is unsorted
        # set done to True by default

        # FOR each index i in length of list-1
            # IF list[i] > list[i+1]:
                # swap
                # set done to False

    while not done:
        done = True

        for i in range(len(unsorted_list)-1):
            if list[i] > list[i+1]:
                t = list[i]
                list[i] = list[i+1]
                list[i+1] = t

                done = False

    return list

print bubbleSort(unsorted_list)