colors = ["black", "white"]
sizes = ["S", "M", "L"]

# Generates a list of tupes arraged by color, then size
tshirts = [(color, size) for color in colors for size in sizes]
print(tshirts)

# Resulting list is same as above listcomp
for color in colors:
    for size in sizes:
        print((color, size))

# Rearranges the item order by size then color
tshirts = [(color, size)
           for size in sizes
           for color in colors]
print(tshirts)
