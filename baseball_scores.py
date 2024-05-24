
def calculate_scores(operations):
    stack = []

    for op in operations:
        if op == '+':
            stack.append(stack[-2] + stack[-1])
        elif op == 'D':
            stack.append(2 * stack[-1])
        elif op == 'C':
            stack.pop()
        else:
            stack.append(int(op))

    return sum(stack)


ops = ["5","2","C","D","+"]

print(calculate_scores(ops))