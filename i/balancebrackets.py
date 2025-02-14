def isbalance(s):
    s=[]
    pairs={'}':'{',']':'[',')':'('}

    for val in s:
        if val in '{[(':
            s.append(val)
        elif val in ']})':
            if not s or s[-1] !=pairs[val]:
                return "Not balanced"
            else:
                s.pop()
    return "balanced" if len(s)==0 else "Not balanced"
s=input("enter brackets: ")
print(isbalance(s))
