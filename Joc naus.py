import time
from pygame.locals import *
import pygame

AMPLADA = 800
ALTURA = 600
BACKGROUND_IMAGE = 'assets/fons.png'
MUSICA_FONS = 'assets/music.mp3'
MUSICA_MENU = 'assets/musicmenu.mp3'
SO_BALA = 'assets/bala.wav'
WHITE = (255,255,255)
MAGENTA = (255,0,255)
BLUE = (0,0,255)
BLACK  = (0,0,0)
guanyador = 0

#Pantalles del joc
#Pantalla 1 - Menú
#Pantalla 2 - Crèdits
#Pantalla 3 - Joc
#Pantalla 4 - Game Over
pantalla_actual = 1


# Jugador 1:
player_image = pygame.image.load('assets/nau.png')
player_rect = player_image.get_rect(midbottom=(AMPLADA // 2, ALTURA - 10))
velocitat_nau = 6


# Jugador 2:
player_image2 = pygame.image.load('assets/nau2.png')
player_rect2 = player_image2.get_rect(midbottom=(AMPLADA // 2, ALTURA - 790))
velocitat_nau2 = 6


# vides:
vides1 = 3
vides2 = 3
vida_image1 = pygame.image.load('assets/cor.png')
vida1_jugador1 = vida_image1.get_rect(midbottom=(780,590))
vida2_jugador1 = vida_image1.get_rect(midbottom=(760,590))
vida3_jugador1 = vida_image1.get_rect(midbottom=(740,590))

vida_image2 = pygame.image.load('assets/cor2.png')
vida1_jugador2 = vida_image2.get_rect(midbottom=(20,40))
vida2_jugador2 = vida_image2.get_rect(midbottom=(40,40))
vida3_jugador2 = vida_image2.get_rect(midbottom=(60,40))

# Bala rectangular blanca:
bala_imatge = pygame.image.load('assets/bala.png') #definim una superficie rectangle de 4 pixels d'ample i 10 d'alçada

bales_jugador1 = [] #llista on guardem les bales del jugador 1
bales_jugador2 = [] #llista on guardem les bales del jugador 2
velocitat_bales = 10
temps_entre_bales = 250 #1 segon
temps_ultima_bala_jugador1 = 0 #per contar el temps que ha passat des de que ha disparat el jugador 1
temps_ultima_bala_jugador2 = 0 #per contar el temps que ha passat des de que ha disparat el jugador 2


pygame.init()
pantalla = pygame.display.set_mode((AMPLADA, ALTURA),pygame.FULLSCREEN)
pygame.display.set_caption("Arcade")

pygame.init()
ambient_music = pygame.mixer.Sound('assets/musicmenu .mp3')
ambient_music.play()

# Control de FPS
clock = pygame.time.Clock()
fps = 60

def imprimir_pantalla_fons(image):
    # Imprimeixo imatge de fons:
    background = pygame.image.load(image).convert()
    pantalla.blit(background, (0, 0))
def show_menu():
    imprimir_pantalla_fons("assets/fonsmenu.png")
def show_credits():
    imprimir_pantalla_fons("assets/credits.png")
    text0 = "SPACE KING"
    text1 = "Programació:"
    text2 = "Gràfics:"
    text3 = "Música:"
    text4 = "Sons:"
    text5 = "Pau del C.(Xavi Sancho)"
    text6 = "Dimrain47-At the Speed of Light"
    text7 = "Freesound.org"
    text8 = "Esc = Quit"
    font0 = pygame.font.SysFont(None, 100)
    font1 = pygame.font.SysFont(None, 60)
    font2 = pygame.font.SysFont(None, 50)
    img0 = font0.render(text0, True, BLUE)
    img1 = font1.render(text1, True, MAGENTA)
    img2 = font1.render(text2, True, MAGENTA)
    img3 = font1.render(text3, True, MAGENTA)
    img4 = font1.render(text4, True, MAGENTA)
    img5 = font2.render(text5, True, BLUE)
    img6 = font2.render(text6, True, BLUE)
    img7 = font2.render(text7, True, BLUE)
    img8 = font1.render(text8, True, BLUE)
    pantalla.blit(img0, (240, 90))
    pantalla.blit(img1, (220, 180))
    pantalla.blit(img5, (220, 220))
    pantalla.blit(img2, (220, 270))
    pantalla.blit(img5, (220, 310))
    pantalla.blit(img3, (220, 350))
    pantalla.blit(img6, (220, 390))
    pantalla.blit(img4, (220, 430))
    pantalla.blit(img7, (220, 470))
    pantalla.blit(img8,(500,450))

while True:
    #contador
    current_time = pygame.time.get_ticks()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if pantalla_actual == 2:
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
        if pantalla_actual == 1:
            if event.type == KEYDOWN:
                if event.key == K_3:
                    pygame.quit()
                if event.key == K_1:
                    pantalla_actual = 2
                if event.key == K_2:
                    ambient_music.stop()
                    ambient_music = pygame.mixer.Sound('assets/music.mp3')
                    ambient_music.play()
                    pantalla_actual = 3
        if pantalla_actual == 4:
            ambient_music.stop()
            pygame.mixer.music.load('assets/explosio.wav')
            pygame.mixer.music.play()
           
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    vides1 = 3
                    vides2 = 3
                    pantalla_actual = 1
                    for i in bales_jugador1:
                        bales_jugador1.remove(i)
                    for i in bales_jugador2:
                        bales_jugador2.remove(i)
        if pantalla_actual==3:
            pygame
            # controlar trets de les naus
            if event.type == KEYDOWN:
                #jugador 1
                if event.key == K_w and current_time - temps_ultima_bala_jugador1 >= temps_entre_bales:
                    bales_jugador1.append(pygame.Rect(player_rect.centerx - 2, player_rect.top, 4, 10))
                    temps_ultima_bala_jugador1 = current_time
                    ambient_music = pygame.mixer.Sound('assets/bala.wav')
                    ambient_music.play()
                # jugador 2
                if event.key == K_UP and current_time - temps_ultima_bala_jugador2 >= temps_entre_bales:
                    bales_jugador2.append(pygame.Rect(player_rect2.centerx - 2, player_rect2.bottom -10, 4, 10))
                    temps_ultima_bala_jugador2 = current_time
                    ambient_music = pygame.mixer.Sound('assets/bala.wav')
                    ambient_music.play()

    if pantalla_actual == 1:
        show_menu()
    if pantalla_actual == 2:
        show_credits()
    if pantalla_actual == 4:

        imprimir_pantalla_fons('assets/gameover.png')
        text = "Player " + str(guanyador) + ' Wins!'
        font = pygame.font.SysFont(None, 64)
        img = font.render(text, True, BLACK)
        pantalla.blit(img, (300,440))
    if pantalla_actual == 3:

        # Moviment del jugador 1
        keys = pygame.key.get_pressed()
        if keys[K_a]:
            player_rect.x -= velocitat_nau
        if keys[K_d]:
            player_rect.x += velocitat_nau
        # Moviment del jugador 2
        if keys[K_LEFT]:
            player_rect2.x -= velocitat_nau2
        if keys[K_RIGHT]:
            player_rect2.x += velocitat_nau2



        # Mantenir al jugador dins de la pantalla:
        player_rect.clamp_ip(pantalla.get_rect())
        player_rect2.clamp_ip(pantalla.get_rect())

        #dibuixar el fons:
        imprimir_pantalla_fons(BACKGROUND_IMAGE)

        #Actualitzar i dibuixar les bales del jugador 1:
        for bala in bales_jugador1: # bucle que recorre totes les bales

            bala.y -= velocitat_bales # mou la bala

            if bala.bottom < 0 or bala.top > ALTURA: # comprova que no ha sortit de la pantalla
                bales_jugador1.remove(bala) # si ha sortit elimina la bala
            else:
                pantalla.blit(bala_imatge, bala) # si no ha sortit la dibuixa
            # Detectar col·lisions jugador 2:
            if player_rect2.colliderect(bala):  # si una bala toca al jugador1 (el seu rectangle)
                print("BOOM 1!")
                vides2 = vides2 - 1
                bales_jugador1.remove(bala)  # eliminem la bala
                # mostrem una explosió
                # eliminem el jugador 1 (un temps)
                # anotem punts al jugador 1

        # Actualitzar i dibuixar les bales del jugador 2:
        for bala in bales_jugador2:
            bala.y += velocitat_bales
            if bala.bottom < 0 or bala.top > ALTURA:
                bales_jugador2.remove(bala)
            else:
                pantalla.blit(bala_imatge, bala)
            # Detectar col·lisions jugador 1:
            if player_rect.colliderect(bala):  # si una bala toca al jugador1 (el seu rectangle)
                print("BOOM 2!")
                bales_jugador2.remove(bala)  # eliminem la bala
                vides1 = vides1 - 1

                # mostrem una explosió
                # eliminem el jugador 1 (un temps)
                # anotem punts al jugador 1

        #dibuixar els jugadors:
        pantalla.blit(player_image, player_rect)
        pantalla.blit(player_image2, player_rect2)

        #dibuixar vides:
        if vides1 >= 1:
            pantalla.blit(vida_image1, vida1_jugador1)
        if vides1 >= 2:
            pantalla.blit(vida_image1, vida2_jugador1)
        if vides1 == 3:
            pantalla.blit(vida_image1, vida3_jugador1)
        if vides2 >= 1:
            pantalla.blit(vida_image2, vida1_jugador2)
        if vides2 >= 2:
            pantalla.blit(vida_image2, vida2_jugador2)
        if vides2 == 3:
            pantalla.blit(vida_image2, vida3_jugador2)




        if vides1 <=0 or vides2 <=0:
            guanyador = 1
            if vides1 <=0:
                guanyador = 2

            pantalla_actual = 4

    pygame.display.update()
    clock.tick(fps)