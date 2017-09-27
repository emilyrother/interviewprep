//given a sorted linked list delete nodes that duplicate numbers
//leaving only distinct numbers from original list

#include <malloc.h>
#include <string.h>
#include <stdio.h>
#include <stdlib.h>

struct Node{
	int data;
	struct Node* next;
}

linkedlist delete(linkedlist original){
	
	struct Node* check=head;
	struct Node* tbd; //pointer to store the next for the to be deleted

	while(check->next != NULL){
		if(check->data == check->next->data){
			//remove the next node 
			tbd=check->next->next;
			free(check->next);
			check->next=tbd; //new next value is the one after next
		}
		//change pointer only if not deleted
		else{
			check = check->next;
		}
	}

	return original;

}
