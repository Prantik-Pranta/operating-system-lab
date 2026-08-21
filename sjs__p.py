# SJF - Preemptive (Shortest Remaining Time First)
n = int(input("Enter the number of process: "))
process = []

print("PID-AT-BT")
for i in range(n):
    PID, AT, BT = input().split()
    
    process.append([PID, int(AT), int(BT), int(BT)])

process.sort(key=lambda x: x[1])

crt = 0      
comp = 0      
rslt = {}     

t_avr_tat = 0
t_avr_wt = 0

while comp < n:
    
    available = [p for p in process if p[1] <= crt and p[3] > 0]
    
    if not available:
        crt = min(p[1] for p in process if p[3] > 0)
        continue
       
    curr = min(available, key=lambda x: x[3])
       
    curr[3] -= 1
    crt += 1
        
    if curr[3] == 0:
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
