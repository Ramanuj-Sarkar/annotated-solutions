import math

def closest_pair(points):
    """
    Finds the closest pair of points using the O(n log n) divide-and-conquer algorithm.
    """
    # Sort points by x-coordinate and y-coordinate once
    points_sorted_x = sorted(points, key=lambda p: p[0])
    points_sorted_y = sorted(points, key=lambda p: p[1])
    
    return find_closest_recursive(points_sorted_x, points_sorted_y)[1]

def find_closest_recursive(points_x, points_y):
    """
    Recursive function to find the closest pair.
    """
    n = len(points_x)
    
    # Base case: brute force for small numbers of points
    if n <= 3:
        min_dist_sq = float('inf')
        closest_points = ()
        for i in range(n):
            for j in range(i + 1, n):
                p1 = points_x[i]
                p2 = points_x[j]
                d_sq = (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2
                
                if d_sq < min_dist_sq:
                    min_dist_sq = d_sq
                    closest_points = (p1, p2)
        
        return min_dist_sq, closest_points

    # Divide
    mid = n // 2
    mid_point = points_x[mid]
    
    # Split the sorted lists for recursion
    left_x = points_x[:mid]
    right_x = points_x[mid:]
    
    left_y = []
    right_y = []
    for p in points_y:
        if p[0] <= mid_point[0]:
            left_y.append(p)
        else:
            right_y.append(p)
    
    # Conquer: recurse on left and right halves
    d1_sq, pair1 = find_closest_recursive(left_x, left_y)
    d2_sq, pair2 = find_closest_recursive(right_x, right_y)
    
    # Combine: take the minimum distance found so far
    min_dist_sq, closest_pair_found = (d1_sq, pair1) if d1_sq < d2_sq else (d2_sq, pair2)
    
    # Create a strip of points within the current minimum distance 'delta'
    strip = []
    delta_sq = min_dist_sq
    for p in points_y:
        if (p[0] - mid_point[0])**2 < delta_sq:
            strip.append(p)
            
    # Check points in the strip
    # We only need to check up to 7 subsequent points in the y-sorted strip
    for i in range(len(strip)):
        for j in range(i + 1, min(i + 8, len(strip))):
            s1 = strip[i]
            s2 = strip[j]
            d_sq = (s1[0] - s2[0])**2 + (s1[1] - s2[1])**2
            if d_sq < min_dist_sq:
                min_dist_sq = d_sq
                closest_pair_found = (strip[i], strip[j])
                delta_sq = d_sq # Update delta_sq for subsequent checks
                
    return min_dist_sq, closest_pair_found
