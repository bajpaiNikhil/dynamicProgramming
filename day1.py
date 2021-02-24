


#fibonacci series using memorization


# def fib(n):
#     if n<=2:
#         return 1
#     else:
#         return fib(n-1)+fib(n-2)
# print(fib(5))
# print(fib(6))
# print(fib(7))
# print(fib(8))
# print(fib(12))
# print(fib(20))

def fib(n,d):
    if n in d:
        return d[n]
    if n<=2 :
        return 1
    d[n]=fib((n-1),d)+fib(n-2,d)
    return d[n]

d={}
print(fib(5,d))
print(fib(40,d))
print(fib(100,d))



