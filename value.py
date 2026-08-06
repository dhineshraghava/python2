number_count = int(input())

pos_count = 0
neg_count = 0
zero_count = 0
total_sum = 0

for i in range(number_count):
    num = int(input())
    total_sum += num
    
    if num > 0:
        pos_count += 1
    elif num < 0:
        neg_count += 1
    else:
        zero_count += 1

print(f"Positive Count: {pos_count}")
print(f"Negative Count: {neg_count}")
print(f"Zero Count: {zero_count}")
print(f"Total: {total_sum}")