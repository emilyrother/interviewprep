//given a sorted linked list delete nodes that duplicate numbers
//leaving only distinct numbers from original list

#include <malloc.h>
#include <string.h>

linkedlist delete(linkedlist original){
	
	ptr* check;

	while(check->next != NULL){
		if(check->data == check->next->data){
			//remove the next node 
			remove(check);
		}
		//change pointer
		check = check->next;
	}

	return original;

}

//function to remove node
ptr* remove(node duplicate){

}