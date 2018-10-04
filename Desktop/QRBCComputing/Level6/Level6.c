#include <stdio.h>
int main()
{
	int number;

	printf("Enter an interger: ");

	scanf("%d", &number);

	if( number == 20){
		printf("Correct, you entered: %d", number);
	}else{
		printf("Sorry that was wrong");
	}

	return 0;
}
