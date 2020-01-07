//bubble sort ascending order

#include <stdio.h>

int bubble_sort(int* arr,int size);

int main()
{
    int i,size,arr[30];
    
    printf("Enter the size of the array : ");
    scanf("%d",&size);
    
    for(i=0;i<size;i++)
    {
        scanf("%d",&arr[i]);
    }
    
    bubble_sort(arr,size);
    
    for(i=0;i<size;i++)
    {
        printf("%d ",arr[i]);
    }
    
    
    return 0;
}

int bubble_sort(int* arr,int size)
{
    int i,k,temp=0;
    int flag = 0;
    
    for(k=0;k<size;k++)
    {
        for(i=0;i<size-k-1;i++)
        {
            if(arr[i]>arr[i+1])          //Ascending order
            {
                temp = arr[i];             //Element Swap
                arr[i] = arr[i+1];
                arr[i+1] = temp;
                flag = 1;
            }
            
            
        }
        if(flag==0)             //breaks the loop if array is sorted
            {
                break;
            }
    }
    return 0;
}
