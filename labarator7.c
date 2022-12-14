#include<stdio.h>
#include<math.h>

//int factorial(int c)
//{
  //int r;
  //for (r = 1; c > 1; r *= (c--))
 //   ;
  //return r;
//}
//int factorial(int a)
int main()
{
	int n=0; 
	double S=0.0, eps, x, t;
	printf("\nВведите точность расчёта eps от 0 до 1 = ");
	scanf("%lf", &eps);
	printf("\nВведите ненулевое значение числа x: ");
	scanf("%lf", &x);
	if (x != 0 && 1 > eps > 0)
	{
		do
		{
			int a = n+2, b = 1, c, i;
			if(a != 0)
			{	for(i=1; i<=a; i++)
				{
					b *=i;
				}
				c = b;
			}
			else
			{
				c = b;
			}
			t = pow(x,n+1)/(c*(n+1));
			S+=t;
			n++;
			printf("\nЭпсилон = %lf\nПромежуточная сумма = %lf\n", eps, S);
		}while(t>eps);
		printf("\nСумма = %lf", S);
		return 0;
	}
	else
	{
		printf("Неверно задан x или точность расчёта=%lf",t);
		return 0;
	}
}
