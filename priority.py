import random


answer_how_many_processes3 = input("How many processes of priority 3? ")
answer_how_many_processes2 = input("How many processes of priority 2? ")
answer_how_many_processes1 = input("How many processes of priority 1? ")
answer_how_many_processes0 = input("How many processes of priority 0? ")
answer_quantum = input("What is the quantum size? (1 to 8) ")
answer_time_to_increment_priority = input("How much time to increment the priority? ")

try :
    how_many_processes3 = int(answer_how_many_processes3)
    how_many_processes2 = int(answer_how_many_processes2)
    how_many_processes1 = int(answer_how_many_processes1)
    how_many_processes0 = int(answer_how_many_processes0)
    quantum = int(answer_quantum)
    time_to_increment_priority = int(answer_time_to_increment_priority)
except ValueError:
    print("Digit only numbers.")

time = 0

def createArray (how_many_processes, priority) :
    processes = []
    p = 0
    while p < how_many_processes :
        new_process = {"time": random.randint(1,20), "priority": priority}
        processes.append(new_process)
        p = p + 1
    return processes

def incrementPriority() :

    if processes3 != []:
        while processes2 != [] :
            p = processes2.pop(0)
            processes3.append(p)
    
    if processes2 != [] or processes3 != []:
        while processes1 != [] :
            p = processes1.pop(0)
            processes2.append(p)

    if processes1 != [] or processes2 != [] or processes3 != [] :
        while processes0 != [] :
            p = processes0.pop(0)
            processes1.append(p)

    else :
        print("There is no priority to increment.")


def processing(processes):
    showProcesses(processes)
    global time
    i = 0
    aux = 3

    while i <= 3 :
        processesOfPriority = processes[i]
        print("------------------------------------------------------------------------")
        print(f'PROCESSING PRIORITY {aux}')
        print(processesOfPriority)
        print()

        while processesOfPriority :

            process = processesOfPriority.pop(0)
            original_process = process.copy()
            quantum_aux = 0
        
            while quantum_aux < quantum and process["time"] > 0:
                time += 1
                quantum_aux += 1
                process["time"] -= 1
        
                if time == time_to_increment_priority:
                    incrementPriority()
                    time = 0
                    print("Priorities incremented during this process.")

            if process["time"] > 0:
                if (process["priority"]) < aux :
                    priority = process["priority"]
                    processes[priority].append(process)
                else :
                    processesOfPriority.append(process)
        
            print("Processed:", original_process["time"] , ", P:", original_process["priority"], 
            "| Remaining: ", process["time"])
            print(f'P3 list: {processes3}')
            print(f'P2 list: {processes2}')
            print(f'P1 list: {processes1}')
            print(f'P0 list: {processes0}', end="\n\n")
        i += 1
        aux -= 1

def showProcesses(processes) :
    for p in processes :
        print(p)

processes3 = createArray(how_many_processes3, 3)  
processes2 = createArray(how_many_processes2, 2)  
processes1 = createArray(how_many_processes1, 1)  
processes0 = createArray(how_many_processes0, 0)

processes = [processes3, processes2, processes1, processes0]

processing(processes)

print(f'End of processes of priority 3: {processes3}')
print(f'End of processes of priority 2: {processes2}')
print(f'End of processes of priority 1: {processes1}')
print(f'End of processes of priority 0: {processes0}')