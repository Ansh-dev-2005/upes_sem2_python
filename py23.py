# sum of list without using sum method
# take list from user
L = []
for i in range(0,L):
    ele = int(input())
    L.append(ele)
print(L)

sum = 0
for i in L:
    sum += i
print(sum)


