violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]
total_time = 0
qty_songs= int(input('Сколько песен выбрать? '))
if qty_songs <= 0:
    print('Введено некорректное число')
for i in range(qty_songs):
    song_name = input(f'Название {i+1}-й песни: ')
    for j, item in enumerate(violator_songs):
        if item[0] == song_name:
            total_time += item[1]
            violator_songs.pop(j)
print('Общее время звучания песен:', total_time)