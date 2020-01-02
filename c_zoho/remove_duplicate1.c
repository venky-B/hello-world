/* 
1. i/p : java       o/p : javb
2. i/p : abczZ001b  o/p : abczD012e
*/


#include <stdio.h>
#include<ctype.h>
#include<string.h>

//function to check duplication in string returns 1 if there is duplicate char in string
int duplicate_check(char* string,int length)
{
    int i,j;
    for(i=0;i<length-1;i++)
    {
        for(j=i+1;j<length;j++)
        {
            if(string[i] == string[j] || string[i] == tolower(string[j]) || string[i] == toupper(string[j]) )
            {
                return 1;
            }
            
        }
    }
    return 0;
}

//function to convert string  
int convert(char* string,int length)
{
    int i,j;
    for(i=1;i<length;i++)
    {
        j = 0;
        while(j<i)
        {
            if(string[i] == string[j] || string[i] == tolower(string[j]) || string[i] == toupper(string[j]))
            {
                if(string[i] == 'z')
                {
                    string[i] = 'a';
                }
                else if(string[i] == 'Z')
                {
                    string[i] = 'A';
                }
                else if(string[i] == '9')
                {
                    string[i] == '0';
                }
                else
                {
                    string[i] += 1;
                }
            }
            j++;
        }
    }
    return 1;
    
}

//main function
int main()
{
    //declartion and initialization
    char string[50];
    int i,j,length=-1;
    
    printf("Enter the string : ");
    scanf("%s",string);
    
    // string length
    while(string[++length]!='\0');
    
    //iterate until duplication in string
    while(duplicate_check(string,length))
    {
        convert(string,length);
    }
    
    
    printf("\n output : %s",string);

    return 0;
}
