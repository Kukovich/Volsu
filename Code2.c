#include <stdio.h>
#include<math.h>

double free(double a, double b, double h)
{
	double c;
	c = sqrt(pow(a, 2)+pow(b, 2)-(2*a*b*cos(h)));
	return c;
}

int main()
{
	double a, b, c, h;

	printf("\nВведите значение первой стороны = ");
	scanf("%lf", &a);

	printf("\nВведите значение второй стороны = ");
	scanf("%lf", &b);

	printf("\nВведите значение угла в радианах = ");
	scanf("%lf", &h);

	if(a > 0 && b > 0)
	{
        if(3,14159 >= h && h > 0)
        {
            c = free(a, b, h);
            printf("\nТретья сторона = %lf\n%lf\n%lf\n%lf", c, a, b, 2*a*b*cos(h));
            return 0;
        }
        
        else
        {
            printf("Неверно задан угол");
            return 0;
        }
    }

    else
    {
        printf("Неверные данные сторон");
        return 0;
    }
}