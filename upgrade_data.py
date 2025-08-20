import pygame
import sys
import abc
import math
import random
#import your_MUM OHHH GODDEM

pygame.init()





class Upgrade():
    def __init__(self, name, upgrade_id, upgrade_price, upgrade_scaler, money_per_second_upgrade, money_per_click_upgrade, money_per_second_multiplier_upgrade, money_per_click_multiplier_upgrade, money_per_second_multiplier, money_per_click_multiplier, is_leveled, max_level):
        self._upgrade_id = upgrade_id
        self._name = name
        self._upgrade_price = upgrade_price
        self._upgrade_scaler = upgrade_scaler
        self._money_per_second_upgrade = money_per_second_upgrade
        self._money_per_click_upgrade = money_per_click_upgrade
        self._money_per_second_multiplier_upgrade = money_per_second_multiplier_upgrade
        self._money_per_click_multiplier_upgrade = money_per_click_multiplier_upgrade
        self._money_per_second_multiplier = money_per_second_multiplier
        self._money_per_click_multiplier = money_per_click_multiplier
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
        if self._max_level > self._current_level:
            player_money_balance = player.get_money_balance()
            player_money_per_click = player.get_money_per_click()
            player_money_per_second = player.get_money_per_second()
            if player_money_balance >= self._upgrade_price:
                if self._money_per_second_multiplier_upgrade > 0:
                    self._money_per_second_multiplier += self._money_per_second_multiplier_upgrade # In gurt we have "for i in upgrades, gurt_mult *= upgrade.money_per_click_multiplier or something along these lines"
                if self._money_per_click_multiplier_upgrade > 0:
                    self._money_per_click_multiplier += self._money_per_click_multiplier_upgrade
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

U000 = Upgrade(
    name = "+$1 per click",
    upgrade_id = 1,
    upgrade_price = 10,
    upgrade_scaler = 1.2,
    money_per_second_upgrade = 0,
    money_per_click_upgrade = 1,
    money_per_second_multiplier_upgrade = 0,
    money_per_click_multiplier_upgrade = 0,
    money_per_second_multiplier = 0,
    money_per_click_multiplier = 0,
    is_leveled = True,
    max_level = 10^100
)

U001 = Upgrade(
    name = "+$1 per second",
    upgrade_id= 2,
    upgrade_price=25,
    upgrade_scaler = 0,
    money_per_second_upgrade= 1,
    money_per_click_upgrade= 0,
    money_per_second_multiplier_upgrade = 0,
    money_per_click_multiplier_upgrade = 0,
    money_per_second_multiplier = 0,
    money_per_click_multiplier = 0,
    is_leveled = False,
    max_level = 1
)

U002 = Upgrade(
    name = "+100% Gurts per second",
    upgrade_id= 3,
    upgrade_price=50,
    upgrade_scaler = 1.2,
    money_per_second_upgrade= 0,
    money_per_click_upgrade= 0,
    money_per_second_multiplier_upgrade = 1,
    money_per_click_multiplier_upgrade = 0,
    money_per_second_multiplier = 1,
    money_per_click_multiplier = 0,
    is_leveled = False,
    max_level = 20
)

U003 = Upgrade(
    name = "",
    upgrade_id= 4,
    upgrade_price=0,
    upgrade_scaler = 0,
    money_per_second_upgrade= 0,
    money_per_click_upgrade= 0,
    money_per_second_multiplier_upgrade = 1,
    money_per_click_multiplier_upgrade = 1,
    money_per_second_multiplier = 1,
    money_per_click_multiplier = 1,
    is_leveled = False,
    max_level = 1
)



























Upgrades = [U000, U001, U002, U003]
