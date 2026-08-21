# shortest job first non preemtive & preemtive
# SJF - Non Preemptive

n = int(input("Enter the number of process: "))

process = []

print("PID-AT-BT")

for i in range(n):
    PID, AT, BT = input().split()
    process.append((PID, int(AT), int(BT)))

process.sort(key=lambda x: x[1])

crt = 0
comp = 0
t_avr_tat = 0
t_avr_wt = 0
rslt = []

while comp < n:
    
    list= []
    for p in process:
        if p[1] <= crt and p[0] not in [r[0] for r in rslt]:
            list.append(p)
    
    if not list:
        crt = min(p[1] for p in process if p[0] not in [r[0] for r in rslt])
        continue


    currt = min(list, key=lambda x: x[2])

    PID, AT, BT = currt

    CT = crt + BT
    TAT = CT - AT
    WT = TAT - BT

    crt = CT
    comp += 1

    t_avr_tat += TAT
    t_avr_wt += WT


    rslt.append((PID, AT, BT, CT, TAT, WT))


print("\nPID\tAT\tBT\tCT\tTAT\tWT")

for i in rslt:
    print(i[0], "\t", i[1], "\t", i[2], "\t",
          i[3], "\t", i[4], "\t", i[5])

print("Total Avrg TAT : ", t_avr_tat / n)
print("Total Avrg WT  : ", t_avr_wt / n)