#  SCAN Disk Scheduling Algorithm
n = int(input("Enter the number of sequences: "))

print("Enter the track sequence numbers (one by one):")

track = []
for i in range(n):
    track.append(int(input()))

head = int(input("Enter the head value: "))
direction = input("Enter direction(left/right): ").lower()
track.sort()

left = [x for x in track if x < head]
right = [x for x in track if x >= head]

result =[]
total_seek = 0
current = head

if direction == "right":
    order = right + left[::-1]
else:
    order = left[::-1] + right

for t in order:
    seek = abs(t - current)
    total_seek += seek
    result.append((t, seek))
    current = t

print(f"\n{"Next Track":<12} {"Seek Distance"}")
print("-" * 20)
for t, seek in result:
    print(f"{t:<12} {seek}")

print("-" * 20)
print(f"Total Seek Time:   {total_seek}")
# 0
# 13
# 41
# 50
# 63
# 89
# 100
