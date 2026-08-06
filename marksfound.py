limit = int(input())
target = int(input())

count = 0
total = 0
found = False

for i in range(1,limit):
    if i % 3 == 0:
        count = count+1
        total = total+i
print(f"Count: {count}")
print(f"Sum: {total}")
print(f"Target Found: No ")