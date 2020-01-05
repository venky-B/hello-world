//selection sort ascending order

#include <stdio.h>
int selection_sort(int* arr,int size); //function prototype

int main()
{
    int i,size,arr[30];
    
    printf("Enter the no.of elements in the array : ");
    scanf("%d",&size);
    
    for(i=0;i<size;i++)
    {
        scanf("%d",arr+i);    // arr+i = &arr[i]
    }
    
    //sorting
    selection_sort(arr,size);
    
    for(i=0;i<size;i++)
    {
        printf("%d ",*(arr+i));   // *(arr+i) = arr[i]
    }

    return 0;
}

int selection_sort(int* arr,int size)
{
    int i,j,temp = 0,imin;
    
    for(i=0;i<size;i++)
    {
        imin = i;
        for(j=i+1;j<size;j++)
        {
            if(arr[imin]>arr[j])
            {
                imin = j;
            }
        }
        
        temp = arr[i];
        arr[i] = arr[imin];  //arr[imin] = arr[imin] + arr[i] - (arr[i] = arr[imin]); (alternative)
        arr[imin] = temp;
        
    
    }
    return 0;
}
