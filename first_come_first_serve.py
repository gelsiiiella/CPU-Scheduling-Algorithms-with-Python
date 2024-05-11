from tabulate import tabulate

process=int(input('Input number of processes: '))

burstTime=[]
wt= [0] * process
tat= [0] * process

for i in range(process):
    burst=int(input("Enter burst time for {}:".format(i+1)))
    burstTime.append(burst)

    if i > 0:
        wt[i] = burstTime[i-1]+wt[i-1]
    tat[i] = wt[i]+ burstTime[i]

    avg_wt=sum(wt)/process
    avg_tat=sum(tat)/process

headers= ['Processes','Burst Time','Turn-Around Time','Waiting Time']
data = [[i+1,burstTime[i],tat[i],wt[i]]for i in range(process)]

print(tabulate(data,headers=headers,tablefmt='grid'))

print("Average Turnaround Time:",round(avg_tat))
print("Average Waiting Time:",round(avg_wt))