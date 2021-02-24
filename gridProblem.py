




"""given and n*m grid you can travell only right and dowm find the mim number of moves to travell form top left to bottom right
   in the grid"""



# def gridTraveler(m,n,d):
#
#     if m==1 and n==1:
#         return 1
#     elif m==0 or n==0 :
#         return 0
#     return gridTraveler(m-1,n,d)+gridTraveler(m,n-1,d)
#
# d={}
# print(gridTraveler(1,1,d))
# print(gridTraveler(2,3,d))
# print(gridTraveler(3,2,d))
# print(gridTraveler(3,3,d))
# print(gridTraveler(18,18,d))


def gridTraveler(m,n,d):
    key=str(m)+","+str(n)
    if key in d:
        return d[key]
    if m==1 and n==1:
        return 1
    elif m==0 or n==0:
        return 0
    d[key]= gridTraveler(m-1,n,d)+gridTraveler(m,n-1,d)
    return d[key]

d={}
print(gridTraveler(1,1,d))
print(gridTraveler(2,2,d))
print(gridTraveler(2,3,d))
print(gridTraveler(3,5,d))
print(gridTraveler(18,18,d))

