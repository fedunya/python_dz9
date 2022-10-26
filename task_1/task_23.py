# Создайте программу для игры в "Крестики-нолики".

def user_input(name, val):    
    _ = 0
    while _ == 0:
        num = input(f'{name}, введите номер ячейки для хода: ')
        if not num.isdigit() or num not in '123456789': print('Неверный ввод!')
        elif val[int(num) - 1] != ' ': print('Ячейка уже занята!')
        else:
            _ = 1
            num = int(num)
    return num

def field_play(val): 
    print(' Игровое поле\t\tНумерация ячеек поля') 
    print('┌───┬───┬───┐') 
    print(emoji.emojize('| {} | {} | {} |\t\t      :one:  :two:  :three:'
                        .format(val[0], val[1], val[2]), language='alias')) 
    print('├───┼───┼───┤')     
    print(emoji.emojize('| {} | {} | {} |\t\t      :four:  :five:  :six:'
                        .format(val[3], val[4], val[5]), language='alias')) 
    print('├───┼───┼───┤')  
    print(emoji.emojize('| {} | {} | {} |\t\t      :seven:  :eight:  :nine:'
                        .format(val[6], val[7], val[8]), language='alias')) 
    print('└───┴───┴───┘')    
def check_win_tie(val, cur_symbol, name):
    if (val[0] == val[1] == val[2] == cur_symbol or val[0] == val[3] == val[6] == cur_symbol
        or val[3] == val[4] == val[5] == cur_symbol or val[1] == val[4] == val[7] == cur_symbol
        or val[6] == val[7] == val[8] == cur_symbol or val[2] == val[5] == val[8] == cur_symbol
        or val[0] == val[4] == val[8] == cur_symbol or val[2] == val[4] == val[6] == cur_symbol):
        print(f'{name} победил\n')
        return True
    if val.count('X') + val.count('O') == 9:
        print('Ничья\n')
        return True
    return False

import os, random, emoji
from art import *
os.system("cls")
tprint('Tic-tac-toe')
val = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
player1 = input('Первый игрок, введи свое имя: ')        
player2 = input('Второй игрок, введи свое имя: ')
key = input('Давай узнаем кто будет ходить первым. Нажми Enter ')
_ = random.randint(0, 1)
if _ == 0:
    current_player = player1
    next_player = player2
    print(f'{player1}, твой ход первый! Играешь -> X')
else:
    current_player = player2
    next_player = player1
    print(f'{player2}, тебе ходить первым. Играешь -> X')
current_symbol = 'X'
next_symbol = 'O'
field_play(val)
while not check_win_tie(val, next_symbol, next_player):    
    num = user_input(current_player,val)
    val[num-1] = current_symbol
    field_play(val)
    current_player, next_player = next_player, current_player
    current_symbol, next_symbol = next_symbol, current_symbol
    



