num_of_elements = int(input("Enter the number of elements you want in the array: "))
list1 = []

for i in range(num_of_elements):
    element = int(input("Enter element : "))
    list1.append(element)   

# Check if all elements are same because sets do not count duplicates
if len(set(list1)) == 1:
    print(-1)
else:
    max_element = max(list1)
    list1.remove(max_element)       # remove largest
    second_max_element = max(list1) # second largest
    print(second_max_element)