numbers = {}

numbers["one"] = 1
numbers["two"] = 2
numbers["three"] = 3
numbers[4] = "four"
numbers[5] = 5.5

print(numbers[4])
print(numbers["three"])

print(numbers.get(5))

for k,v in numbers.items():
    print(k,v)