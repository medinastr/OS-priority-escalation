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
    if processes1 != []  and (processes2 != [] or processes3 != [] or processes4 != []) :
        p = processes1.pop(0)
        processes2.append(p)
        print(f'Process {p} incremented priority: 1 -> 2')
    elif processes2 != [] and (processes3 != [] or processes4 != []):
        p = processes2.pop(0)
        processes3.append(p)
        print(f'Process {p} incremented priority: 2 -> 31')
    elif processes3 != [] and processes4 != []:
        p = processes3.pop(0)
        processes4.append(p)
        print(f'Process {p} incremented priority: 3 -> 4')
    else :
        print("There is no priority to increment.")

def processing(processes):
    print(processes)
    global time
    while processes:
        process = processes.pop(0)  # Retira o primeiro processo da fila
        original_process = process  # Salva o valor original do processo
        quantum_aux = 0
        
        while quantum_aux < quantum and process > 0:
            time += 1
            quantum_aux += 1
            process -= 1
            
            # Incrementar prioridade ao atingir o tempo
            if time == time_to_increment_priority:
                incrementPriority()
                time = 0
        
        if process > 0:
            processes.append(process)  # Reinsere o processo com o tempo restante
        print(f"Processed: {original_process}, Remaining: {process}")
        print(processes)

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