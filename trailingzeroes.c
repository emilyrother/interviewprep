//given an integer, find the factorial and then how many 
//trailing zeroes

#include <malloc.h>
#include <string.h>
#include <stdio.h>
#include <stdlib.h>

//returns how many zeroes at the end
int trailingZeroes(int n){
	int x = findFactorial(n);
	int zeroes=0;
	//keep dividing by 10 to decide # of 0s
	while(x%10==0){
		zeroes++;
		x=x/10;
	}
	return zeroes;
}

//finds and returns the factorial
int findFactorial(int n){
	int factorial=1;
	while(n>0){
		factorial=factorial*n;
		n--;
	}
	return factorial;
}