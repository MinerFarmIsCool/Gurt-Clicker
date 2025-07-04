#This is going to be a clicker game for the Gurt franchise
# Made by me :3

import pygame
import sys
import abc
import math
import random
#import your_MUM OHHH GODDEM

pygame.init()


#Setup (global variables)
Screen_Width, Screen_Height, FPS = 1600, 1080, 60
win = pygame.display.set_mode((Screen_Width, Screen_Height))
pygame.display.set_caption("Gurt Clicker")
FONT = pygame.font.SysFont("comisans", 40)
clock = pygame.time.Clock()


# Colours for placeholder sprites
MAGENTA_SPRITE_COLOUR = (255, 0, 255)
WHITE_SPRITE_COLOUR = (255, 255, 255)
GREEN_SPRITE_COLOUR = (0, 255, 0)

# Classes

class Player():
    def __init__(self):
        # Values for how much money the player will earn. Don't know if I should keep here.
        self._money_per_click = 1
        self._money_per_second = 1
        self._money_balance = 0

    def get_money_per_click(self):
        return self._money_per_click
    
    def set_money_per_click(self, new_money_per_click):
        self._money_per_click = new_money_per_click

    
    def get_money_per_second(self):
        return self._money_per_second
    
    def set_money_per_second(self, new_money_per_second):
        self._money_per_second = new_money_per_second

    
    def get_money_balance(self):
        return self._money_balance
    
    def set_money_balance(self, new_money_balance):
        self._money_balance = new_money_balance
    



