number = 0
sum = 0

while sum < 200:
    number += 1
    sum += pow(number, 2)


print("Total: %s" % sum)
print("Last number: %s" % number)
