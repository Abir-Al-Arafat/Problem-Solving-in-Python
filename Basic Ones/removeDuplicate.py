# write a function that removes duplicate entries from a list

names = ['larry', 'curly', 'joe', 'adam', 'brian', 'larry', 'joe']


def removeDuplicate(names):
    unique_names = []
    for name in names:
        if name not in unique_names:
            unique_names.append(name)
    return unique_names


print(names)
print("after removing duplicates:", removeDuplicate(names))
