#include<stdio.h>
#include<math.h>

int factorial(int c)
{
  int r;
  for (r = 1; c > 1; r *= (c--))
    ;
  return r;
}
int main()
{
	int n=0; 
	double S=0.0, eps, x, a, b;
	printf("Введите ненулевое значение числа x: ");
	scanf("%lf", &x);
	//printf("\nВведите допустимое минимальное значение эпсилон (включительно): ");
	//scanf("%lf", &a);
	printf("\nВведите допустимое максимальное значение эпсилон (включительно): ");
	scanf("%lf", &b);
	if (x != 0)
	{
		do
		{
			eps = (pow(-1, n)*pow(x, n+1))/((n+1)*factorial(2+n));
			S+=eps;
			n = n+1;
			printf("\nЭпсилон = %lf\nПромежуточная сумма = %lf\n", eps, S);
		}while(eps<=b);
		printf("\nСумма = %lf", S);
		return 0;
	}
	else
	{
		printf("Неверно задан x");
		return 0;
	}
}
