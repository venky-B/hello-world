instr = input()
dict_key = ["break","else","long","switch","case","enum","register","typedef","char","extern","return","union"]
flag = False
for i in dict_key:
    if i == instr :
        flag = True
if flag:
    print(instr," is a keyword")
else:
    print(instr," is not a keyword")