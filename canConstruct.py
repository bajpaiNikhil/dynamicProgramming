



"""given an string of character tell whether target string can be reached or not ."""

#canConstruct(abcdef,[ab,abc,cd,def,abcd]) o/p yes==> abcdef


# def canConstruct(taget,words):
#     if taget=="":
#         return True
#
#
#     for word in words:
#         if len(taget)>=len(word) and taget[:len(word)]==word:
#             suffix=taget[len(word):]
#             if canConstruct(suffix,words)==True:
#                 return True
#     return False
#tc==O(n^m*m)
#sc==>o(m^2)


def canConstruct(tagert,words,d):
    if tagert in d:
        return d[tagert]
    if tagert=="":
        return True

    for word in words:
        if len(tagert)>=len(word) and tagert[:len(word)]==word:
            suffix=tagert[len(word):]
            if canConstruct(suffix,words,d)==True:
                d[tagert]=True
                return True
    d[tagert]= False
    return False


#tc==>o(n*m^2)
#sq==>o(m^2)

print(canConstruct("abcdef",["ab,cd","def","abcs","abc"],{}))

print(canConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",[
    "e","ee","eee","eeee","eeeee","eeeeee"],{}))

