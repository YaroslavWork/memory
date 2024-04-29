import pygame


# Class Text - represents text in the model (this class optimizes the use of fonts and a text surface
# because pygame.font.Font is very slow)
class Text:
    fonts = {}  # Dictionary of fonts
    texts = []

    def __init__(self, position, text, color, size_font, type_font=None, position_center=True) -> None:
        if size_font in Text.fonts:
            self.font = Text.fonts[size_font]
        else:
            if type_font:
                self.font = pygame.font.Font("fonts/" + type_font + ".ttf", size_font)
            else:
                self.font = pygame.font.Font(None, size_font)
            Text.fonts[size_font] = self.font
        self.text_surface = self.font.render(text, True, color)

        self.position = position
        self.position_center = position_center
        self.is_visible = True

        Text.texts.append(self)

    def __del__(self):
        Text.texts.remove(self)

    def change_text(self, text):
        self.text_surface = self.font.render(text, True, self.text_surface.get_at((0, 0)))

    def draw(self, screen) -> None:
        if self.is_visible:
            if self.position_center:
                screen.blit(self.text_surface, self.text_surface.get_rect(center=self.position))
            else:
                screen.blit(self.text_surface, self.position)

    def show(self):
        self.is_visible = True

    def hide(self):
        self.is_visible = False
