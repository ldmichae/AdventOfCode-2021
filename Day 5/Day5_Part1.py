# %%
with open('day5-data.txt') as file:
     lines = file.readlines()
     readings = []
     for line in lines:
         temp_line = line.split(' -> ')
         readings.append([temp_line[0].split(','),temp_line[1].split('\n')[0].split(',')])    

def gen_line(start, end):
    start = [int(start[0]),int(start[1])]
    end   = [int(end[0]), int(end[1])]
    print(start,end)
    calcd_points = []
    calcd_points.append(start)
    if start[0] == end[0]:   ##horizontal line
        p1 = start[1]
        p2 = end[1]
        for i in range(min(p1,p2) + 1, max(p1,p2)):
            calcd_points.append([start[0], i])
    else:                    ##vertical line
        p1 = start[0]
        p2 = end[0]
        for i in range(min(p1,p2) + 1, max(p1,p2)):
            calcd_points.append([i, end[1]])
    calcd_points.append(end)
    return calcd_points
        
# %%
valid_readings = []
for reading in readings:
    if (int(reading[0][0]) == int(reading[1][0]) or int(reading[0][1]) == int(reading[1][1])):
        valid_readings.append(reading)
    else:
        pass

point_counts = {}
for valid_reading in valid_readings:
    points_crossed = gen_line(valid_reading[0],valid_reading[1])
    for point in range(len(points_crossed)):
        point = points_crossed[point]
        if str(point) not in list(point_counts.keys()):
            point_counts[str(point)] = 1
        else:
            point_counts[str(point)] += 1
# %%
result = 0
for i,j in point_counts.items():
    if j > 1:
        result +=1
# %%
