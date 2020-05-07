#include <stdio.h>
#include <conio.h>
#include <string.h>

int max(int a, int b);

char *s1, *s2;	//for dynamic alloc
int i, j, m, n, length;
int table[10][10] = {0};
char sequence[10] = {0};

void LCS();
void print_table();
void sequenceFinder();

int main()
{
  clrscr();

  //Getting first string
  printf("\nEnter size of string 1 : ");
  scanf("%d", &m);

  //dynamic allocation of memory for string
  s1 = (char*)malloc((m+1) * sizeof(char));

  printf("Enter string 1: ");
  scanf("%s", s1);

  //Getting second string
  printf("\nEnter size of string 2 : ");
  scanf("%d", &n);

  //dynamic allocation of memory for string
  s2 = (char*)malloc((n+1) * sizeof(char));

  printf("Enter string 2: ");
  scanf("%s", s2);

  //Displaying both strings
  printf("\nString 1 : %s\n", s1);
  printf("String 2 : %s\n", s2);

  //Calling to dynamically programmed LCS function
  LCS();
  //printing the DP table
  print_table();

  /*Length of longest subsequence is stored
	in the last element of table*/
  length = table[m][n];
  printf("\nLength of LCS is %d", length);

  if(length == 0)
    printf("\nNo LCS found");
  else
  {
    //traces the longest common subsequence
    sequenceFinder();
    printf("\nThe LCS       : %s", sequence);
  }

  getch();
  return 0;
}

void LCS()
{
  for (i=0; i<=m; i++)
    for (j=0; j<=n; j++)
    {
      if (i == 0 || j == 0)
				table[i][j] = 0;

      //when char of both strings match
      else if (s1[i-1] == s2[j-1])
				//assign incremented value of upper-left diagonal element
				table[i][j] = table[i-1][j-1] + 1;
      //if char of both strings dont match
      else
				//assign max value of upper or left element
				table[i][j] = (table[i-1][j] > table[i][j-1]) ? table[i-1][j] : table[i][j-1];
    }

}

void sequenceFinder()
{
	sequence[length] = '\0';
	i = m;
	j = n;
	while (i > 0 && j > 0)
		// If current character in s1 and s2 are same, then
		// current character is part of LCS
		if (s1[i-1] == s2[j-1])
		{
			sequence[length-1] = s1[i-1]; // Put current character in result
			i--; j--; length--;     // reduce values of i, j and length
		}

		// If not same, then find the larger of two and
		// go in the direction of larger value
		else if (table[i-1][j] > table[i][j-1])
			i--;
		else
			j--;
}

void print_table()
{
  printf("\n\n");
  printf("DP table : \n");
  for(i = 0; i < m+1; i++)
    for(j = 0; j < n+1; j++)
    {
      printf("%d\t", table[i][j]);
      if((j+1) % (n+1) == 0)
				printf("\n");
    }
}