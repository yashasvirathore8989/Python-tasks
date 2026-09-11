floor_length = 200
floor_width = 400
tile_length = 5
tile_width = 8
floor_area = floor_length * floor_width
tile_area = tile_length * tile_width
tiles = floor_area / tile_area
print("tiles required:",int(tiles))