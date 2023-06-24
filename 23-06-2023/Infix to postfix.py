def infix_to_postfix(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    stack = []
    output = []

    for char in expression:
        if char.isalnum():
            output.append(char)
        elif char == '(':
            stack.append('(')
        elif char == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()  # Discard '('
        else:
            while stack and stack[-1] != '(' and precedence[char] <= precedence.get(stack[-1], 0):
                output.append(stack.pop())
            stack.append(char)

    while stack:
        output.append(stack.pop())

    return ''.join(output)


# Driver code
while True:
    expression = input("Enter an infix expression (or 'exit' to quit): ")
    if expression.lower() == 'exit':
        print("Exiting...")
        break
    postfix = infix_to_postfix(expression)
    print("Postfix expression:", postfix)
