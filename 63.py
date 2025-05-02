n = int(input("Enter a number: "))

i = 1
sum = 0
while i<=n:
    sum += i
    i += 1

print(sum)


product = 1
for i in range(1, n+1):
    product *= i
    
print(product)