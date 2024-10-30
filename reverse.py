def reverse(any):
    reverse_string = ""
    for i in any:
        reverse_string = i + reverse_string
    print(reverse_string)

reverse("Hello")

def reverse(any):
    reverse_string = []
    for i in any:
        reverse_string.insert(0,i)
    print(reverse_string)

reverse([3, 5, 7, 9])