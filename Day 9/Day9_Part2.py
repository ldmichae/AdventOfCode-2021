# %%
height_map = []
with open('day9-data.txt', 'r') as file:
    lines = file.readlines();   
    for line in lines:
        height_map.append(list(line.strip('\n')))

height_map_dict = {}
for row in range(len(height_map)):
    for reading in range(len(height_map[row])):
        height_map_dict[(reading, row)] = int(height_map[row][reading])
        
def get_neighbor_indices(x,y):
    neighbor_indices_temp = []
    for i in range(-1,2):
        for j in range(-1,2):
            if (i == 0 and j == 0) or (i in [-1,1] and j in [-1,1]) :
                pass
            else:
                if (x+i, y+j) in height_map_dict.keys():
                    neighbor_indices_temp.append((x+i, y+j))
                else:
                    pass
    return neighbor_indices_temp

def delineate_basin(val):
    searched.append(val)
    basin_indices = [val]
    neighbors_to_search = get_neighbor_indices(val[0],val[1])
    neighbors_to_search = [i for i in neighbors_to_search if height_map_dict[i] != 9 and i != val and i not in searched]
    basin_indices.extend(neighbors_to_search)
    while len(neighbors_to_search) > 0:
        for i in neighbors_to_search:
            basin_indices.extend(delineate_basin(i))
            neighbors_to_search.remove(i)

    return list(set(basin_indices))

basins = []
searched = []

for k in list(height_map_dict.keys()):
    if height_map_dict[k] == 9 or any(k in i for i in basins if isinstance(i, list)):
        pass
    else:
        basins.append(delineate_basin(k))

sizes = [len(x) for x in basins]

