//selection sort descending order

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
    int i,j,temp = 0,imax;
    
    for(i=0;i<size;i++)
    {
        imax = i;
        for(j=i+1;j<size;j++)
        {
            if(arr[imax]<arr[j])
            {
                imax = j;
            }
        }
        
        temp = arr[i];
        arr[i] = arr[imax];  //arr[imax] = arr[imax] + arr[i] - (arr[i] = arr[imax]); (alternative)
        arr[imax] = temp;
        
    
    }
    return 0;
}
