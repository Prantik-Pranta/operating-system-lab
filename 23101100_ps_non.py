
#Priority Schedulling- Non Preemptive
n = int(input("Enter the number of process: "))
process = []

print("PID-AT-BT-Priority")
for i in range(n):
    PID, AT, BT, Priority = input().split()

    process.append([PID, int(AT), int(BT), int(Priority)])

process.sort(key=lambda x: x[1])

crt = 0
comp = 0
rslt = {}

visited = [False] * n

t_avr_tat = 0
t_avr_wt = 0

while comp < n:

    ready = []

    for i in range(n):
        if process[i][1] <= crt and not visited[i]:
            ready.append(i)


    if not ready:
        crt = min(
            p[1] for i, p in enumerate(process)
            if not visited[i]
        )
        continue

   
    i = min(
        ready,
        key=lambda i: (process[i][3], process[i][1])
    )

    curr = process[i]

    PID, AT, BT, Priority = curr

    crt += BT

    CT = crt
    TAT = CT - AT
    WT = TAT - BT

    t_avr_tat += TAT
    t_avr_wt += WT

    comp += 1
    visited[i] = True

    rslt[PID] = (PID, AT, BT, Priority, CT, TAT, WT)


print("\nPID\tAT\tBT\tPriority\tCT\tTAT\tWT")

for p in process:
    pid = p[0]
    r = rslt[pid]

    print(
        f"{r[0]}\t{r[1]}\t{r[2]}\t"
        f"{r[3]}\t\t{r[4]}\t{r[5]}\t{r[6]}"
    )


print("\nTotal Avrg TAT :", t_avr_tat / n)
print("Total Avrg WT :", t_avr_wt / n)