class Gurt(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.__base_height__ = 200
        self.__base_width__ = 200
        self._width = self.__base_width__
        self._height = self.__base_height__
        self.image = pygame.image.load("Assets/the gurt.png")
        self.image = pygame.transform.scale(self.image, (self._width, self._height))
        self._base_image = self.image
        self._true_x = 400
        self._true_y = 400
        self._x = self._true_x
        self._y = self._true_y
        self._rect = self.image.get_rect()
        self._rect.topleft = (self._x, self._y)
        self._rect.bottomright = (self._x + self._width, self._y + self._height)
        self._hover_width = self._width * 1.2
        self._hover_height = self._height * 1.2

    # Getter/Setters

    def get_coordinates(self):
        return self._x, self._y
    
    def set_coordinates(self, new_x, new_y):
        self._x = new_x
        self._y = new_y
        self._rect.topleft = (int(self._x), int(self._y))

    def get_width_and_height(self):
        return self._width, self._height
    
    def set_width_and_height(self, new_width, new_height):
        self._width = int(new_width)
        self._height = int(new_height)


    def update(self, win):
        win.blit(self.image, self._rect)

    def check_for_input(self, position):
        if position[0] in range(self._rect.left, self._rect.right) and position[1] in range(self._rect.top, self._rect.bottom):
            return True
        return False
    
    def change_size_when_hover(self, position):
        if position[0] in range(self._rect.left, self._rect.right) and position[1] in range(self._rect.top, self._rect.bottom):
            new_width = self._hover_width
            new_height = self._hover_height
            self._width_difference = int((self._hover_width - self.__base_width__) // 2)
            self._height_difference = int((self._hover_height - self.__base_height__) // 2)
            self.set_width_and_height(new_width, new_height)
            self._x = self._true_x - self._width_difference
            self._y = self._true_y - self._height_difference
            self._rect.topleft = (int(self._x), int(self._y))
            self.image = pygame.transform.scale(self._base_image, (self._width, self._height))

        else:
            self._width = self.__base_width__
            self._height = self.__base_height__
            self._x = self._true_x
            self._y = self._true_y
            self.image = pygame.transform.scale(self._base_image, (self._width, self._height))
            self._rect.topleft = (int(self._x), int(self._y))



class Button(): # Written by Baraltech, edited slightly by me
	def __init__(self, image, pos, text_input, font, base_colour, hovering_colour):
		self.image = image
		self.x_pos = pos[0]
		self.y_pos = pos[1]
		self.font = font
		self.base_colour, self.hovering_colour = base_colour, hovering_colour
		self.text_input = text_input
		self.text = self.font.render(self.text_input, True, self.base_colour)
		if self.image is None:
			self.image = self.text
		self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
		self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

	def update(self, win): 
		if self.image is not None:
			win.blit(self.image, self.rect)
		win.blit(self.text, self.text_rect)

	def checkForInput(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			return True
		return False

	def changeColour(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			self.text = self.font.render(self.text_input, True, self.hovering_colour)
		else:
			self.text = self.font.render(self.text_input, True, self.base_colour)
               







# Functions

def player_clicked_gurt(player):
    current_money_balance = player.get_money_balance()
    current_money_per_click = player.get_money_per_click()
    new_money_balance = current_money_balance + current_money_per_click
    player.set_money_balance(new_money_balance)
    
def gurt_shop(player):
    #Setup for the buttons
    plus_one_per_click_button = Button(image=None, pos=(640, 460), text_input="Increase Money Per Click by 1", font=pygame.font.SysFont("comisans", 40), base_colour="Black", hovering_colour="Green")
    back_button = Button(image=None, pos=(640, 600), text_input="Back to Game", font=pygame.font.SysFont("comisans", 40), base_colour="Black", hovering_colour="Green")

    # Other setup
    shopping = True

    while shopping == True:
        clock.tick(30)
        mouse_pos = pygame.mouse.get_pos()  # Update mouse position each frame

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                shopping = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN: # Check to see if player presses escape
                if event.key == pygame.K_ESCAPE:
                    return
            if event.type == pygame.MOUSEBUTTONDOWN:
                if plus_one_per_click_button.checkForInput(mouse_pos):
                    # Add shop logic here
                    pass
                if back_button.checkForInput(mouse_pos):
                    return

        # Display
        win.fill((255, 255, 255))
        
        # Draw shop title
        shop_title = FONT.render("Gurt Shop", True, (0, 0, 0))
        win.blit(shop_title, (600, 200))
        
        # Draw player money
        player_money = FONT.render(f"Money: ${player.get_money_balance()}", True, (0, 0, 0))
        win.blit(player_money, (600, 250))
        
        plus_one_per_click_button.changeColour(mouse_pos)
        plus_one_per_click_button.update(win)
        back_button.changeColour(mouse_pos)
        back_button.update(win)
        
        pygame.display.flip()  # This was missing!





# Main game function

def gurt_clicker_game(player, gurt, shop_button):

    running = True
    
    while running == True:
        clock.tick(FPS)
        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN: # Check to see if player presses space
                if event.key == pygame.K_ESCAPE:
                    running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if gurt.check_for_input(mouse_pos):
                    player_clicked_gurt(player)
                if shop_button.checkForInput(mouse_pos):
                    gurt_shop(player)
                    return
    
        player_money_balance = player.get_money_balance()

        # Display setup
        player_printable_balance = FONT.render(f"${player_money_balance}", True, (0, 0, 0)) 

        # Display
        win.fill((255, 255, 255))
 
        shop_button.changeColour(mouse_pos)
        shop_button.update(win)
        gurt.change_size_when_hover(mouse_pos)
        gurt.update(win)

        win.blit(player_printable_balance, (300, 300))

        pygame.display.flip()



# Main overall function

def main_game_function():
    #Object creation
    gurt = Gurt()
    player = Player()

    # Button setup
    shop_button_image = pygame.image.load("Assets/Shop Asset for Gurt Clicker (Not original work).png")
    shop_button_image = pygame.transform.scale(shop_button_image, (128, 128))
    shop_button = Button(image=shop_button_image, pos=(640, 460), text_input=None, font=pygame.font.SysFont("comisans", 40), base_colour="Black", hovering_colour="Green")



    gurt_clicker_game(player, gurt, shop_button) 





main_game_function()





pygame.quit()
sys.exit()