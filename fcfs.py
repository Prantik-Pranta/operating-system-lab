#fcfs
n = int(input("Enter the number of process: "))

process = list()

print("PID-AT-BT")

for i in range(n):
    PID , AT, BT = input().split()
    process.append((PID,int(AT),int(BT)))

process.sort(key = lambda x: x[1])

crt = 0
t_avr_tat = 0
t_avr_wt = 0
result = list()

for i in process:
    if crt < i[1]:
        crt=i[1]
    CT = crt + i[2]
    TAT = CT - i[1]
    WT = TAT - i[2]

    crt = CT
    t_avr_tat += TAT
    t_avr_wt += WT

    result.append((i[0],i[1],i[2], CT, TAT, WT))

for i in result:
    print(i)

print("Total Avrg TAT : ",t_avr_tat/n)
print("Total Avrg WT : ",t_avr_wt/n)