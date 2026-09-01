symbols = '$¢£¥€¤'
# Using listcomp to build the array
array = [ord(s) for s in symbols if ord(s) > 35]
print(array)
# Using map, filter and lambda to build the same array
array_2 = list(filter(lambda c: c > 35, map(ord, symbols)))
print(array_2)