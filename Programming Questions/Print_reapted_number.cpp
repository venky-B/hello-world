//To find most repeated number in an array.
//If the two number have same frequency, the gratest of them should be printed

#include <iostream>

using namespace std;

int max_freq_repeat(int *arr, int num)
{

 int i,j,max_freq,count_freq,max_num;
 max_freq=0;
 max_num = 0;
	
	for(i=0;i<num-1;i++)
	{
	    count_freq = 1;
	    for(j=i+1;j<num;j++)
	    {
	        if(arr[i] == arr[j])
	        {
	            count_freq++;
	        }
	    }
	        if(max_freq<count_freq)
	        {
	            max_freq = count_freq;
	           max_num = arr[i];
	            
	        }
	        
	        else if ( max_freq == count_freq)
	        {
	            max_num = (max_num < arr[i])? arr[i]: max_num;
	        }
	        
	        
	   	}
      
	return max_num;
	
}


int main() {
	int num, arr[20],i;
	
	
	cin>>num;
	for(i=0;i<num;i++)
	{
	    cin>>arr[i];
	}
	
	cout<<max_freq_repeat(arr,num);
	
	return 0;
}
