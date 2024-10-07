/*+-------------------------------------------------------------+
| UNIFAL – Universidade Federal de Alfenas. |
| BACHARELADO EM CIENCIA DA COMPUTACAO. |
| Trabalho..: Escalonamento de processos |
| Disciplina: Sistemas Operacionais |
| Professor.: Fellipe Rey |
| Aluno(s)..: Pedro Medina 2023.1.08.033
|             Vinicius Gomes 2023.1.08.022 |
| Data......: 13/10/2024 |
+-------------------------------------------------------------+*/

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <stdbool.h>
#define QUANTUM 6

typedef struct Node_{
    int time;
    struct Node_ *prox;
}Node;

// insere o novo processo na fila
Node *insereProcesso(Node *begin) {
    Node *novo_no = (Node*)malloc(sizeof(Node));
    novo_no->time = rand() % 20 + 1; // número aleatório de 1-20
    Node *pont = begin;
    if(begin == NULL) {
        return novo_no;
    }
    while(pont->prox != NULL) { // percorrendo a fila até achar o fim
        pont = pont->prox;
    }
    pont->prox = novo_no;
    return begin; // retorna o começo da fila com o novo processo inserido no fim
}

Node *deleteProcess(Node *begin) {
    Node *pont = begin;
    if(pont != NULL) {
        begin = begin->prox;
        free(pont);
    }
    return begin;
}

void showProcesses(Node *begin) {
    printf("Processes: ");
    if(begin != NULL) {
        Node *pont = begin;
        while(pont != NULL) {
            printf("%d ", pont->time);
            pont = pont->prox;
        }
    }
    printf("\n-------------------------\n");
}

int generateRandomProcess() {
    return (rand() % 20) + 1;
}

int generateRandomQuantum() {
    return (rand() % 8) + 1;
}

int generateRandomPriority() {
    return (rand() % 4) + 1;
}

int generateRandomTimeToIncrement() {
    return (rand() % 30) + 1;
}

// a função recebe um novo NO com as unidades de tempo que não foram processadas
// e as coloca no final da lista, visando o método Round-Robin
Node *insereNoFinal(Node *begin, Node *resto) {
    Node *pont = begin;
    while(pont->prox != NULL) { // percorre a lista até o final
        pont = pont->prox;
    }
    pont->prox = resto; // coloca o restante do processo no final da lista
    return begin;
}

Node *processing(Node *begin, int *time, int timeToIncrement, int quantum) {
    int quantum_aux = quantum;
    if(begin != NULL) {
        Node *p = begin;
        while(p->time > 0 && quantum_aux > 0) {
            time = time + 1;
            p->time = p->time - 1;
            quantum_aux = quantum_aux - 1;
            if(time == timeToIncrement) {
                // deve aumentar a prioridade de um processo
            }
        }
    }
    return begin;
}

Node *startProcesses() {
    Node *begin = NULL;
    int size = generateRandomProcess();
    for(int i = 0; i < size; i++) {
        Node *process = (Node*)malloc(sizeof(Node));
        process->time = generateRandomProcess;
        begin = insereNoFinal(begin, process);
    }
    return begin;
}

int main() {

    srand(time(NULL));

    Node *beginPriorities4 = startProcesses();
    Node *beginPriorities3 = startProcesses();
    Node *beginPriorities2 = startProcesses();
    Node *beginPriorities1 = startProcesses();

    int timeToIncrement = generateRandomTimeToIncrement();
    int quantum = generateRandomQuantum();
    int time = 0;

    beginPriorities4 = processing(beginPriorities4, &time, timeToIncrement, quantum);

    return 0;
}