

"""
given an target and an array find whether sum of elements in the array results in target or not
canSum(7,[4,3,7])==> true
"""

# def cansum(target,a):
#     if target==0 :
#         return True
#     if target<0 :
#         return False
#
#     for i in a:
#         remainder=target-i
#         if cansum(remainder,a)==True:
#             return True
#     return False


"""tc==>n^m"""

def cansum(target,a,d):
    if target in d:
        return d[target]
    if target==0:
        return True
    if target<0:
        return False
    for i in a:
        remainder=target-i
        if cansum(remainder,a,d)==True:
            d[target]=True
            return True
    d[target]=False
    return False
# target=int(input())
# n=list(map(int,input().split()))
print(cansum(8,[2,3,5],{}))
print(cansum(300,[7,14],{}))


