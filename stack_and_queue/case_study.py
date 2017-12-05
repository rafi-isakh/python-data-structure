from stack import Stack

# Balance bracket checking
def check_brackets(statement):
    stack = Stack()

    for ch in statement:
        if ch in ('(', '{', '['):
            stack.push(ch)
        if ch in (')', '}', ']'):
            element = stack.pop()
        
            if element is '(' and ch is ')':
                continue
            elif element is '{' and ch is '}':
                continue
            elif element is '[' and ch is ']':
                continue
            else:
                return False

    if stack.size > 0:
        return False
    else:
        return True
