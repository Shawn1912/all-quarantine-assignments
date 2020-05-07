List = [1, 'a', 0, False, True, '0']
filteredList = filter(None, List)
print('The filtered elements are:')
for element in filteredList:
    print(element)
