n = input().upper()
unique_list=list(set(n))
cnt=[]
for i in unique_list:
    cnt.append(n.count(i))
if cnt.count(max(cnt)) > 1:
    print('?')
else:
    print(unique_list[cnt.index(max(cnt))])
