
a = input()
empty_list = []
empty_list.append(a[0].lower())
for i in a[1:]:
    if i in ('ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
        empty_list.append('_') 
        empty_list.append(i.lower())
    elif a in ('ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
        empty_list.append(i.lower())
    else:
        empty_list.append(i)
print(''.join(empty_list))