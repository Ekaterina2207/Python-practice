s = input('Введите текст: ')
k = input('Введите символ: ')
def draw_box(s, k):
    print(k * (len(s)+2))
    print(k, s, k, sep='')
    print(k * (len(s)+2))
draw_box(s, k)