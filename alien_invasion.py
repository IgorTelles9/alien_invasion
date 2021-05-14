""" Módulo onde o jogo roda """

import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
    """ Inicializa o jogo e cria um objeto para a tela """
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    ship = Ship(ai_settings, screen)
    # cria um grupo no qual serão armazenados os projéteis
    bullets = Group()
    # cria um grupo no qual serão armazenados os alienígena
    aliens = Group()

    # cria a frota de aliens
    gf.create_fleet(ai_settings, screen, ship, aliens)


    # inicia o laço principal do jogo
    while True:
        # observa eventos de teclado e mouse
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(aliens, bullets)
        gf.update_aliens(ai_settings, aliens)


        gf.update_screen(ai_settings, screen, ship, aliens, bullets)
        #print(len(aliens))


run_game()
