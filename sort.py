
def sorting(array):
    tracker = 0

    for i in range(0, len(array)):
        for j in range(i+1, len(array)):
            if array[i] < array[j]:
                tracker = array[i]
                array[i] = array[j]
                array[j] = tracker
    #print(array, end=" ")
    # print(array)
    return array

def length(char):
    count = 0
    for i in char:
        count+=1
    return count
