import unittest
import subprocess
from unittest.mock import patch
import sys
sys.path.insert(0, '../15')
import loto  # модуль с игрой в лото


class TestProgram(unittest.TestCase):
    def test_1(self):
        self.player = loto.Player('Alex')
        self.assertEqual(self.player.name, 'Alex')
        print("Test 1.0 passed")




    '''def setUp(self):
        # Подготовка к тестам, создание экземпляра игры и другие начальные действия
        self.new_game = loto.Game()
        self.test_player = loto.Player('Alex')
        self.new_game.list_players.append(self.test_player)
    def test_initial_state(self):
        # Тестирование начального состояния игры
        self.assertEqual(len(self.new_game.cards), 3)  # Проверяем количество карточек
        self.assertEqual(self.new_game.list_players[0].name, 'Alex')  # Проверяем количество карточек
        self.assertTrue(all(card.is_empty() for card in self.new_game.cards))  # Проверяем, что все карточки пусты
        self.assertTrue(all(card.is_empty() for card in self.new_game.cards))  # Проверяем, что все карточки пусты
    def test_gameplay(self):
        # # Тестирование игрового процесса
        self.game.start_game()  # Начинаем игру
        self.assertFalse(self.game.is_over())  # Проверяем, что игра не закончена после начала
        
        self.game.draw_number()  # Вытаскиваем номер
        self.assertEqual(len(self.game.drawn_numbers), 1)  # Проверяем, что был вытянут один номер
        
        self.game.check_cards()  # Проверяем карточки после вытягивания номера
        
         # Проверяем, что игра завершена после заполнения карточек
        while not self.game.is_over():
            self.game.draw_number()
            self.game.check_cards()
        self.assertTrue(self.game.is_over())'''

if __name__ == '__main__':
    unittest.main()
