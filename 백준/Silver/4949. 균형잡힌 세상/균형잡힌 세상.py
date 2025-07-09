def is_balanced(line):
    pairs = {
        '(': ')',
        '[': ']'
    }

    stack = []

    for char in line:
        if char in pairs:
            stack.append(char)
        elif char in pairs.values():
            if not stack or char != pairs[stack.pop()]:
                return "no"

    return "yes" if not stack else "no"


def solve():
    while True:
        line = input()

        if line == ".":
            break
        else:
            result = is_balanced(line)
            print(result)


solve()
