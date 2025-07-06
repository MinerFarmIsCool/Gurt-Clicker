import pygame
import sys
import abc
import math
import random
#import your_MUM OHHH GODDEM

pygame.init()





class Upgrade():
    def __init__(self, name, upgrade_id, upgrade_price, upgrade_scaler, money_per_second_upgrade, money_per_click_upgrade, is_leveled, max_level):
        self._upgrade_id = upgrade_id
        self._name = name
        self._upgrade_price = upgrade_price
        self._upgrade_scaler = upgrade_scaler
        self._money_per_second_upgrade = money_per_second_upgrade
        self._money_per_click_upgrade = money_per_click_upgrade
        self._is_leveled = is_leveled
        self._max_level = max_level
        self._current_level = 0
        

    def get_upgrade_price(self):
        return self._upgrade_price

    def set_upgrade_price(self, upgrade_price):
        self._upgrade_price = upgrade_price

    def get_max_level(self):
        return self._max_level

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_upgrade_id(self):
        return self._upgrade_id

    def set_upgrade_id(self, upgrade_id):
        self._upgrade_id = upgrade_id

    def get_current_level(self):
        return self._current_level

    def set_current_level(self, current_level):
        self._current_level = current_level

    def increase_current_level(self):
        self._current_level += 1



    def apply_upgrade(self, player):
        player_money_balance = player.get_money_balance()
        player_money_per_click = player.get_money_per_click()
        player_money_per_second = player.get_money_per_second()
        if player_money_balance >= self._upgrade_price:
            player.set_money_balance(player_money_balance - self._upgrade_price)
            self._upgrade_price = int(self._upgrade_price * self._upgrade_scaler)
            player.set_money_per_click(player_money_per_click + self._money_per_click_upgrade)
            player.set_money_per_second(player_money_per_second + self._money_per_second_upgrade)
            self.increase_current_level()





# Upgrades

#U000 = Upgrade(
#    name = ,
#    upgrade_id = ,
#    upgrade_price = ,
#    upgrade_scaler = ,
#    money_per_second_upgrade = ,
#    money_per_click_upgrade = ,
#    is_leveled = ,
#    max_level = 
#)

U001 = Upgrade(
    name = "+$1 per click",
    upgrade_id = 1,
    upgrade_price = 10,
    upgrade_scaler = 1.2,
    money_per_second_upgrade = 0,
    money_per_click_upgrade = 1,
    is_leveled = True,
    max_level = 10^100
)



