import stacks as s

test = s.stack()
test.push(3)
test.push(2)
test.push(1)

print(test.mini())
test.push(0)
print(test.mini())
test.pop()
print(test.mini())
test.pop()
print(test.mini())
test.push(5)
print(test.mini())
print(test.peek())



