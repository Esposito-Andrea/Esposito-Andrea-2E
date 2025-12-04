a = float(input("inserisci a: "))
b = float(input("inserisci b: "))
c = float(input("inserisci c: "))
d = float(input("inserisci d: "))

def maggiore():
    if a>b:
        if a>c:
            if a>d:
                max = a
    else:
        if c>d:
            max = c
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
print("tra ", a,",",b, ",",c," e ",d," il maggiore è ",max)

maggiore()
max = float

