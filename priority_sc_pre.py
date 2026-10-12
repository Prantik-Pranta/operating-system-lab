# Priority Scheduling -- Preemptive

n = int(input("Enter the number of process: "))
process = []

print("PID-AT-BT-Priority")
for i in range(n):
    PID, AT, BT, Priority = input().split()

    process.append([PID,int(AT),int(BT),int(Priority),int(BT)])

process.sort(key=lambda x: x[1])
time_quant = int(input("Enter Time Quant:"))

crt = 0
comp = 0
rslt = {}

t_avr_tat = 0
t_avr_wt = 0

visited = [False] * n

while comp < n:  
    list = []
    for i in range(n):
        if process[i][1] <= crt and process[i][4] > 0:
            list.append(i)

    if not list:
        crt = min(p[1] for i, p in enumerate(process) if p[4] > 0)
        continue
  
    i = min(list,key=lambda i: (process[i][3], process[i][1]))

    curr = process[i]

    curr[4] -= time_quant
    crt += time_quant

    if curr[4] == 0:

        PID, AT, BT, Priority, _ = curr

        CT = crt
        TAT = CT - AT
        WT = TAT - BT

        t_avr_tat += TAT
        t_avr_wt += WT

        comp += 1

        rslt[PID] = (PID,AT,BT,Priority,CT,TAT,WT)


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
