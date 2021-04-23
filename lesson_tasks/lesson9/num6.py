def print_list(my_list):
    print(my_list)


def print_new_list(my_list, new_name):
    my_list.append(new_name)
    print(my_list)


names = ["Ярослав", "Богдан", "Катя"]
new_name = "Євген"
print_list(names)
print_new_list(names, new_name)
