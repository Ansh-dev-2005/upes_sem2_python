struct Node {
    int data;
    struct Node* prev;
    struct Node* next;
};

struct DoubleLinkedList {
    struct Node* head;
    struct Node* tail;
    int size;
};

void initList(struct DoubleLinkedList* list) {
    list->head = NULL;
    list->tail = NULL;
    list->size = 0;
}

void insertAtBeginning(struct DoubleLinkedList* list, int data) {
    struct Node* newNode = (struct Node*) malloc(sizeof(struct Node));
    newNode->data = data;
    newNode->prev = NULL;
    newNode->next = list->head;
    
    if (list->head == NULL) {
        list->tail = newNode;
    } else {
        list->head->prev = newNode;
    }
    
    list->head = newNode;
    list->size++;
}

void insertAtEnd(struct DoubleLinkedList* list, int data) {
    struct Node* newNode = (struct Node*) malloc(sizeof(struct Node));
    newNode->data = data;
    newNode->prev = list->tail;
    newNode->next = NULL;
    
    if (list->tail == NULL) {
        list->head = newNode;
    } else {
        list->tail->next = newNode;
    }
    
    list->tail = newNode;
    list->size++;
}

void insertAtIndex(struct DoubleLinkedList* list, int index, int data) {
    if (index < 0 || index > list->size) {
        printf("Index out of bounds.\n");
        return;
    }
    
    if (index == 0) {
        insertAtBeginning(list, data);
    } else if (index == list->size) {
        insertAtEnd(list, data);
    } else {
        struct Node* current = list->head;
        for (int i = 0; i < index; i++) {
            current = current->next;
        }
        
        struct Node* newNode = (struct Node*) malloc(sizeof(struct Node));
        newNode->data = data;
        newNode->prev = current->prev;
        newNode->next = current;
        current->prev->next = newNode;
        current->prev = newNode;
        list->size++;
    }
}

void removeFromBeginning(struct DoubleLinkedList* list) {
    if (list->head == NULL) {
        printf("List is empty.\n");
        return;
    }
    
    struct Node* nodeToDelete = list->head;
    list->head = nodeToDelete->next;
    
    if (list->head == NULL) {
        list->tail = NULL;
    } else {
        list->head->prev = NULL;
    }
    
    free(nodeToDelete);
    list->size--;
}

void removeFromEnd(struct DoubleLinkedList* list) {
    if (list->tail == NULL) {
        printf("List is empty.\n");
        return;
    }
    
    struct Node* nodeToDelete = list->tail;
    list->tail =



void removeFromEnd(struct DoubleLinkedList* list) {
    if (list->tail == NULL) {
        printf("List is empty.\n");
        return;
    }
    
    struct Node* nodeToDelete = list->tail;
    list->tail = nodeToDelete->prev;
    
    if (list->tail == NULL) {
        list->head = NULL;
    } else {
        list->tail->next = NULL;
    }
    
    free(nodeToDelete);
    list->size--;
}

void removeFromIndex(struct DoubleLinkedList* list, int index) {
    if (index < 0 || index >= list->size) {
        printf("Index out of bounds.\n");
        return;
    }
    
    if (index == 0) {
        removeFromBeginning(list);
    } else if (index == list->size - 1) {
        removeFromEnd(list);
    } else {
        struct Node* current = list->head;
        for (int i = 0; i < index; i++) {
            current = current->next;
        }
        
        current->prev->next = current->next;
        current->next->prev = current->prev;
        free(current);
        list->size--;
    }
}

void printList(struct DoubleLinkedList* list) {
    struct Node* current = list->head;
    while (current != NULL) {
        printf("%d ", current->data);
        current = current->next;
    }
    printf("\n");
}

int main() {
    struct DoubleLinkedList list;
    initializeList(&list);
    
    insertAtBeginning(&list, 1);
    insertAtBeginning(&list, 2);
    insertAtEnd(&list, 3);
    insertAtEnd(&list, 4);
    insertAtIndex(&list, 2, 5);
    
    printf("List contents: ");
    printList(&list);
    
    removeFromBeginning(&list);
    removeFromEnd(&list);
    removeFromIndex(&list, 1);
    
    printf("List contents after removals: ");
    printList(&list);
    
    return 0;
}