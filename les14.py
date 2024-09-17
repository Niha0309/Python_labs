#for loop
for character in 'Python':
    print(character)

for item in ['EGG', 'RICE', 'OIL']:
    print(item)

for number in [1, 2, 3, 4, 5]:
    print(number)
for number in range (5,10):
    print(number)


# find bill using for loop
bills = [10, 30, 10,50]
total = 0
for bill in bills :
    total += bill
print(f"total bill : ${total}")
