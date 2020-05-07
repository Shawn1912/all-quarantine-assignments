#include <stdio.h>
#include <conio.h>

int SubsetSum(int set[], int n, int sum);

int main()
{
int i, n, sum;
int set[10];
clrscr();

printf("\n\nEnter the number of elements : ");
scanf("%d", &n);
printf("\nEnter the elements in set : ");
for(i = 0; i < n; i++)
  scanf("%d", &set[i]);

printf("\nEnter the value of sum : ");
scanf("%d", &sum);

if (SubsetSum(set, n, sum) == 1)
	printf("\nFound a subset with given sum!!!");
else
	printf("\nNo subset with given sum!!!");
getch();
return 0;
}

int SubsetSum(int set[], int n, int sum)
{
	int subset[10][10];
	int i, j;

	for (i = 0; i <= n; i++)
	subset[i][0] = 1;

	for (i = 1; i <= sum; i++)
	subset[0][i] = 0;

	for (i = 1; i <= n; i++)
	{
	for (j = 1; j <= sum; j++)
	{
		if(j<set[i-1])
			subset[i][j] = subset[i-1][j];
		if (j >= set[i-1])
			subset[i][j] = subset[i-1][j] || subset[i - 1][j-set[i-1]];
	}
	}

	printf("\nDP Table : \n")
	for (i = 0; i <= n; i++)
	{
		for (j = 0; j <= sum; j++)
		printf ("%4d", subset[i][j]);
	printf("\n");
	}

	return subset[n][sum];
}
