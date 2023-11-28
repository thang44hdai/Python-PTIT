import numpy as np
from collections import deque

# Hàm kiểm tra xem một vị trí có hợp lệ trên bàn cờ hay không
def is_valid(x, y):
    return 0 <= x < 4 and 0 <= y < 4

# Hàm tạo danh sách các bước di chuyển
def create_move_sequence(parents, start, end):
    sequence = []
    current = end
    while current != start:
        sequence.append(current)
        current = parents[current]
    sequence.reverse()
    return sequence

# Đọc trạng thái xuất phát và trạng thái đích
start_state = []
for _ in range(4):
    row = list(map(int, input().split()))
    start_state.append(row)

end_state = []
for _ in range(4):
    row = list(map(int, input().split()))
    end_state.append(row)

# Biến đổi trạng thái bàn cờ thành ma trận numpy để dễ dàng xử lý
start_state = np.array(start_state)
end_state = np.array(end_state)

# Tìm vị trí của quân cờ trong trạng thái xuất phát và trạng thái đích
start_pos = np.argwhere(start_state)
end_pos = np.argwhere(end_state)

# Tạo danh sách kết quả
result = []

# Sử dụng BFS để tìm đường đi ngắn nhất
visited = set()
queue = deque()
parents = {}

queue.append(tuple(start_pos[0]))
visited.add(tuple(start_pos[0]))

while queue:
    current = queue.popleft()
    if current == tuple(end_pos[0]):
        break

    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        new_x, new_y = current[0] + dx, current[1] + dy
        if is_valid(new_x, new_y) and (new_x, new_y) not in visited:
            queue.append((new_x, new_y))
            visited.add((new_x, new_y))
            parents[(new_x, new_y)] = current

# Tạo danh sách bước di chuyển
move_sequence = create_move_sequence(parents, tuple(start_pos[0]), tuple(end_pos[0]))

# Đếm số bước di chuyển
num_moves = len(move_sequence)

# Thêm các bước di chuyển vào danh sách kết quả
for i in range(num_moves - 1):
    x1, y1 = move_sequence[i]
    x2, y2 = move_sequence[i + 1]
    result.append((x1 + 1, y1 + 1, x2 + 1, y2 + 1))

# In kết quả
print(num_moves)
for move in result:
    print(*move)
