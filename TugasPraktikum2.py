a = int(input("Masukkan bilangan a: "))
b = int(input("Masukkan bilangan b: "))
c = int(input("Masukkan bilangan c: "))

if a > c and a > b:
    print("Bilangan terbesar adalah bilangan a =",a)
elif b > a and b > c:
    print("Bilangan terbesar adalah bilangan b =",b)
else:
    print("Bilangan terbesar adalah bilangan c =",c)