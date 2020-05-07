    #include<stdio.h>
    #include<conio.h>
    #include<math.h>
    void putnqueen(int);
    int okqueen(int, int);
    int setqueen(int);
    void queen();
    char p[10][10];
    int n;
    int main() 
    {
      int a, b;
      clrscr();
      printf(" Enter the no. of queens : ");
      scanf("%d", &n);
      for (a = 0; a < n; ++a)
      for (b = 0; b < n; ++b)
      p[a][b] = '.';
      putnqueen(0);
      getch();
    return (0);
    }
    void putnqueen(int x) {
     int a;
     if (x < n) {
     for (a = 0; a < n; ++a) {
     if (okqueen(x, a)) {
     p[x][a] = 'Q';
     putnqueen(x + 1);
     p[x][a] = '.';
     }
     }
     } 

     else {
     printf("\n The solution is ");
     queen();
     }
    }
    int okqueen(int x, int y) {
                 int a, b;
                 for (a = 0; a < n; ++a) {
                 b = setqueen(a);
                 if (y == b || abs(x - a) == abs(y - b))
                 return 0;
                 }
                 return 1;
    }
    int setqueen(int x) {
                 int a;
                 for (a = 0; a < n; ++a)
                 if (p[x][a] == 'Q') {
                 return(a);
                 break;
                 }
    }
    void queen(){
                int a, b;
                printf("\n");
                for (a = 0; a < n; ++a) {
                for (b = 0; b < n; ++b)
                printf("\t%c", p[a][b]);
                printf("\n\n");
                }
    }