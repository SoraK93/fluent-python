import array

symbols = '$¢£¥€¤'

# generator expression is the single argument in a function call
tup = tuple(ord(symbol) for symbol in symbols)
print(tup)

# Array contructor takes two arguments, first argument defines the storage type
arr = array.array("I", (ord(symbol) for symbol in symbols))
print(arr)