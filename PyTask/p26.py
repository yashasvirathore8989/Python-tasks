length = 120
breadth = 2.4
brick_length = 0.24
brick_breadth = 0.15
path_area = length * breadth
brick_area = brick_length * brick_breadth
bricks = path_area / brick_area
print("bricks required:",int(bricks))