



"""number of way target can be made by the string given in the array"""

#countConstruct("abcdef",[ab,abc,cd,def,abcd])//op==1




# def countConstruct(taget,words):
#     if taget=="":
#         return 1
#     totalcount=0
#     for word in words:
#         if len(taget)>=len(word) and taget[:len(word)]==word:
#             ways=countConstruct(taget[len(word):],words)
#             totalcount+=ways
#     return totalcount

def countConstruct(target,words,d):
    if target=="":
        return 1
    if target in d:
        return d[target]
    total=0
    for word in words:
        if len(target)>=len(word) and target[:len(word)]== word:
            ways=countConstruct(target[len(word):],words,d)
            total+=ways
    d[target]=total
    return total


print(countConstruct("abcdef",['ab','abc','cd','def','abcd'],{}))#==1
print(countConstruct("purple",["purp","p","ur","le","purpl"],{}))#===2
print(countConstruct("abd",["a"],{}))
print(countConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",[
    "e","ee","eee","eeee","eeeee","eeeeee"],{}))

