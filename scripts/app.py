import pygame
import pygame_gui

import scripts.settings as s
from scripts.UI.button import Button
from scripts.field import Field
from scripts.UI.text import Text


class App:

    def __init__(self) -> None:
        # Initialize pygame and settings
        pygame.init()

        self.size = self.width, self.height = s.SIZE
        self.name = s.NAME
        self.colors = s.COLORS
        self.fps = s.FPS

        # Set pygame window
        pygame.display.set_caption(self.name)

        # Set pygame clock
        self.screen = pygame.display.set_mode(self.size)
        self.clock = pygame.time.Clock()

        # Set pygame GUI
        self.manager = pygame_gui.UIManager(self.size, theme_path="scripts/UI/theme.json")
        self.manager.add_font_paths("fonts/Inter-Regular.ttf", "Inter")
        self.manager.preload_fonts([{'name': 'Inter', 'html_size': 4.5, 'style': 'bold'}])

        # Set input variables
        self.dt = 0
        self.mouse_pos = (0, 0)
        self.keys = []

        # This line takes data from save file
        self.field = Field(self.manager)

        self.fps_text = Text((self.width - 70, self.height - 21), "FPS: ", (0, 0, 0), 14, "Inter-Regular", False)
        # self.button = Button(shape=pygame.Rect((377, 231), (364, 80)),
        #                      background_color=(240, 175, 139),
        #                      hover_color=(246, 205, 183),
        #                      press_color=(252, 215, 197),
        #                      border_color=(0, 0, 0),
        #                      border_width=2,
        #                      content=Text("SINGLEPLAYER", (0, 0, 0), 40, "Inter-Regular")
        #                      )
        # self.button.give_action(lambda: self.field.menu.update("singleplayer_rules"))

    def update(self) -> None:
        """
        Main update function of the program.
        This function is called every frame
        """

        # -*-*- Input Block -*-*-
        self.mouse_pos = pygame.mouse.get_pos()  # Get mouse position

        for event in pygame.event.get():  # Get all events
            if event.type == pygame.QUIT:  # If you want to close the program...
                close()
                Text.fonts = {}  # Clear fonts

            if event.type == pygame.MOUSEBUTTONDOWN:   # If mouse button down...
                if event.button == 1:
                    for button in Button.buttons:
                        button.press()

            if event.type == pygame.MOUSEBUTTONUP:  # If mouse button up...
                if event.button == 1:
                    for button in Button.buttons:
                        button.release()
            #
            # if event.type == pygame.KEYDOWN:  # If key button down...
            #     if event.key == pygame.K_SPACE:
            #         pass

            self.manager.process_events(event)

            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                for i, element in enumerate(self.field.menu.menu_layout[self.field.menu.active_menu]):
                    print(i, element)
                    if event.ui_element == element:
                        print(i)
                        self.field.menu.pressing_button(i)

        self.keys = pygame.key.get_pressed()  # Get all keys (pressed or not)
        # if self.keys[pygame.K_LEFT] or self.keys[pygame.K_a]:
        #     pass
        # -*-*-             -*-*-

        # -*-*- Physics Block -*-*-
        for button in Button.buttons:
            button.update(self.mouse_pos)
        self.fps_text.change_text(f"FPS: {round(self.clock.get_fps())}")
        # -*-*-               -*-*-

        # -*-*- Rendering Block -*-*-
        self.screen.fill(self.colors['background'])  # Fill background

        self.field.draw(self.screen)  # Draw field

        for button in Button.buttons:
            button.draw(self.screen)
        for text in Text.texts:
            text.draw(self.screen)
        # -*-*-                 -*-*-

        # -*-*- Update Block -*-*-
        pygame.display.update()

        self.dt = self.clock.tick(self.fps)
        # -*-*-              -*-*-


def close():
    pygame.quit()
    exit()
