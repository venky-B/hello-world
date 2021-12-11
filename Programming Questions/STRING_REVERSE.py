def reverse_string(str_value):
    
    ans = str_value.split();
    
    str_rev = ""
    for i in ans:
        str_rev =str_rev  + i[::-1] + " "
        
        
    print(str_rev)


str_value = input("Enter the string you want to reverse : ") 

reverse_string(str_value)
