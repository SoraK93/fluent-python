colors = ["black", "white"]
sizes = ["S", "M", "L"]

# The generator expression yields items one by one; a list with all siz T-shirt variations is never produced here.
for tshirt in (f'{c} {s}' for c in colors for s in sizes):
    print(tshirt)