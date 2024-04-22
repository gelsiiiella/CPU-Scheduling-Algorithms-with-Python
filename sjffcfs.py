from tabulate import tabulate


print('''               Main Menu
                [1] First Come First Serve 
                [2] Shortest Job First
                [3] Exit ''')

menu=int(input('Input your process management: '))

def first_come_first_serve():
    process=int(input('Input number of processes:  '))
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

def shortest_job_first():
    process=int(input('Input number of processes:  '))
    burstTime=[]
    wt= [0] * process
    tat= [0] * process
    ct= [0] * process

    for i in range(process):
        burst=int(input("Enter burst time for {}:".format(i+1)))
        burstTime.append(burst)

        if i > 0:
            tat[i] = wt[i]+ burstTime[i]
            wt[i] = tat[i-1]-burstTime[i-1]
            ct [i] = burstTime[i-1] + tat[i-1]

            avg_wt=sum(wt)/process
            avg_tat=sum(tat)/process
            avg_ct = sum(ct)/process

    headers= ['Processes','Burst Time','Turn-Around Time','Waiting Time','Completion Time']
    data = [[i+1,burstTime[i],tat[i],wt[i],ct[i]] for i in range(process)]

    print(tabulate(data,headers=headers,tablefmt='grid'))

    print("Average Turnaround Time:",round(avg_tat))
    print("Average Waiting Time:",round(avg_wt))

if menu == 1:
    first_come_first_serve()
else:
    shortest_job_first()




