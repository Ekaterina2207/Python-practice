from math import *

a = int(input('Введите значение числа a: '))
b = int(input('Введите значение числа b: '))
info = '''
a + b = {plus}
a - b = {minus}
a * b = {mult}
a / b = {delit}
a // b = {celoe}
a % b = {ostatok}
a ** b = {stepen}
log10(a) = {lga} 
log10(b) = {lgb}
a < b = {smen}
a <= b = {men}
a > b = {sbol}
a >= b = {bol}
a != b = {neravno}
a == b = {ravno}
'''
print(
    info.format(
        plus=a + b,
        minus=a - b,
        mult=a * b,
        delit=round(a / b, 2),
        celoe=a // b,
        ostatok=a % b,
        stepen=a ** b,
        lga=round(log10(a), 2),
        lgb=round(log10(b), 2),
        smen=a < b,
        men=a <= b,
        sbol=a > b,
        bol=a >= b,
        neravno=a != b,
        ravno=a == b
    )
)