# %%
with open('day5-data.txt') as file:
     lines = file.readlines()
     readings = []
     for line in lines:
         temp_line = line.split(' -> ')
         readings.append([temp_line[0].split(','),temp_line[1].split('\n')[0].split(',')])    

def gen_line(start, end):
    p1 = [int(start[0]),int(start[1])]
    p2 = [int(end[0]), int(end[1])]
    print(p1,p2)
    calcd_points = []
    calcd_points.append(start)
    xslope = 0
    yslope = 0
    
    if p2[0] > p1[0]:
        xslope = 1
    elif p2[0] < p1[0]:
        xslope = -1
    else:
        xslope = 0

    if p2[1] > p1[1]:
        yslope = 1
    elif p2[1] < p1[1]:
        yslope = -1
    else:
        yslope = 0
    print(xslope, yslope)
    
    calcd_points.append(p1)

    temp_point = p1

    while temp_point != p2:
        temp_point = [temp_point[0] + xslope, temp_point[1] + yslope]
        calcd_points.append(temp_point)
        
    return calcd_points
        
# %%
point_counts = {}
for valid_reading in readings:
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
