from tabulate import tabulate

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
    print("\nAverage Turnaround Time:", round(average_turnaround_time, 2))
    print("Average Waiting Time:", round(average_waiting_time, 2))
    print("Average Completion Time:", round(average_completion_time, 2)) 
    print("\nPresented by: Angela Samboa - CS1D")

def main():
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
        processes.append(Process(i+1, arrival_time, burst_time))

        if burst_time == 0:
            print("Burst time cannot be 0.")
            exit(1)

    shortest_remaining_time_first(processes)

if __name__ == "__main__":
    main()
