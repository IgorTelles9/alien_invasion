import pygame

class Ship():
    def __init__(self,ai_settings ,screen):
        """ Inicializa a nave e define a posição inicial """
        self.screen = screen
        self.ai_settings = ai_settings

        # carrega a imagem da nave e obtém seu rect
        self.image = pygame.image.load('images/ship_1.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # inicia a nave na parte inferior central da tela
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # armazena um valor decimal para o centro da nave
        self.center = float(self.rect.centerx)

        # flag de movimento
        self.moving_right = False
        self.moving_left = False


    def update (self):
        """ Atualiza a posição da nave de acordo com as flags de movimento """

        # Atualiza o valor do centro da nave, e não o retângulo
        if self.moving_right and self.rect.right <  self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        # atualiza o retângulo de acordo com o self.center
        self.rect.centerx = self.center


    def blitme(self):
        """ Desenha a nave em sua posição atual """
        self.screen.blit(self.image, self.rect)