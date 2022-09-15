# Display
DISPLAYWIDTH = 600
DISPLAYHEIGHT = 600
FPS = 60
TITLE = 'Character Generator'

# Colors
WHITE = (255,255,255)
BLACK = (000,000,000)
GRAY = (155,155,155)
RED = (255,000,000)
GREEN = (000,255,000)
BLUE = (000,000,255)
GOLD = (255,215,000)
BLUEGREEN = (000,255,255)
DARKBLUE = (20,40,90)
PURPLE = (255,000,255)

# Fonts
FONTNAME = 'Breathe Fire.otf'
LARGEFONTSIZE = 60
MEDIUMFONTSIZE = 50
SMALLFONTSIZE = 30

# Layers
WALLLAYER = 1
IMGLAYER = 2
TXTLAYER = 3

# Image files
ARROW_R = 'CharacterGenArrowRight.png'
ARROW_L = 'CharacterGenArrowLeft.png'
ARROW_R_B = 'CharacterGenArrowRight_Bright.png'
ARROW_L_B = 'CharacterGenArrowLeft_Bright.png'
SAVE_BUTT = 'CharacterGenSave2.png'
SAVE_BUTT_B = 'CharacterGenSave2_Bright.png'
BACK_BUTT = 'CharacterGenBack.png'
BACK_BUTT_B = 'CharacterGenBack_Bright.png'
QUIT_BUTT = 'CharacterGenQuit.png'
QUIT_BUTT_B = 'CharacterGenQuit_Bright.png'

# Image positions
## Arrow Right
ARROW_R_W = 90
ARROW_R_H = 40
ARROW_R_X1 = 485
ARROW_R_X2 = ARROW_R_X1 + ARROW_R_W
ARROW_R_Y1 = 225
ARROW_R_Y2 = ARROW_R_Y1 + ARROW_R_H

## Arrow Left
ARROW_L_W = 90
ARROW_L_H = 40
ARROW_L_X1 = 385
ARROW_L_X2 = ARROW_L_X1 + ARROW_L_W
ARROW_L_Y1 = 225
ARROW_L_Y2 = ARROW_L_Y1 + ARROW_L_H

## Save
SAVE_W = 150
SAVE_H = 50
SAVE_X1 = 406
SAVE_X2 = SAVE_X1 + SAVE_W
SAVE_Y1 = 301
SAVE_Y2 = SAVE_Y1 + SAVE_H

## Back
BACK_W = 150
BACK_H = 50
BACK_X1 = (DISPLAYWIDTH / 2) - 200
BACK_X2 = BACK_X1 + BACK_W
BACK_Y1 = (DISPLAYHEIGHT / 2) + 150
BACK_Y2 = BACK_Y1 + BACK_H

## Quit
QUIT_W = 150
QUIT_H = 50
QUIT_X1 = (DISPLAYWIDTH / 2) + 50
QUIT_X2 = QUIT_X1 + QUIT_W
QUIT_Y1 = (DISPLAYHEIGHT / 2) + 150
QUIT_Y2 = QUIT_Y1 + QUIT_H

# Characters
## Dark Elf
DARKELF_RACE = 'Dark Elf'
DARKELF_IMG = 'CharacterGenDarkElf.png'
DARKELF_MAXHP = 25
DARKELF_MAXMP = 15
DARKELF_ATK = 5
DARKELF_DEF = 5
DARKELF_MATK = 5
DARKELF_MDEF = 5
DARKELF_SPD = 10

## Dwarf
DWARF_RACE = 'Dwarf'
DWARF_IMG = 'CharacterGenDwarf.png'
DWARF_MAXHP = 25
DWARF_MAXMP = 0
DWARF_ATK = 12
DWARF_DEF = 8
DWARF_MATK = 0
DWARF_MDEF = 0
DWARF_SPD = 4

## High Elf
HIGHELF_RACE = 'High Elf'
HIGHELF_IMG = 'CharacterGenHighElf.png'
HIGHELF_MAXHP = 20
HIGHELF_MAXMP = 30
HIGHELF_ATK = 3
HIGHELF_DEF = 3
HIGHELF_MATK = 10
HIGHELF_MDEF = 10
HIGHELF_SPD = 12

## Human
HUMAN_RACE = 'Human'
HUMAN_IMG = 'CharacterGenHuman.png'
HUMAN_MAXHP = 30
HUMAN_MAXMP = 0
HUMAN_ATK = 10
HUMAN_DEF = 10
HUMAN_MATK = 0
HUMAN_MDEF = 0
HUMAN_SPD = 10

# Stats info and positions
## Race name
STAT_RACE_X = -100
STAT_RACE_Y = 140

## Physical Attack
STAT_ATK_X = -225
STAT_ATK_Y = 250

## Physical Defense
STAT_DEF_X = -125
STAT_DEF_Y = 250

## Magic Attack
STAT_MATK_X = 0
STAT_MATK_Y = 250

## Magic Defense
STAT_MDEF_X = 125
STAT_MDEF_Y = 250

## Speed
STAT_SPD_X = 225
STAT_SPD_Y = 250

## Max HP
STAT_MAXHP_X = 225
STAT_MAXHP_Y = 100

## Max MP
STAT_MAXMP_X = 225
STAT_MAXMP_Y = 140

## Character Image
STAT_IMG_POS = ((DISPLAYWIDTH / 2) -250, (DISPLAYHEIGHT / 2) - 209)
