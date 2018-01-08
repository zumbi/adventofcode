#include<stdio.h>

int main(){

	long long a=12,b=0,c=0,d=0;

	b = a;
	b --;
s1:
	d = a;
	a = 0;
	do {
		c = b;
		do {
			a ++;
			c--;
		}while (c!=0);
		d--;
	} while (d!=0);
	b--;
	c =b;
	d = c;
	do {
		d--;
		c++;
	}while(d!=0);

	fprintf(stdout,"%d %d %d %d\n",a,b,c,d);
	c=-16;
	goto s1;

	return 0;

}
