import pygame

SIZE = [1080, 720]
NAME = "Memory"
FPS = 0  # 0 - unlimited
COLORS = {
    "background": (255, 227, 211),
    "button_primary_background": (240, 175, 139),
    "button_primary_hover": (252, 198, 167),
    "button_primary_press": (252, 215, 197),
    "button_border": (0, 0, 0),
    "button_exit_background": (240, 145, 139),
    "button_exit_hover": (246, 175, 183),
    "button_exit_press": (252, 185, 197),
    "button_play_background": (240, 206, 139),
    "button_play_hover": (246, 216, 183),
    "button_play_press": (252, 226, 197),
    "second_background": (246, 205, 183),
    "text_primary": (0, 0, 0),
}

FONTS = "JosefinSans-Regular"

SPRITES = {
    "logo": pygame.image.load("./sprites/logo.png"),
    "background": pygame.image.load("./sprites/background.png"),
    "singleplayer": pygame.image.load("./sprites/singleplayer.png"),
    "multiplayer": pygame.image.load("./sprites/multiplayer.png"),
    "settings": pygame.image.load("./sprites/settings.png"),
    "exit": pygame.image.load("./sprites/exit.png"),
    "size": pygame.image.load("./sprites/size.png"),
    "card_connection": pygame.image.load("./sprites/card_connection.png"),
    "move": pygame.image.load("./sprites/move.png"),
    "time": pygame.image.load("./sprites/time.png"),
    "random": pygame.image.load("./sprites/random.png"),
    "start_game": pygame.image.load("./sprites/start_game.png"),
    "left_click": pygame.image.load("./sprites/left_click.png"),
    "right_click": pygame.image.load("./sprites/right_click.png"),
    "slider": pygame.image.load("./sprites/slider.png"),
}
