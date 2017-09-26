//fizz buzz oracle prep

#include <malloc.h>
#include <string.h>

string[] fizzbuzz(int n){
	string[n] answer;
	for(int i=0; i<n; i++){
		if(i%3==0){
			answer[i]="Fizz";
		}
		else if(i%5==0){
			answer[i]="Buzz";
		}
		else if(i%5==0 && i%3==0){
			answer[i]="FizzBuzz";
		}
		else{
			answer[i] = i;
		}
	}
	return answer;
}