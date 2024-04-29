import pygame
from enum import Enum

from scripts.UI.text import Text


class ButtonStatus(Enum):
    IDLE = 1
    HOVER = 2
    CLICKING = 3

class Button:
    buttons = []

    def __init__(self, shape: [pygame.Rect, tuple[float, float] | list[float, float]],
                 background_color: (int, int, int),
                 hover_color: (int, int, int),
                 press_color: (int, int, int),
                 border_color: (int, int, int),
                 border_width: int = 1,
                 content: [Text, pygame.surface.Surface] = None,
                 content_center = None,
                 is_enable: bool = True,
                 is_visible: bool = True) -> None:
        self.is_enable = is_enable
        self.is_visible = is_visible

        self.shape = shape

        self.background_color = background_color
        self.hover_color = hover_color
        self.press_color = press_color
        self.border_color = border_color

        self.border_width = border_width
        self.content = content
        self.content_center = content_center

        self.__status = ButtonStatus.IDLE
        self.__clicking = False

        self.function = lambda: ...

        if self.content_center:
            if type(self.content) == Text:
                self.content.position = self.content_center

        Button.buttons.append(self)

    def __del__(self):
        Button.buttons.remove(self)

    def give_action(self, function) -> None:
        self.function = function

    def is_collide(self, mouse_position: (float, float)) -> bool:
        if type(self.shape) == pygame.Rect:
            return pygame.Rect.colliderect(self.shape, pygame.Rect(*mouse_position, 1, 1))
        else:
            raise NotImplementedError("Check collision for polygon is not implemented")

    def change_position(self, position: (float, float)) -> None:
        if type(self.shape) == pygame.Rect:
            self.shape.topleft = position
        else:
            raise NotImplementedError("Change position for polygon is not implemented")

        if self.content:
            if type(self.content) == Text:
                self.content.position = position
            else:
                center = self.shape.center[0] - self.content.get_width() // 2, \
                            self.shape.center[1] - self.content.get_height() // 2
                self.content_center = center

    def draw(self, screen: pygame.surface):
        if self.is_visible:
            if type(self.shape) == pygame.Rect:
                # Fill
                if self.__status == ButtonStatus.CLICKING:  # if button is pressing
                    pygame.draw.rect(screen, self.press_color, self.shape)
                elif self.__status == ButtonStatus.HOVER:
                    pygame.draw.rect(screen, self.hover_color, self.shape)
                else:
                    pygame.draw.rect(screen, self.background_color, self.shape)

                # Corner
                pygame.draw.rect(screen, self.border_color, self.shape, self.border_width)
            else:
                raise NotImplementedError("Show button for polygon is not implemented")

            if self.content:
                if type(self.content) == pygame.surface.Surface:
                    if type(self.shape) == pygame.Rect:
                        if self.content_center:
                            screen.blit(self.content, self.content_center)
                        else:
                            center = self.shape.center[0] - self.content.get_width() // 2, \
                                     self.shape.center[1] - self.content.get_height() // 2
                            screen.blit(self.content, center)
                    else:
                        if self.content_center:
                            screen.blit(self.content, self.content_center)
                        else:
                            raise AttributeError("Center of content is not defined. Please, define content_center: ("
                                                 "float, float)")

    def update(self, mouse_position: (float, float)):
        if type(self.shape) == pygame.Rect:
            if self.__status != ButtonStatus.IDLE and self.__clicking:
                self.__status = ButtonStatus.CLICKING
            elif self.is_collide(mouse_position):  # if mouse hovering in button
                self.__status = ButtonStatus.HOVER
            else:
                self.__status = ButtonStatus.IDLE
        else:
            raise NotImplementedError("Update button for polygon is not implemented")

    def press(self):
        if self.is_enable and self.__status == ButtonStatus.HOVER:
            self.__clicking = True

    def release(self):
        if self.is_enable and self.__status == ButtonStatus.CLICKING:
            self.function()
        self.__clicking = False

    def enable(self):
        self.is_enable = True
        if type(self.content) == Text:
            self.content.show()

    def disable(self):
        self.is_enable = False
        if type(self.content) == Text:
            self.content.hide()

    def show(self):
        self.is_visible = True

    def hide(self):
        self.is_visible = False