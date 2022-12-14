#include<stdio.h>
#include<math.h>

int main()
{
	int b = 1, c, i, n;
	printf("Введите значение n:");
	scanf("%d", &n);
	int a = n+2;
	if(a != 0)
	{	for(i=1; i<=a; i++)
		{
			b *=i;
		}
		c = b;
	}
	else
	{
		c = 1;
	}
	printf("\nФакториал = %d", c);
	return 0;
}
