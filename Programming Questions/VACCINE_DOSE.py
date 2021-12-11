from datetime import date

def age_finder(dob):
    
    dob_list = dob.split('/',2)
        
    start_time = date(int(dob_list[2]),int(dob_list[1]),int(dob_list[0]))    
    end_time = date.today()
    age = end_time.year - start_time.year - ((end_time.month,end_time.day) < (start_time.month,start_time.day))
    
    return age
    
    
# main_pgm
aadhar = input("Enter aadhar number : ")
dob = input("Enter the date of birth : ")
comorbidity = input("comorbidity : ")

if len(aadhar) == 14:
    if age_finder(dob) >60 or comorbidity =="yes":
        print(1)
        
    elif age_finder(dob) >45:
        print(2)
        
    elif age_finder(dob) >30:
        print(3)
