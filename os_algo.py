import sys
from tabulate import tabulate
from art import *

class Process:
        def __init__(self, pid, arrival_time=0, burst_time=0):
            self.pid = pid
            self.arrival_time = arrival_time
            self.burst_time = burst_time
            self.remaining_time = burst_time
            self.completion_time = 0

def shortest_remaining_time_first(processes):
    time = 0
    completed_processes = 0
    n = len(processes)

    while completed_processes < n:
        min_remaining_time = float('inf')
        min_index = -1

        for i in range(n):
            if processes[i].arrival_time <= time and processes[i].remaining_time > 0:
                if processes[i].remaining_time < min_remaining_time:
                    min_remaining_time = processes[i].remaining_time
                    min_index = i

        if min_index == -1:
            time += 1
            continue

        processes[min_index].remaining_time -= 1
        time += 1

        if processes[min_index].remaining_time == 0:
            processes[min_index].completion_time = time
            completed_processes += 1

    total_waiting_time = 0
    total_turnaround_time = 0
    total_completion_time = 0  

    for p in processes:
        p.turnaround_time = p.completion_time - p.arrival_time
        p.waiting_time = p.turnaround_time - p.burst_time
        total_waiting_time += p.waiting_time
        total_turnaround_time += p.turnaround_time
        total_completion_time += p.completion_time  

    average_waiting_time = total_waiting_time / n
    average_turnaround_time = total_turnaround_time / n
    average_completion_time = total_completion_time / n  

    print("\t\t\t\t\tSummary Table")
    headers = ['Process', 'Arrival Time', 'Burst Time', 'Completion Time', 'Turnaround Time', 'Waiting Time']
    data = [[p.pid, p.arrival_time, p.burst_time, p.completion_time, p.turnaround_time, p.waiting_time] for p in processes]

    print(tabulate(data, headers=headers, tablefmt='grid'))
    print("\nAverage Completion Time:", round(average_completion_time, 2))
    print("Average Turnaround Time:", round(average_turnaround_time, 2))
    print("Average Waiting Time:", round(average_waiting_time, 2))
    print('\n') 

def run_srtf():
    print("""          
              __________                                 
            .'----------`.                              
            | .--------. |                             
            | |########| |       __________              
            | |########| |      /__________\             
   .--------| `--------' |------|    --=-- |------------------.
   |        `----,-.-----'      |o ======  |                  | 
   |       ______|_|_______     |__________|                  | 
   |      /  %%%%%%%%%%%%  \       Shortest Remaining         | 
   |     /  %%%%%%%%%%%%%%  \             ---                 | 
   |     ^^^^^^^^^^^^^^^^^^^^          Time First             |
   +----------------------------------------------------------+
   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
            """)

    process_count = int(input("Input number of processes: "))
    print("\n")
    processes = []

    for i in range(process_count):
        arrival_time = int(input("Enter arrival time for process {}: ".format(i+1)))
        burst_time = int(input("Enter burst time for process {}: ".format(i+1)))
        print('\n') 
        processes.append(Process(i+1, arrival_time, burst_time))

        if burst_time == 0:
            print("Burst time cannot be 0.")
            exit(1)

    shortest_remaining_time_first(processes)

def first_come_first_serve():
    print("""          
              __________                                 
            .'----------`.                              
            | .--------. |                             
            | |########| |       __________              
            | |########| |      /__________\             
   .--------| `--------' |------|    --=-- |------------------.
   |        `----,-.-----'      |o ======  |                  | 
   |       ______|_|_______     |__________|                  | 
   |      /  %%%%%%%%%%%%  \           First Come             | 
   |     /  %%%%%%%%%%%%%%  \             ---                 | 
   |     ^^^^^^^^^^^^^^^^^^^^          First Serve            |
   +----------------------------------------------------------+
   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
            """)
     
    process=int(input('Input number of processes: '))
    print('\n')
    burstTime=[]
    wt= [0] * process
    tat= [0] * process

    for i in range(process):
        burst=int(input("Enter burst time for {}: ".format(i+1)))
        burstTime.append(burst)

        if i > 0:
            wt[i] = burstTime[i-1]+wt[i-1]
        tat[i] = wt[i]+ burstTime[i]

        avg_wt=sum(wt)/process
        avg_tat=sum(tat)/process

    print("\t\t\tSummary Table")
    headers= ['Processes','Burst Time','Turn-Around Time','Waiting Time']
    data = [[i+1,burstTime[i],tat[i],wt[i]]for i in range(process)]

    print(tabulate(data,headers=headers,tablefmt='grid'))

    print("Average Turnaround Time:",round(avg_tat,2))
    print("Average Waiting Time:",round(avg_wt,2))

def shortest_job_first():
    print("""          
              __________                                 
            .'----------`.                              
            | .--------. |                             
            | |########| |       __________              
            | |########| |      /__________\             
   .--------| `--------' |------|    --=-- |------------------.
   |        `----,-.-----'      |o ======  |                  | 
   |       ______|_|_______     |__________|                  | 
   |      /  %%%%%%%%%%%%  \           Shortest Job           | 
   |     /  %%%%%%%%%%%%%%  \             ---                 | 
   |     ^^^^^^^^^^^^^^^^^^^^      First(Non-Preemptive)      |
   +----------------------------------------------------------+
   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
            """)
    process=int(input('Input number of processes:  '))
    print('\n')
    burstTime=[]

    for i in range(process):
        burst=int(input("Enter burst time for process {}: ".format(i+1)))
        burstTime.append(burst)

    burstTime.sort()
    wt= [0] * process
    tat= [0] * process
    ct= [0] * process

    ct[0] = burstTime[0]  
    tat[0] = burstTime[0] 
    wt[0] = 0   

    for i in range(process):
        if i > 0:
            ct [i] = ct[i-1]+ burstTime[i] 
            tat[i] = ct[i] 
            wt[i]= ct[i]-burstTime[i]

        avg_wt=sum(wt)/process
        avg_tat=sum(tat)/process
        avg_ct = sum(ct)/process


    print("\t\t\tSummary Table")
    headers= ['Processes','Completion Time','Turn-Around Time','Waiting Time']
    data = [[i+1,ct[i],tat[i],wt[i]] for i in range(process)]

    print(tabulate(data,headers=headers,tablefmt='grid'))

    print("Average Completion Time:",round(avg_ct,2))
    print("Average Turnaround Time:",round(avg_tat,2))
    print("Average Waiting Time:",round(avg_wt,2))


def confirm_exit():
    while True:
        valid = input('Are you sure you want to exit? (Y/N): ').upper()
        if valid == 'Y':
            print('Exiting the program')
            sys.exit()
        elif valid == 'N':
            return True
        else:
            print("Invalid input. Please enter 'Y' or 'N'.")

def main():
    while True:
        tprint("Main Menu",font="block",chr_ignore=True)
        tprint('''
                First Come First Serve 
                Shortest Job First
                Shortest Remaining Time First
                ''', font="cybermedium")
        print("\t\t\t\t\t\t\t\tSelect from the following Algorithms:\n\n\n")
        print("\t\t\t\t»» [1] FCFS\t\t [2] SJF\t\t\t [3] SRTF\t\t\t [4] Exit ««\n\n\n")

        processes = []
        menu=int(input('Input your Choice [1-4]: '))

        if menu == 1:
            first_come_first_serve()
        elif menu == 2:
            shortest_job_first()
        elif menu == 3:
            run_srtf()
        elif menu == 4:
            if confirm_exit():
                break
        else:
            print('Invalid Input. Try again.')

if __name__ == "__main__":
    main()
