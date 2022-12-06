#include<stdio.h>
#include<math.h>

factorial(int n)
{
  int r;
  for (r = 1; n > 1; r *= (n--))
    ;
  return r;
}
int main()
{
	int n=0; 
	double S=0.0, eps, x;
	printf("Введите ненулевое значение числа x: ");
	scanf("%lf", &x);
	if (x != 0)
	{
		do
		{
			eps = (pow(-1, n)*pow(x, n+1))/((n+1)*factorial(2+n));
			S+=eps;
			n++;
		}while(eps<1 && eps>0);
		printf("\nСумма = %lf", S);
		return 0;
	}
	else
	{
		printf("Неверно задан x");
		return 0;
	}
}