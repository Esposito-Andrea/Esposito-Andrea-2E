def minore(a,b,c,d):
    min = float
    if a<b:
        if a<c:
            if a<d:
                min = a
    
    if b<a:
        if b<c:
            if b<d:
                min = b
    if c<a:
        if c<b:
            if c<d:
                min = c
    else:
        if d<a:
            if d<b:
                if d<c:
                    min = d
    return min
    

a = float(input("inserisci a: "))
b = float(input("inserisci b: "))
c = float(input("inserisci c: "))
d = float(input("inserisci d: "))


m = minore(a,b,c,d)

print("tra ", a,",",b, ",",c," e ",d," il minore è ",m)