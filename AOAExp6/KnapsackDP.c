#include<stdio.h>
#include<conio.h>

int max(int x, int y)
{
	if(x > y)
		return x;
	else
		return y;
}

void main()
{
	int i, j, n, m;
	int p[50], w[50], v[50][50];
	clrscr();

	printf("Enter the number of objects : ");
	scanf("%d", &n);

	printf("Enter the Knapsack capacity : ");
	scanf("%d", &m);

	printf("\nEnter the profit and weight of each object : ");
	for(i = 1; i <= n; i++)
	{
		printf("Profit of obj no. %d : ", i);
		scanf("%d", &p[i]);

		printf("Weight of obj no. %d : ", i);
		scanf("%d", &w[i]);

		printf("\n");
	}

	for (i = 0; i <= n; i++)
	{
		v[i][0] = 0;
	}

	for (j = 0; j <= m; j++)
	{
		v[0][j] = 0;
	}

	for(i = 1; i <= n; i++)
		for(j = 1; j <= m; j++)
			if(i == 1)
				if(j < w[1])
					v[1][j] = 0;
				else
					v[1][j] = p[1];
			else if(j < w[i])
				v[i][j] = v[i-1][j];
			else
				v[i][j] = max(v[i-1][j], v[i-1][j-w[i]] + p[i]);

	printf("\n Maximum profit earned : %d\n", v[n][m]);

	printf("\nValue table is as shown \n");
	for(i = 0; i <= n; i++)
	{
		for(j = 0; j <= m; j++)
			printf("%5d", v[i][j]);
		printf("\n");
	}

	printf("\nObjects included in Knapsack are : ");
	i = n;
	j = m;
	while(i > 0 && j > 0)
	{
		if(v[i][j] != v[i-1][j])
		{
			printf("%d -> ", i);
			j = j - w[i];
			i = i - 1;
		}
		else
			i = i -1;
	}
	getch();
}