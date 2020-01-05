/* Enter the no.of elements in the array : 10                                                                                    
   1 2 3 4 5 6 7 89 56 345                                                                                                       
   345 1 89 2 56 3 7 4 6 5
*/

//Given an array of integers, rearrange the array in such a way that the first element is first maximum and second element is first minimum.
// implemented using selection sort

#include <stdio.h>

int alternate_sort(int* arr,int size); //function prototype

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
    alternate_sort(arr,size);
    
    for(i=0;i<size;i++)
    {
        printf("%d ",*(arr+i));   // *(arr+i) = arr[i]
    }

    return 0;
}

int alternate_sort(int* arr,int size)
{
    int i,j,temp = 0,index;
    
        for(i=0;i<size;i++)
        {
            index = i;
            for(j=i+1;j<size;j++)
            {
                
                if(i%2==0 && arr[index]<arr[j]) //find the largest element in an array
                {
                    index = j;
                }
                
                else if(i%2!=0 && arr[index]>arr[j]) //find the smallest element in an array
                {
                    index = j;
                }
            }
            
        
            temp = arr[i];
            arr[i] = arr[index];  //arr[index] = arr[index] + arr[i] - (arr[i] = arr[index]); (alternative)
            arr[index] = temp;
        }
    
        
    return 0;
}
