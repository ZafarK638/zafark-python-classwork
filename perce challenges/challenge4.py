min_x1 = int(input())
min_y1 = int(input())
min_z1 = int(input())
sl1 = int(input())
min_x2 = int(input())
min_y2 = int(input())
min_z2 = int(input())
sl2 = int(input()) 

max_x1 = min_x1 + sl1
max_y1 = min_y1 + sl1
max_z1 = min_z1 + sl1

max_x2 = min_x2 + sl2
max_y2 = min_y2 + sl2
max_z2 = min_z2 + sl2

intersect_min_x = max(min_x1, min_x2)
intersect_min_y = max(min_y1, min_y2)
intersect_min_z = max(min_z1, min_z2)

intersect_max_x = min(max_x1, max_x2)
intersect_max_y = min(max_y1, max_y2)
intersect_max_z = min(max_z1, max_z2)

width = max(0, intersect_max_x - intersect_min_x)
depth = max(0, intersect_max_y - intersect_min_y)
height = max(0, intersect_max_z - intersect_min_z)

print(width*depth*height)
