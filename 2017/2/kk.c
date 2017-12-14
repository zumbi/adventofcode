#include <stdio.h>
#include <unistd.h>
#include <string.h>

int main(){
	char buffer[1024];
	unsigned int sum = 0;

	while (fgets(buffer, sizeof(buffer), stdin)) {
		char *b = buffer;
		unsigned int min = 0xffffffff;
		unsigned int max = 0;
		unsigned int v;
		while (sscanf(b, "%d", &v)) {
			if (v < min)
				min =v;
			if (v > max)
				max =v;
			b = strstr(b, "\t");
			if (!b)
				break;
			b++;
		}
		sum += max - min;
	}

	printf("%ld\n", sum);
}
