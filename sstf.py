# SSTF - Shortest Seek Time First (Track numbers only)

n = int(input("Enter the number of sequences: "))

print("Enter the track sequence numbers (one by one):")
tracks = []
for i in range(n):
    tracks.append(int(input()))

h = int(input("Enter the initial head value: "))

remaining = tracks.copy()
result = []

total_seek = 0
current_head = h

while remaining:
    closest = min(remaining, key=lambda x: abs(x - current_head))

    seek = abs(closest - current_head)
    total_seek += seek

    result.append((closest, seek))

    current_head = closest
    remaining.remove(closest)

print(f"\n{"Next Track":<12}{"Seek Distance"}")
print("-" * 25)
for track, seek in result:
    print(f"{track:<12}{seek}")

print("-" * 25)
print(f"Total Seek Time:   {total_seek}")
