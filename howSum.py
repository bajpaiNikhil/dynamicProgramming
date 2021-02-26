"""

given an target  and an array find whether the target sum can be achived using arrray elements
"""



"""brute force time tc=(n^m*m)"""
# def howsum(target,a):
#     if target==0 :
#         return []
#     if target<0 :
#         return None
#
#     for i in a:
#         remainder=target-i
#         remainder_result=howsum(remainder,a)
#         #print(remainder_result)
#         if remainder_result is not None:
#             remainder_result+=[i]
#             return remainder_result
#
#     return None
#

def howsum(target,a,d):

    if target in d:
        return d[target]
    if target==0:
        return []
    if target<0:
        return None

    for i in a:
        remainder=target-i
        remainder_result=howsum(remainder,a,d)
        if remainder_result is not None:
            remainder_result+=[i]
            d[target]=remainder_result
            return d[target]
    d[target]=None
    return None
print(howsum(7,[2,3],{}))
print(howsum(7,[5,3,4,7],{}))
print(howsum(7,[1,6,7],{}))
print(howsum(300,[7,14],{}))

"""tc of the above is n*m^m
   sc of the above is m^2 """



