# List Comprehension -> new_list = [new_item for item in old_list]

numbers = [1,2,3,4]
new_list = [n+1 for n in numbers] # List Comprehension
new_list2 = []

for n in numbers:
    new = n+1
    new_list2.append(new)

print(numbers)
print(new_list)
print(new_list2)

name = "Saksham"
name_list = [letter for letter in name]
print(name_list)

num_list = [n*2 for n in range(1,5)]
print(num_list)

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
short_list = [name for name in names if len(name)<=4]
print(short_list)

upper_list = [name.upper() for name in names if len(name)>=5]
print(upper_list)