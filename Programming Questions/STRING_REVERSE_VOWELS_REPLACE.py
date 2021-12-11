str_val = input("Enter the string : ")
count = 1
rev_str = list(str_val)

for i in range(len(rev_str)):
    
    count = count % 10
    if count == 0:
        count =1
    
    if(rev_str[i] in ('a','e','i','o','u','A','E','I','O','U')):
        rev_str[i] = str(count)
        count+=1
        
str_val = "".join(rev_str)

print(str_val[::-1])
