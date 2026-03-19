from sys import maxsize

def create_stack():
    stack = []
    return stack
def empty(stack):
    if len(stack) == 0:
        return True
    else:
        return False
def push(stack, item):
    stack.append(item)
    print("item has been added to the stack", item)
def pop(stack):
    if empty(stack):
        return str(-maxsize - 1)
    else:
        return stack.pop()
def peek(stack):
    if empty(stack):
        return str(-maxsize - 1)
    else:
        return stack[-1]

stack = create_stack()

push(stack,12)
push(stack,13)
push(stack,16)

pop(stack)
peek(stack)
print(stack)