import pygame, sys
import sprite
from button import Button
import time

pygame.init()

SCREEN = pygame.display.set_mode((600, 600))
pygame.display.set_caption("MrBEST CHESS")

py_icon = pygame.image.load('assets/icon.png')
pygame.display.set_icon(py_icon)

BG = pygame.image.load("assets/Background.png")

intro = pygame.image.load("assets/intro_max.png")
sprite_intro = sprite.SpriteSheet(intro)

mrbest_sprite_image = pygame.image.load("assets/mrbeest.png").convert_alpha()
sprite_sheet = sprite.SpriteSheet(mrbest_sprite_image)

#music and sounds
button_sound = pygame.mixer.Sound("assets/mouse_button1.ogg")
sound = pygame.mixer.Sound("assets/music.ogg")
volume = 0.5
sound.set_volume(volume)
mute_sound = 0

#animation
animation_list1 = []
animation_beast = 3

animation_list2 = []
animation_intro = 56

last_update = pygame.time.get_ticks()
animation_cooldown1 = 50

new_update = pygame.time.get_ticks()
animation_cooldown2 = 100
frame1 = 0
frame2 = 0

for x in range(animation_intro):
    animation_list1.append(sprite_intro.get_image(x, 750, 420, "black"))

for x in range(animation_beast):
    animation_list2.append(sprite_sheet.get_image(x, 600, 600, "black"))


def get_font(size):
    return pygame.font.Font("assets/Stargod.ttf", size)

def get_font1(size):
    return pygame.font.Font("assets/DePixelBreit.ttf", size)

def play():

    #Dito mo call yung chess

    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")

        #buttons
        PLAY_TEXT = get_font(45).render("This is the PLAY screen.", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(300, 260))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        PLAY_BACK = Button(image=None, pos=(300, 400), text_input="BACK", font=get_font(30), base_color="White", hovering_color="Green")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    button_sound.play()
                    main_menu()

        pygame.display.update()

def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")

        OPTIONS_TEXT = get_font(45).render("Music", True, "Black")

        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(300, 250))

        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        #buttons
        OPTIONS_BACK = Button(image=None, pos=(300, 400), text_input="BACK", font=get_font(30), base_color="Black", hovering_color="Green")
        OPTIONS_MUTE = Button(image=None, pos=(220, 320), text_input="Mute", font=get_font(45), base_color="Black",hovering_color="Red")
        OPTIONS_UNMUTE = Button(image=None, pos=(370, 320), text_input="Unmute", font=get_font(45), base_color="Black",hovering_color="Green")

        OPTIONS_UNMUTE.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_UNMUTE.update(SCREEN)

        OPTIONS_MUTE.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_MUTE.update(SCREEN)

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_MUTE.checkForInput(OPTIONS_MOUSE_POS):
                    sound.set_volume(mute_sound)
                if OPTIONS_UNMUTE.checkForInput(OPTIONS_MOUSE_POS):
                    sound.set_volume(volume)
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    button_sound.play()
                    main_menu()

        pygame.display.update()

def main_menu():

    global new_update, frame2

    while True:

        SCREEN.fill("black")

        #update animation
        current_time = pygame.time.get_ticks()
        if current_time - new_update >= animation_cooldown2:
            frame2 += 1
            new_update = current_time
            if frame2 >= len(animation_list2):
                frame2 = 0

        #show frame image
        SCREEN.blit(animation_list2[frame2], (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(80).render("MrBest Chess", True, "#90BED4")

        MENU_RECT = MENU_TEXT.get_rect(center=(300, 200))

        #buttons
        PLAY_BUTTON = Button(image=None, pos=(300, 300), text_input="PLAY", font=get_font1(30), base_color="white", hovering_color="White")
        OPTIONS_BUTTON = Button(image=None, pos=(300, 350), text_input="OPTIONS", font=get_font1(30), base_color="white", hovering_color="White")
        QUIT_BUTTON = Button(image=None, pos=(300, 400), text_input="QUIT", font=get_font1(30), base_color="white", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    button_sound.play()
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    button_sound.play()
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

def intro_beast():
    global last_update, frame1, sound

    time.sleep(1)

    while True:

        SCREEN.fill("black")
        current_time = pygame.time.get_ticks()
        if current_time - last_update >= animation_cooldown1:
            frame1 += 1
            last_update = current_time
            if frame1 >= len(animation_list1):

                time.sleep(2)

                sound.play()
                main_menu()


        SCREEN.blit(animation_list1[frame1], (-65, 80))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
intro_beast()