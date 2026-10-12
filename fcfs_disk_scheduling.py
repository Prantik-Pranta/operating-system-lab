n = int(input("Enter number of requests: "))
requests = list(map(int, input("Enter request sequence: ").split()))
head = int(input("Enter head position: "))

total_seek = 0
current = head

for i in requests:
    if i > current:
        total_seek += i - current
    else:
        total_seek += current - i

    current = i

print("Total No. of Seek Operations:", total_seek)
# 176 51 50 40 39 100
