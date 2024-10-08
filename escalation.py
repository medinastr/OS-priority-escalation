import random


answer_how_many_processes4 = input("How many processes of priority 4? ")
answer_how_many_processes3 = input("How many processes of priority 3? ")
answer_how_many_processes2 = input("How many processes of priority 2? ")
answer_how_many_processes1 = input("How many processes of priority 1? ")
answer_quantum = input("What is the quantum size? (1 to 8) ")
answer_time_to_increment_priority = input("How much time to increment the priority? ")

try :
    how_many_processes4 = int(answer_how_many_processes4)
    how_many_processes3 = int(answer_how_many_processes3)
    how_many_processes2 = int(answer_how_many_processes2)
    how_many_processes1 = int(answer_how_many_processes1)
    quantum = int(answer_quantum)
    time_to_increment_priority = int(answer_time_to_increment_priority)
except ValueError:
    print("Digit only numbers.")

time = 0

def createArray (how_many_processes) :
    processes = []
    p = 0
    while p < how_many_processes :
        processes.append(random.randint(1,20))
        p = p + 1
    return processes

def incrementPriority() :
    if processes1 != [] :
        p = processes1[-1]
        processes1.pop()
        processes2.append(p)
    elif processes2 != [] :
        p = processes2[-1]
        processes2.pop()
        processes3.append(p)
    elif processes3 != [] :
        p = processes3[-1]
        processes3.pop()
        processes4.append(p)
    else :
        print("There is no process to increment priorities.")
    return p

def processing(processes) :
    time = 0
    while processes != [] :
        for p in processes :
            print(processes)
            p_aux = p
            quantum_aux = 0
            while quantum_aux < quantum and p > 0 :
                time = time + 1
                quantum_aux = quantum_aux + 1
                p = p - 1
                if time == time_to_increment_priority :
                    new_p = incrementPriority()
                    print(f'Process created: {new_p}')
                    time = 0
            if p > 0 :
                p_rest = p_aux - quantum
                processes.append(p_rest)
            del processes[0]
    print(f'END {processes}')

processes4 = createArray(how_many_processes4)  
processes3 = createArray(how_many_processes3)  
processes2 = createArray(how_many_processes2)  
processes1 = createArray(how_many_processes1)

print(processes4)
print(processes3)
print(processes2)
print(processes1)

print("PROCESSING 4")
processing(processes4)
print("PROCESSING 3")
processing(processes3)
print("PROCESSING 2")
processing(processes2)
print("PROCESSING 1")
processing(processes1)

print(processes4)
print(processes3)
print(processes2)
print(processes1)