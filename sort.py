
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

# How to sort array ascending order
array_one = [10, 22, 38, 27, 11]
temp = 0
print("Elements of the array: ")
#Display the elements of the array
for i in range(0, len(array_one)):
    print(array_one[i], end=" ")

#Sort the array in ascending order
for i in range(0, len(array_one)):
    for j in range(i+1, len(array_one)):
        if array_one[i] > array_one[j]:
            temp = array_one[i]
            array_one[i] = array_one[j]
            array_one[j] = temp

print()

#Display the elements of the array after_sorting
print("Elements of the array sorted in ascending order: ")
for i in range(0, len(array_one)):
    print(array_one[i], end=" ")



# How to sort array decending order
array = [11, 45, 80, 7, 9, 68]

tracker = 0

for i in range(0, len(array)):
    for j in range(i+1, len(array)):
        if array[i] < array[j]:
            tracker = array[i]
            array[i] = array[j]
            array[j] = tracker
print(array, end=" ")


print("Elements of the array sorted in ascending order: ")
for i in range(0, len(array)):
    print(array[i], end=" ")