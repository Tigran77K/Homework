a1, b1, a2, b2 = map(float, input().split())
start_intersection = max(a1, a2)
end_intersection = min(b1, b2)
if start_intersection > end_intersection:
    intersection_length = 0
else:
    intersection_length = end_intersection - start_intersection
print(intersection_length)


