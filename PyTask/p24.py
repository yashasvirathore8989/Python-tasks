brick_volume = 25 * 10 * 7.5
wall_volume = 2000 * 200 * 75
bricks = wall_volume / brick_volume
cost = (bricks / 1000) * 900
print("bricks needed:",bricks)
print("cost:", cost)