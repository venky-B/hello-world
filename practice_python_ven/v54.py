def sort_v(v_lis):
    return v_lis[1]

v_list = [('abc',124),('def',567),('jr',34)]
print(v_list)
v_list.sort(key=sort_v)     #doubt
print(v_list)

new_list = list(map(lambda x : x[1],v_list))
print(new_list)

