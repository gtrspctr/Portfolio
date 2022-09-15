import pygame
import sys
from datetime import datetime
from os import path
from settings import *
from buttons import *
from characters import *


class Game:
    def __init__(self):
        # Initialize game window, etc.
        pygame.init()
        pygame.display.set_caption(TITLE)
        self.display = pygame.display.set_mode((DISPLAYWIDTH, DISPLAYHEIGHT))
        self.clock = pygame.time.Clock()
        self.game_running = True
        self.loadGameData()


    def loadGameData(self):
        # Define file/folder locations
        game_folder = path.dirname(__file__)
        img_folder = path.join(game_folder, 'images')
        font_folder = path.join(game_folder, 'fonts')
        self.saves_folder = path.join(game_folder, 'saves')

        # Define font
        self.font_name = path.join(font_folder, FONTNAME)

        # Define images
        arrow_right = pygame.image.load(path.join(img_folder, ARROW_R)).convert_alpha()
        arrow_left = pygame.image.load(path.join(img_folder, ARROW_L)).convert_alpha()
        arrow_right_brt = pygame.image.load(path.join(img_folder, ARROW_R_B)).convert_alpha()
        arrow_left_brt = pygame.image.load(path.join(img_folder, ARROW_L_B)).convert_alpha()
        save_button = pygame.image.load(path.join(img_folder, SAVE_BUTT)).convert_alpha()
        save_button_brt = pygame.image.load(path.join(img_folder, SAVE_BUTT_B)).convert_alpha()
        back_button = pygame.image.load(path.join(img_folder, BACK_BUTT)).convert_alpha()
        back_button_brt = pygame.image.load(path.join(img_folder, BACK_BUTT_B)).convert_alpha()
        quit_button = pygame.image.load(path.join(img_folder, QUIT_BUTT)).convert_alpha()
        quit_button_brt = pygame.image.load(path.join(img_folder, QUIT_BUTT_B)).convert_alpha()
        human_pic = pygame.image.load(path.join(img_folder, HUMAN_IMG)).convert_alpha()
        highelf_pic = pygame.image.load(path.join(img_folder, HIGHELF_IMG)).convert_alpha()
        darkelf_pic = pygame.image.load(path.join(img_folder, DARKELF_IMG)).convert_alpha()
        dwarf_pic = pygame.image.load(path.join(img_folder, DWARF_IMG)).convert_alpha()

        # Initialize characters
        ## Dark Elf
        dark_elf = Character(DARKELF_RACE,
                             darkelf_pic,
                             DARKELF_MAXHP,
                             DARKELF_MAXMP,
                             DARKELF_ATK,
                             DARKELF_DEF,
                             DARKELF_MATK,
                             DARKELF_MDEF,
                             DARKELF_SPD)

        ## Dwarf
        dwarf = Character(DWARF_RACE,
                          dwarf_pic,
                          DWARF_MAXHP,
                          DWARF_MAXMP,
                          DWARF_ATK,
                          DWARF_DEF,
                          DWARF_MATK,
                          DWARF_MDEF,
                          DWARF_SPD)

        ## High Elf
        high_elf = Character(HIGHELF_RACE,
                             highelf_pic,
                             HIGHELF_MAXHP,
                             HIGHELF_MAXMP,
                             HIGHELF_ATK,
                             HIGHELF_DEF,
                             HIGHELF_MATK,
                             HIGHELF_MDEF,
                             HIGHELF_SPD)

        ## Human
        human = Character(HUMAN_RACE,
                          human_pic,
                          HUMAN_MAXHP,
                          HUMAN_MAXMP,
                          HUMAN_ATK,
                          HUMAN_DEF,
                          HUMAN_MATK,
                          HUMAN_MDEF,
                          HUMAN_SPD)

        # Add characters to list to iterate thru later
        self.chars = [dark_elf,
                      dwarf,
                      high_elf,
                      human]

        # Initialize buttons        
        ## Arrow right
        self.arrow_r_b = Button(ARROW_R_W,
                              ARROW_R_H,
                              ARROW_R_X1,
                              ARROW_R_X2,
                              ARROW_R_Y1,
                              ARROW_R_Y2,
                              arrow_right,
                              arrow_right_brt)

        ## Arrow left
        self.arrow_l_b = Button(ARROW_L_W,
                              ARROW_L_H,
                              ARROW_L_X1,
                              ARROW_L_X2,
                              ARROW_L_Y1,
                              ARROW_L_Y2,
                              arrow_left,
                              arrow_left_brt)

        ## Save
        self.save_b = Button(SAVE_W,
                             SAVE_H,
                             SAVE_X1,
                             SAVE_X2,
                             SAVE_Y1,
                             SAVE_Y2,
                             save_button,
                             save_button_brt)

        ## Back
        self.back_b = Button(BACK_W,
                             BACK_H,
                             BACK_X1,
                             BACK_X2,
                             BACK_Y1,
                             BACK_Y2,
                             back_button,
                             back_button_brt)

        ## Quit
        self.quit_b = Button(QUIT_W,
                             QUIT_H,
                             QUIT_X1,
                             QUIT_X2,
                             QUIT_Y1,
                             QUIT_Y2,
                             quit_button,
                             quit_button_brt)


    def saveCharacterData(self):
        # Determine which character is currently selected
        # (var 'r'), grab the datetime and create a
        # save file. Write the stats of the chosen character
        # to the file.
        c = self.chars[self.char_counter]
        date = datetime.now().strftime("%Y%m%d-%H.%M.%S.%f")
        self.out_file = (str(c.race) + '_' +
                         str(date) +
                         '.dat')
        with open(path.join(self.saves_folder, self.out_file), 'w', encoding = 'utf-8') as f:
            f.write(str(c.race) + ',' +
                    str(c.max_hp) + ',' +
                    str(c.max_mp) + ',' +
                    str(c.p_atk) + ',' +
                    str(c.p_def) + ',' +
                    str(c.m_atk) + ',' +
                    str(c.m_def) + ',' +
                    str(c.spd))            
        

    def messageToScreen(self, msg, color, size, xDisplace=0, yDisplace=0):
        # Renders font and displays text to the screen
        font = pygame.font.Font(self.font_name, size)
        text_surf = font.render(msg, True, color)
        text_surf.set_alpha(255)
        text_rect = text_surf.get_rect()
        text_rect.center = (DISPLAYWIDTH/2) + xDisplace, (DISPLAYHEIGHT/2) + yDisplace
        self.display.blit(text_surf, text_rect)


    def showStats(self, num):
        # Displays stats for each character to the screen
        self.messageToScreen(num.race,
                             WHITE,
                             MEDIUMFONTSIZE,
                             STAT_RACE_X,
                             STAT_RACE_Y)
        self.messageToScreen(str(num.p_atk),
                             BLUEGREEN,
                             SMALLFONTSIZE,
                             STAT_ATK_X,
                             STAT_ATK_Y)
        self.messageToScreen(str(num.p_def),
                             BLUEGREEN,
                             SMALLFONTSIZE,
                             STAT_DEF_X,
                             STAT_DEF_Y)
        self.messageToScreen(str(num.m_atk),
                             BLUEGREEN,
                             SMALLFONTSIZE,
                             STAT_MATK_X,
                             STAT_MATK_Y)
        self.messageToScreen(str(num.m_def),
                             BLUEGREEN,
                             SMALLFONTSIZE,
                             STAT_MDEF_X,
                             STAT_MDEF_Y)
        self.messageToScreen(str(num.spd),
                             BLUEGREEN,
                             SMALLFONTSIZE,
                             STAT_SPD_X,
                             STAT_SPD_Y)
        self.messageToScreen(str(num.max_hp),
                             BLUEGREEN,
                             SMALLFONTSIZE,
                             STAT_MAXHP_X,
                             STAT_MAXHP_Y)
        self.messageToScreen(str(num.max_mp),
                             BLUEGREEN,
                             SMALLFONTSIZE,
                             STAT_MAXMP_X,
                             STAT_MAXMP_Y)
        self.display.blit(num.img, STAT_IMG_POS)


    def new(self):
        # Var 'menu_type' defines which menu to display.
        # There are two menu types: 'game' and 'save'.
        # Var 'race_counter' is a selecter with which to
        # iterate through 'self.races'.
        self.menu_type = 'game'
        self.char_counter = 0
        self.run()


    def run(self):
        # Main game loop
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            self.events()
            self.draw()


    def events(self):
        # Get events (mouse clicks, key strokes, etc)

        # Get mouse coordinates in (x, y) format
        self.mouse = pygame.mouse.get_pos()

        # Determine which buttons to display ('self.menu_type').
        # Update the buttons to check if mouse is over.
        if self.menu_type == 'game':
            self.arrow_r_b.update(self.mouse)
            self.arrow_l_b.update(self.mouse)
            self.save_b.update(self.mouse)
        else:
            self.back_b.update(self.mouse)
            self.quit_b.update(self.mouse)
        
        # Loop through events and get event type
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONUP and self.arrow_r_b.mouse_over:
                # Mouse press on right arrow, iterate through list of characters
                if self.char_counter == 0:
                    self.char_counter = 1
                elif self.char_counter == 1:
                    self.char_counter = 2
                elif self.char_counter == 2:
                    self.char_counter = 3
                else:
                    self.char_counter = 0
            if event.type == pygame.MOUSEBUTTONUP and self.arrow_l_b.mouse_over:
                # Mouse press on left arrow, iterate through list of characters
                if self.char_counter == 0:
                    self.char_counter = 3
                elif self.char_counter == 1:
                    self.char_counter = 0
                elif self.char_counter == 2:
                    self.char_counter = 1
                else:
                    self.char_counter = 2
            if event.type == pygame.MOUSEBUTTONUP and self.save_b.mouse_over:
                # Mouse press Save button, switch menu type to 'save',
                # and write data to file.
                self.saveCharacterData()
                self.menu_type = 'save'
                self.save_b.mouse_over = False
            if event.type == pygame.MOUSEBUTTONUP and self.back_b.mouse_over:
                # Mouse press Back button, switch menu type back to 'game'
                self.menu_type = 'game'
                self.back_b.mouse_over = False
            if event.type == pygame.MOUSEBUTTONUP and self.quit_b.mouse_over:
                # Mouse press Quit button.
                pygame.quit()
                sys.exit()


    def draw(self):
        # Fill background
        self.display.fill(DARKBLUE)

        # Check if on the character creation menu or the save menu
        if self.menu_type == 'game':
            # Draw buttons
            self.display.blit(self.arrow_r_b.displayed_img,
                              (self.arrow_r_b.x1, self.arrow_r_b.y1))
            self.display.blit(self.arrow_l_b.displayed_img,
                              (self.arrow_l_b.x1, self.arrow_l_b.y1))
            self.display.blit(self.save_b.displayed_img,
                              (self.save_b.x1, self.save_b.y1))

            # Draw text
            self.messageToScreen('Choose thy character', GOLD,
                                 LARGEFONTSIZE, 0, -250)
            self.messageToScreen('ATK', GOLD,
                                 SMALLFONTSIZE, -225, 200)
            self.messageToScreen('DEF', GOLD,
                                 SMALLFONTSIZE, -125, 200)
            self.messageToScreen('M. ATK', GOLD,
                                 SMALLFONTSIZE, 0, 200)
            self.messageToScreen('M.DEF', GOLD,
                                 SMALLFONTSIZE, 125, 200)
            self.messageToScreen('SPD', GOLD,
                                 SMALLFONTSIZE, 225, 200)
            self.messageToScreen('MAX HP', GOLD,
                                 SMALLFONTSIZE, 125, 100)
            self.messageToScreen('MAX MP', GOLD,
                                 SMALLFONTSIZE, 125, 140)
            self.messageToScreen('Select a race', GOLD,
                                 SMALLFONTSIZE, 180, -100)

            # Draw character info
            self.showStats(self.chars[self.char_counter])
        else:
            # Verify data was saved
            if path.exists(path.join(self.saves_folder, self.out_file)):
                self.messageToScreen('Character data saved', GOLD,
                                     MEDIUMFONTSIZE, 0, -200)
            else:
                self.messageToScreen('Data was not saved', GOLD,
                                     MEDIUMFONTSIZE, 0, -200)
            # Draw buttons
            self.display.blit(self.back_b.displayed_img,
                              (self.back_b.x1, self.back_b.y1))
            self.display.blit(self.quit_b.displayed_img,
                              (self.quit_b.x1, self.quit_b.y1))


        pygame.display.update()


# Initialize game
g = Game()
while g.game_running:
    g.new()
