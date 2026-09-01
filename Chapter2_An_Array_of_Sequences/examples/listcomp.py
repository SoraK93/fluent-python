# Build a list of Unicode code points from a string
symbols = '$¢£¥€¤'
codes = []
for symbol in symbols:
    codes.append(ord(symbol))
print(codes)

# Build a list of Unicode code points from a string, using a listcomp
symbols = '$¢£¥€¤'
codes = [ord(symbol) for symbol in symbols]
print(codes)
