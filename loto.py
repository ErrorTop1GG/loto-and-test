# 1. Создать новый проект "Игра лото""
# 2. Правила игры можно посмотреть тут:  
# https://github.com/dmitry-vs/python-loto-game
# (Если не получается перейти по ссылке, скопируйте и вставьте в строку браузера самостоятельно)

# 3. Написать игру лото.
 
# Возможные подходы к решению задачи:
# 1) Проектирование на основании предметной области. Подумать какие объекты есть в игре и какие из них можно перенести в программу. Для них создать классы с соответствующими свойствами и методами. Проверить каждый класс отдельно. Написать программу с помощью этих классов;
 
# 2) Метод грубой силы + рефакторинг. Написать программу как получиться. После этого с помощью принципа DRY убрать дублирование в коде;
 
# 3) Процедурное программирование.
 
# 4. Минимальные требования: 2 игрока - человек играет с компьютером;
# 5. (Дополнительно *) возможность выбирать тип обоих игроков (компьютер или человек) таки образом чтобы можно было играть: компьютер - человек, человек - человек, компьютер - компьютер;
# 6. (Дополнительно *) возможность играть для любого количества игроков от 2 и более;
 
# 7. Выложите проект на github;
# 8. Можно сдать задание в виде pull request.

import random

class Card:
  source_list = list(range(1,91))
  def __init__(self, name_player):
      self.name = name_player
      self.card_numbers = []

  @classmethod
  def reset_source_list(cls):
      cls.source_list = list(range(1, 91))

  @classmethod
  def get_line_card(cls):
    # Случайные 5 чисел расположенные
    random_numbers = random.sample(cls.source_list, 5)
    random_numbers.sort()  # Сортируем выбранные числа по возрастанию

    # Удалим выбранные числа из исходного списка
    for number in random_numbers:
        cls.source_list.remove(number)
    # Генерируем список из 9 элементов, включая пропуски
    new_list = []
    ind_num=0
    count_emp=0
    for i in range(9):
        if (random.randint(0,1) and ind_num<5) or count_emp>3:
            new_list.append(random_numbers[ind_num])
            ind_num+=1
        else:
            new_list.append('  ')
            count_emp+=1
    return new_list

  def get_card(self):
    '''
    Функция для генерации чисел на 2х карточках без повторений
    На каждой карточке 15 чисел
    В каждой строке числа расположены по возрастанию
    В каждой строке 5 чисел из 9
    '''
    for _ in range(3):
        new_list = Card.get_line_card()
        self.card_numbers.append(new_list)

  def show_card(self):
    n=(26 - (len(self.name)+2))//2
    print('-'*n+f' {self.name} '+'-'*(n+1))
    for line in self.card_numbers:
        st=''
        for num in line:
            if len(str(num))==1:
              st+=' '+str(num)+' '
            else:
              st+=str(num)+' '
        print(st)
    print('-'*26)

  def check_num_card(self, number_barrel):
    lines=[]
    for line in self.card_numbers:
      lines+= line
    return number_barrel in lines

  def cross_number_card(self, number_barrel):
    # Проходим по списку и заменяем
    j=-1
    for line in self.card_numbers:
      j+=1
      for i in range(len(line)):
          if line[i] == number_barrel:
              self.card_numbers[j][i] = '-'

  def is_filled_card(self):
    lines=[]
    for line in self.card_numbers:
      lines+= line
    contains_digits = any(str(item).isdigit() for item in lines)
    return not contains_digits
    
    
class Barrel:
  def __init__(self):
      barrels = list(range(1,91))
      self.queue_barrels = random.sample(barrels, 90)
      self.left_barrels=90
  def next_barrel(self):
      self.left_barrels-=1
      self.current_barrel = self.queue_barrels[self.left_barrels]
      return self.queue_barrels[self.left_barrels]
  def messege_barrel(self):
      print(f'Новый боченок: {self.next_barrel()} (осталось {self.left_barrels})')
      
      
class Player:
  def __init__(self, name):
    self.name = name
    self.card = Card(self.name)
  def give_answer(self):
      answer = input()
      return answer
      
      
class Game:
  def __init__(self):
      print('Начало новой игры')
      Card.reset_source_list()
    #===== Решить поблему обновления карточек (очистка из памяти)
      self.list_players = []
      while True:
        name = input('Введите Имя игрока или stop для продолжения:')
        if name == 'stop':
          break
        self.list_players.append(Player(name))
      computer_player='y'
      if len(self.list_players)>1:
         computer_player = input('Будет ли играть компьютер? y/n')
      if computer_player == 'y':
        self.list_players.append(Player('Компьютер'))
      for player in self.list_players:
          player.card.get_card()
      self.barrel = Barrel()
  @staticmethod
  def show_question():
    print('Зачеркнуть цифру? (y/n)')

  def communication(self,player):
    #Число есть на карточке и игрок отвечает n или
    #Числа нет на карточке и игрок говорит зачеркнуть
    print(f'{player.name}')
    Game.show_question()
    answer = player.give_answer()
    num_in_card=player.card.check_num_card(self.barrel.current_barrel)
    if (num_in_card and answer.lower() == 'n') or\
       (not num_in_card and answer.lower() == 'y'):
        # Должны завершить игру
        return False
    elif (num_in_card and answer.lower() == 'y'):
          player.card.cross_number_card(self.barrel.current_barrel)
          #Зачеркиваем и продолжаем
          return True
    else: #нет числа и ответил не зачеркивать (продолжаем без изменений)
          return True

  def play_round(self):
        info = {}
        info['win'] = 'nobody'
        info['lose'] = 'nobody'
        self.barrel.messege_barrel()

        for player in self.list_players:
          player.card.show_card()

        if self.list_players[-1].card.check_num_card(
                           self.barrel.current_barrel):
           self.list_players[-1].card.cross_number_card(
                              self.barrel.current_barrel)

        for player in self.list_players[:-1]:
            if self.communication(player):
               if player.card.is_filled_card():
                  info['win'] = player.name
                  info['lose'] = 'others'
                  return True, info
               else:
                  return False, info
            else:
              info['win'] = 'nobody'
              info['lose'] = player.name
              return True, info

  def start_game(self):
      while True:
           is_game_finish, info = self.play_round()
           if is_game_finish:
              print(f'Win: {info["win"]}')
              print(f'Lose: {info["lose"]}')
              break
     