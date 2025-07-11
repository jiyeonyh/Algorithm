def find_empty_row(planner, a, b):
    for i, row in enumerate(planner):
        if not any(row[a:b + 1]):
            return i
    return -1


def fill_planner(planner, row_index, a, b):
    new_row = planner[row_index][:]
    for i in range(a, b + 1):
        new_row[i] = True
    planner[row_index] = new_row
    return planner


def compute_result(planner, n):
    total_area = 0
    current_height = 0
    current_width = 0

    for day in range(1, 366):
        has_schedule = False
        max_row = 0

        for row in range(n):
            if planner[row][day]:
                has_schedule = True
                max_row = max(max_row, row + 1)

        if has_schedule:
            current_width += 1
            current_height = max(current_height, max_row)
        else:
            if current_width > 0:
                total_area += current_height * current_width
                current_height = 0
                current_width = 0

    if current_width > 0:
        total_area += current_height * current_width

    return total_area


def solve():
    n = int(input())
    planner = [[False] * 366 for _ in range(n)]
    schedule = []

    for _ in range(n):
        a, b = map(int, input().split())
        schedule.append((a, b))

    schedule.sort(key=lambda x: (x[0], -x[1]))

    for a, b in schedule:
        empty_row = find_empty_row(planner, a, b)
        planner = fill_planner(planner, empty_row, a, b)

    result = compute_result(planner, n)
    print(result)


solve()
