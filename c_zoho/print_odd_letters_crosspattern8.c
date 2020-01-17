/*

Enter the string : venkatesh    

v       h                                                                                                                       
 e     s                                                                                                                        
  n   e                                                                                                                         
   k t                                                                                                                          
    a                                                                                                                           
   k t                                                                                                                          
  n   e                                                                                                                         
 e     s                                                                                                                        
v       h                       

*/

#include <stdio.h>

int main()
{
    char string[30];
    int i,j,length=0;
    
    printf("Enter the string : ");
    scanf("%[^\n]s",string);              //scanf terminates only if newline is entered
    
    //string length
    while(string[++length] != '\0');
    
    if(length %2 ==0)
    {
        printf("Even length can't be printed");
        return 1;
    }
    
    for(i=0;i<length;i++)                  //two for loop to print the pattern
    {
        for(j=0;j<length;j++)
        {
            if(i == j)
            {
                printf("%c",string[i]);
            }
            else if(length-1 == i+j)
            {
                printf("%c",string[j]);
            }
            else
            {
                printf(" ");
            }
        }
        printf("\n");
    }
    

    return 0;
}
