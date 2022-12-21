#include<stdio.h>
#include<math.h>

int factorial(int c)
{
  int r;
  for (r = 1; c > 1; r *= (c--))
    ;
  return r;
}

double sum(double eps, double x)
{	
	int n = 0;
	double S = 0.0, t;
	do{
		t = (pow(-1, n)*pow(x, n+1))/((n+1)*factorial(2+n));
		S+=t;
		n++;
		}while(t>eps);
	return S;
}
	
int main()
{
	double S, eps, x;
	printf("\nВведите точность расчёта eps от 0 до 1 = ");
	scanf("%lf", &eps);
	printf("\nВведите ненулевое значение числа x: ");
	scanf("%lf", &x);
	if (x != 0 && 1 > eps > 0)
	{
		S = sum(eps, x);
		printf("\nСумма = %lf", S);
		return 0;
	}
	else
	{
		printf("Неверно задан x или точность расчёта");
		return 0;
	}
}
