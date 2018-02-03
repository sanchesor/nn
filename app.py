import network as n

n1 = n.Network([2,2,1])

input = [1,2]
n1.forward(input)

print('input', input)
n1.show()
