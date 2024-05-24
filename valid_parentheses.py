
def is_valid(s):
    stack = []
    close_to_open_map = { 
        '}': '{', 
        ')': '(', 
        ']': '[' 
    }

    for c in s:
        if c in close_to_open_map:
            if stack and stack[-1] == close_to_open_map[c]:
                stack.pop()
            else:
                return False
        else:
            stack.append(c)

    if not stack:
        return True
    else:
        return False
    

s = '()'
print(is_valid(s))
s = '(){}[]'
print(is_valid(s))