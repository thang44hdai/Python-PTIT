from shapely.geometry import Polygon, Point

# Đọc số lượng tam giác
N = int(input())

# Tạo một Polygon để biểu diễn diện tích tổng của tất cả tam giác
total_area = Polygon()

for i in range(N):
    x1, y1, x2, y2, x3, y3 = map(int, input().split())
    # Tạo Polygon cho tam giác thứ i
    triangle = Polygon([(x1, y1), (x2, y2), (x3, y3)])
    # Thêm Polygon của tam giác thứ i vào diện tích tổng
    total_area = total_area.union(triangle)

# Tạo một Polygon để biểu diễn hình vuông giới hạn
boundary = Polygon([(-10**6, -10**6), (-10**6, 10**6),
                   (10**6, 10**6), (10**6, -10**6)])

# Tính diện tích bị che phủ
covered_area = total_area.intersection(boundary).area


print("{:.6f}".format(covered_area))
