stack = []

stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.pop()

print(stack[::-1]) # 최상단 원소 ~ 최하단 원소
print(stack) # 최하단 원소 ~ 최상단 원소

