class Settings():
    """Essa classe armazena todas as configurações do jogo"""

    def __init__(self):
        """Inicializa as configurações"""

        #tela
        self.screen_width = 1200
        self.screen_height = 700
        self.bg_color = (17, 8, 55)
        # ship
        self.ship_speed_factor = 1.5
        # bullets
        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
        # aliens
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        #fleet_direction igual a 1 = direita; -1 = esquerda
        self.fleet_direction = 1