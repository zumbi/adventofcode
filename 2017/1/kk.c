#include <stdio.h>
#include <unistd.h>

int main(){
	char aux;
	long sum=0;
	int first;
	int last;

	read(0,&aux, 1);
	last = first = aux-'0';

	while (read(0,&aux, 1) == 1) {
		unsigned int next = aux - '0';

		if (next > 9)
			break;

		if (next == last)
			sum += next;
		last = next;
	}

	if (last == first)
		sum += last;

	printf("%ld\n", sum);
}
