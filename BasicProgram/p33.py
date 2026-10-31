length = 30
breadth = 20
path1 = 3
path2 = 4
garden_area = length * breadth
paths_area = (length * path1) + (breadth * path2) - (path1 * path2)
usable_area = garden_area - paths_area
print("usable area:", usable_area)