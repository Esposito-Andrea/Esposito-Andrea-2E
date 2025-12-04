# dati 4 numeri in ingresso restituire il maggiore dei 4


def maggiore(a,b,c,d):
    max= float
    if a>b:
        if a>c:
            if a>d:
                max = a
    
    if b>a:
        if b>c:
            if b>d:
                max = b
    if c>a:
        if c>b:
            if c>d:
                max = c
    else:
        if d>a:
            if d>b:
                if d>c:
                    max = d
    return max
    

a = float(input("inserisci a: "))
b = float(input("inserisci b: "))
c = float(input("inserisci c: "))
d = float(input("inserisci d: "))


m = maggiore(a,b,c,d)

print("tra ", a,",",b, ",",c," e ",d," il maggiore è ",m)