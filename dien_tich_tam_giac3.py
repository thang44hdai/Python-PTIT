def area_of_triangle(x1, y1, x2, y2, x3, y3):
    # Tính diện tích của tam giác bằng công thức Heron
    a = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    b = ((x2 - x3) ** 2 + (y2 - y3) ** 2) ** 0.5
    c = ((x3 - x1) ** 2 + (y3 - y1) ** 2) ** 0.5
    s = (a + b + c) / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    return area


def main():
    N = int(input())  # Số lượng tam giác
    triangles = []

    for _ in range(N):
        x1, y1, x2, y2, x3, y3 = map(int, input().split())
        triangles.append((x1, y1, x2, y2, x3, y3))

    min_x = min(x for x1, _, x2, _, x3, _ in triangles for x in [x1, x2, x3])
    max_x = max(x for x1, _, x2, _, x3, _ in triangles for x in [x1, x2, x3])
    min_y = min(y for _, y1, _, y2, _, y3 in triangles for y in [y1, y2, y3])
    max_y = max(y for _, y1, _, y2, _, y3 in triangles for y in [y1, y2, y3])

    step = 0.01  # Kích thước bước cho lưới mạng, bạn có thể điều chỉnh tùy ý

    total_area = 0
    for x in range(int(min_x), int(max_x), int(step)):
        for y in range(int(min_y), int(max_y), int(step)):
            point_covered = False
            for triangle in triangles:
                x1, y1, x2, y2, x3, y3 = triangle
                area1 = area_of_triangle(x, y, x2, y2, x3, y3)
                area2 = area_of_triangle(x1, y1, x, y, x3, y3)
                area3 = area_of_triangle(x1, y1, x2, y2, x, y)
                triangle_area = area_of_triangle(x1, y1, x2, y2, x3, y3)

                if abs(triangle_area - (area1 + area2 + area3)) < 1e-6:
                    point_covered = True
                    break

            if point_covered:
                total_area += step * step

    print(f'{total_area:.6f}')


if __name__ == "__main__":
    main()
