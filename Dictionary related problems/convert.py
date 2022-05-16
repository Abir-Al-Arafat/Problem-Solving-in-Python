# "Below are the two lists convert it into the dictionary",
# "keys = ['Ten', 'Twenty', 'Thirty']\n", "values = [10, 20, 30]\n", "Expected output:{'Ten': 10, 'Twenty': 20, 'Thirty': 30}"

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

zipped = dict(zip(keys, values))

print(zipped)

# "Use the inputs below and try to unzip them with unpacking method. Use zip function to unzip them
#     "coordinate = ['x', 'y', 'z']
#     "value = [3, 4, 5]
#     "Output:
#     "[('x', 3), ('y', 4), ('z', 5)]\n",
#     "c = ('x', 'y', 'z')\n",
#     "v = (3, 4, 5)"

coordinate = ['x', 'y', 'z']
value = [3, 4, 5]

# combining the values to make list of tuples
pack = list(zip(coordinate, value))
print(pack)

c, v = zip(*pack)  # putting aesterics to iterate over all the values

print(c)
print(v)
