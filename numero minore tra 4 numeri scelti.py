#seleziona il più grande tra i tre numeri

a = float(input("inserisci a: "))
b = float(input("inserisci b: "))
c = float(input("inserisci c: "))
d = float(input("inserisci d: "))

def minore():
    if a<b:
        if a<c:
            if a<d:
                min = a
    else:
        if c<d:
            min = c
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

print ("tra ", a,",",b, ",",c," e ",d," il minore è ",min)

minore()