# l=["ab1","b","cnjvniesj0"]
# print(len(l))
# for i in range(len(l)):
#     for j in l[i]:
#         print(j)
t=int(input())
for t in range(t):
    l=list(map(str,input().split()))
    a="abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    a=list(a)
    m=len(l)
    summ=0
    for i in range(len(l)):
        for j in range(len(l[i])):
            summ+=j+a.index(l[i][j])

    #         summ+=a.index(j)
    #         print(j,a.index(j))
    print(summ*m)

