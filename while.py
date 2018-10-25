# x=1
# total = 0
# while x < 100:
#     if x & 1:
#         print(x, end=" ")
#         total += x

#     x+= 1
# print (x ,"sum", total)


# for c in "hello!":
#     print(c)

# for x in range(5, 100):
#     if x % 2 == 0:
#         print(x, end=" ")
# print ()

numbers = []
for x in range(10):
    numbers.append(x)

print(numbers)

numbers2 = [x**2 for x in range(10)]
print(numbers2)