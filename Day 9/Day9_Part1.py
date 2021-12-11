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
        

def get_neighbor_values(x,y):
    neighbor_values_temp = []
    for i in range(-1,2):
        for j in range(-1,2):
            if (i == 0 and j == 0) or (i in [-1,1] and j in [-1,1]) :
                pass
            else:
                if (x+i, y+j) in height_map_dict.keys():
                    neighbor_values_temp.append(int(height_map_dict[(x+i, y+j)]))
                else:
                    pass
    return neighbor_values_temp

# %%
low_points = []
for k in height_map_dict.keys():
    neighbors = get_neighbor_values(k[0],k[1])
    current_value = height_map_dict[k]
    is_current_smallest = len([*filter(lambda x: x > current_value, neighbors)]) == len(neighbors)
    if is_current_smallest:
        low_points.append(current_value)
    else:
        pass



# %%
res = sum(low_points) + len(low_points)

# %%
