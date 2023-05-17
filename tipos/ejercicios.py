n = str(int(input("ingrese un integrante")))
digit_sum = 0
for i in n:
    digit_sum = digit_sum + int(i)**len(n)
if int(n) == digit_sum:
    print(n, "es un numero amstrong")
else:
    print(n, " no es un numero armstrong")
