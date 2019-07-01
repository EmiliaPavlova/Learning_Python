square_side = int(input())
tile_width = float(input())
tile_length = float(input())
bench_width = int(input())
bench_length = int(input())
time = 0.2

square_area = square_side ** 2
bench_area = bench_width * bench_length
area_to_cover = square_area - bench_area
tile_area = tile_width * tile_length

required_tiles = round(area_to_cover / tile_area, 2)
required_time = round(required_tiles * time, 2)
print(required_tiles)
print(required_time)
