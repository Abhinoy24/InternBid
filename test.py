a = [5,10,12,15,16]
newlist = []
length = len(a)
print(length)
def modifylist():
    return [a[0],a[length-1]]
newlist = modifylist()
print(newlist)