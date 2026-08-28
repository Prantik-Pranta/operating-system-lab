# P1 0 7
# P2 1 4
# P3 2 15
# P4 3 11
# P5 4 20
# P6 4 9

# RR -- Preemptive[Round Robin]
n = int(input("Enter the number of process: "))
process = []

print("PID-AT-BT")
for i in range(n):
    PID, AT, BT = input().split()
    
    process.append([PID, int(AT), int(BT), int(BT)])

process.sort(key=lambda x: x[1])

time_quant = int(input("Enter Time time_quant: "))

crt = 0
comp = 0
rslt = {}

queue = []
visited = [False] * n

t_avr_tat = 0
t_avr_wt = 0

while comp < n:
    for i in range(n):
        if process[i][1] <= crt and not visited[i] and process[i][3] > 0:
            queue.append(i)
            visited[i] = True           

    if not queue:
        crt = min(p[1] for i, p in enumerate(process)
                  if p[3] > 0 and not visited[i])
        continue

    i = queue.pop(0)
    curr = process[i]

    
    execution_time = min(time_quant, curr[3])

    curr[3] -= execution_time
    crt += execution_time

    
    for j in range(n):
        if process[j][1] <= crt and not visited[j] and process[j][3] > 0:
            queue.append(j)
            visited[j] = True

    
    if curr[3] > 0:
        queue.append(i)

    
    else:
        PID, AT, BT, _ = curr

        CT = crt
        TAT = CT - AT
        WT = TAT - BT

        t_avr_tat += TAT
        t_avr_wt += WT

        comp += 1

        rslt[PID] = (PID, AT, BT, CT, TAT, WT)


print("\nPID\tAT\tBT\tCT\tTAT\tWT")

for p in process:
    pid = p[0]
    r = rslt[pid]

    print(f"{r[0]}\t{r[1]}\t{r[2]}\t{r[3]}\t{r[4]}\t{r[5]}")


print("\nTotal Avrg TAT :", t_avr_tat / n)
print("Total Avrg WT :", t_avr_wt / n)