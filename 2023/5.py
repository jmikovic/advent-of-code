from collections import namedtuple

Map = namedtuple('Map', ['dest', 'source', 'length'])

with open('./2023/5.input', 'r') as f:
    lines = [line.strip() for line in f]

seeds = [int(n) for n in lines[0].split(':')[1].strip().split(' ')]
seed_to_soil = [Map(*(int(n) for n in line.split(' '))) for line in lines[3:28]]
soil_to_fertilizer = [Map(*(int(n) for n in line.split(' '))) for line in lines[30:39]]
fertilizer_to_water = [Map(*(int(n) for n in line.split(' '))) for line in lines[41:74]]
water_to_light = [Map(*(int(n) for n in line.split(' '))) for line in lines[76:122]]
light_to_temp = [Map(*(int(n) for n in line.split(' '))) for line in lines[124:159]]
temp_to_humidity = [Map(*(int(n) for n in line.split(' '))) for line in lines[161:181]]
humidity_to_loc = [Map(*(int(n) for n in line.split(' '))) for line in lines[183:]]

seeds_in_range = []
for i, _ in enumerate(seeds[::2]):
    seeds_in_range += list(range(seeds[2*i], seeds[2*i] + seeds[2*i+1]))

def get_lowest(seeds: list[int]) -> int:
    lowest_loc = 999999999999
    for seed in seeds:
        soil = seed
        for soil_map in seed_to_soil:
            if seed in range(soil_map.source, soil_map.source + soil_map.length):
                soil = soil_map.dest + (seed - soil_map.source)
                break
        fert = soil
        for fert_map in soil_to_fertilizer:
            if soil in range(fert_map.source, fert_map.source + fert_map.length):
                fert = fert_map.dest + (soil - fert_map.source)
                break
        water = fert
        for water_map in fertilizer_to_water:
            if fert in range(water_map.source, water_map.source + water_map.length):
                water = water_map.dest + (fert - water_map.source)
                break
        light = water
        for light_map in water_to_light:
            if water in range(light_map.source, light_map.source + light_map.length):
                light = light_map.dest + (water - light_map.source)
                break
        temp = light
        for temp_map in light_to_temp:
            if light in range(temp_map.source, temp_map.source + temp_map.length):
                temp = temp_map.dest + (light - temp_map.source)
                break
        hum = temp
        for hum_map in temp_to_humidity:
            if temp in range(hum_map.source, hum_map.source + hum_map.length):
                hum = hum_map.dest + (temp - hum_map.source)
                break
        loc = hum
        for loc_map in humidity_to_loc:
            if hum in range(loc_map.source, loc_map.source + loc_map.length):
                loc = loc_map.dest + (hum - loc_map.source)
                break
        lowest_loc = min(lowest_loc, loc)
    return lowest_loc
