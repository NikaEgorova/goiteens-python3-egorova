names = ["Katya", "Max", "Oleksii", "Olesya", "Oleh", "Yaroslav", "Anastasiia"]
age = [25, 54, 18, 23, 45, 21, 21]
isPaid = [True, False, True, True, False, True, False]
Max_index = names.index("Max")
names.pop(Max_index)
ageMax = age[Max_index]
age.pop(Max_index)
Max_paid = isPaid[Max_index]
isPaid.pop(Max_index)
print(names)
print(age)
print(isPaid)
