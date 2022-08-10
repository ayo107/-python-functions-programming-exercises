names = ['John', 'Kenny', 'Tom', 'Bob', 'Dilan']
# CREATE YOUR FUNCTION HERE
def sort_names(names):
    names = ['John', 'Kenny', 'Tom', 'Bob', 'Dilan']
    return names.sort()



print(sort_names(names))

names = ['John', 'Kenny', 'Tom', 'Bob', 'Dilan']

names.sort()
print('List in Ascending Order: ', names)

names.sort(reverse=True)
print('List in Descending Order: ', names)
