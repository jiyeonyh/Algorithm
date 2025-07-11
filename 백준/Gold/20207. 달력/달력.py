def add_count_plan(planner, a, b):
    for i in range(a, b + 1):
        planner[i] += 1


def compute_result(planner, end_date):
    result = 0
    max_plan = 0
    day_count = 0
    for i in range(1, end_date + 1):
        if planner[i] != 0:
            max_plan = max(max_plan, planner[i])
            day_count += 1
        else:
            result += day_count * max_plan
            max_plan = 0
            day_count = 0

    result += day_count * max_plan
    return result


def solve():
    n = int(input())
    planner = [0] * 366

    end_date = 0
    for _ in range(n):
        a, b = map(int, input().split())
        add_count_plan(planner, a, b)

        end_date = max(end_date, b)

    result = compute_result(planner, end_date)
    print(result)


solve()
