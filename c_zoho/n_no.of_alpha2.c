/* 1. i/p : v10s9   o/p : vvvvvvvvvvsssssssss
   2. i/p : a3s4d2  o/p : aaassssdd
*/

#include <stdio.h>

int main()
{
    //initialization and declartion
    char string[30];
    int j,i,number,length = -1;
    
    printf("enter the string : ");
    scanf("%s",string);
    
    //string length
    while(string[++length]!='\0');
    
    //loop for length times 
    for(i=0;i<length;i++)
    {
        if(string[i]>64)
        {
            number = 0;
            j = i;
            
            //condition satisfies is char is '0' to '9'
            while((string[j+1]>=48 && string[j+1]<=57) && (j+1)<length)
            {
                
                //append the number character and convert it into number (similar to atoi())
                number = (number*10)+(string[j+1] - '0');
                j++;
            }
            
            //loop for number times to print previous alphabet
            for(j=0;j<number;j++)
            {
                printf("%c",string[i]);
            }
            
        }
    }

    return 0;
}
