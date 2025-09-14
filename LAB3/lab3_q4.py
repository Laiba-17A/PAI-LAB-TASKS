
l1= input("Enter first list separated by commas: ")
list1 = l1.split(",")

l2 = input("Enter second list separated by commas: ")
list2 = l2.split(",")
if len(list1) != len(list2):
    print("Error")
else:
    my_dict = dict(zip(list1, list2))
    print("The final dictionary is:", my_dict)
