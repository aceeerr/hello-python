num =1
total = 0
num1 = input ("Enter a comma separated list of numbers: ")
num1 = [num**2 for num in range(5)]

total += num

print("sum of squares = {}".format(total))

