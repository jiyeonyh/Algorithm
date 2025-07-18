import itertools

def calculate(numbers, operators):
    result = numbers[0]
    for i in range(1, len(numbers)):
        if operators[i - 1] == '+':
            result += numbers[i]
        elif operators[i - 1] == '-':
            result -= numbers[i]
        elif operators[i - 1] == '*':
            result *= numbers[i]
        else:
            if result < 0:
                result = -(-result // numbers[i])
            else:
                result //= numbers[i]
    return result

def generate_operators(op_counts, symbols=['+', '-', '*', '/']):
    return [op for count, op in zip(op_counts, symbols) for _ in range(count)]

def find_max_min(numbers, op_permutations):
    results = [calculate(numbers, operators) for operators in op_permutations]
    return max(results), min(results)

def solve():
    n = int(input())
    numbers = list(map(int, input().split()))
    op_count = list(map(int, input().split()))

    op_arr = generate_operators(op_count)
    op_permutations = set(itertools.permutations(op_arr, n-1))
    max_result, min_result = find_max_min(numbers, op_permutations)

    print(max_result)
    print(min_result)


solve()