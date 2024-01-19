test = '[]{}()'
stack = []
pairs = {
    '(':')',
    '[':']',
    '{':'}'
}

# checks if its in the keys
for bracket in test:
    if bracket in pairs:
        stack.append(bracket)
    elif len(stack) == 0 or bracket != pairs[stack.pop()]:
        print(False)
    
    print(len(stack) == 0)