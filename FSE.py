# FSE
# Night of the Invaders
# Salman Chowdhury - [ STUDENT ]
# Gr. 11
#Mr.McKenzie - [ TEACHER ]
# [ START DATE ] - Monday, April 8, 2019
# [ DUE DATE ] - Friday, June 14, 2019
# Enjoy the game

from pygame import *
from math import *
from random import *

init()

size = width, height = 1152, 670
screen = display.set_mode(size)

display.set_caption("Night of the Invaders")

song = mixer.Sound('music\\bg_music.wav')
song.play(loops=-1)

myClock = time.Clock()

# Default initial position of the good guy
goodX, goodY = 0, 0

# My Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (190, 190, 0)
LIGHT_YELLOW = (255, 255, 0)
TURQUOISE = (0, 191, 255)
GRAY = (224, 244, 244)
DARKRED = (139, 0, 0)
MAGENTA = (153, 0, 153)
SKYBLUE = (153, 255, 255)

# Positions
X = 0
Y = 1
VX = 2
VY = 3

# Lists to store bullet values
bullet = []
jet_bullets = []

# Cooldown for weapons
cooldown = 0
cooldown_enemy = 0

# Font for in-game title
font.init()
myfont = font.SysFont('Comic Sans MS', 50, bold=True)
textsurface = myfont.render(' Night of the Invaders', True, (0, 0, 0))

# Health/Shield of all characters
soldier_HEALTH = 200
soldier_SHIELD = 200
jet_HEALTH = 9
birds_HEALTH = 4

soldier_HEALTH_colour = GREEN
soldier_SHIELD_colour = BLUE
enemy_tot_colour = DARKRED

# Used for counting number of jets/birds killed
num_jet = 0
num_birds = 0

# Number of enemies total
enemy_tot = 200


def distance(x1, y1, x2, y2):
    return ((x1-x2)**2 + (y1-y2)**2)**0.5


def running():  # EVENT LOOP
    for evnt in event.get():
        if evnt.type == QUIT:
            return False

    return True


################################   MENU    ##########################################

# To create my texts in menu (for ' def(intro) ', WHITE font)
def text_obj_W(text, font):
    textSurface = font.render(text, True, WHITE)
    return textSurface, textSurface.get_rect()

# To create my texts in menu (for ' def(intro) ', TURQUOISE font)


def text_obj_T(text, font):
    textSurface = font.render(text, True, TURQUOISE)
    return textSurface, textSurface.get_rect()

# To create my texts in menu (for ' def(intro) ', BLACK font)


def text_obj_B(text, font):
    textSurface = font.render(text, True, BLACK)
    return textSurface, textSurface.get_rect()

# To create my texts in menu (for ' def(intro) ', MAGENTA font)


def text_obj_M(text, font):
    textSurface = font.render(text, True, MAGENTA)
    return textSurface, textSurface.get_rect()

# Menu / Intro Interface


def intro():
    global page

    screen.blit(menu_bg, (0, 0))

    # Types of text
    main_text = font.Font('freesansbold.ttf', 100)
    small_text = font.Font('freesansbold.ttf', 30)

    # Title Display
    Text_Surf, Text_Rect = text_obj_W('Night of the Invaders', main_text)
    Text_Rect.center = ((width//2), (height//6))
    screen.blit(Text_Surf, Text_Rect)

    if 420+300 > mx > 420 and 300 + 82 > my > 300:  # PLAY colour when hovered upon
        draw.rect(screen, LIGHT_YELLOW, (420, 300, 300, 82))
    else:
        draw.rect(screen, YELLOW, (420, 300, 300, 82))

    if 420+300 > mx > 420 and 425+60 > my > 425:  # INSTRUCTIONS colour when hovered upon
        draw.rect(screen, LIGHT_YELLOW, (420, 425, 300, 60))
    else:
        draw.rect(screen, YELLOW, (420, 425, 300, 60))

    if 420+300 > mx > 420 and 520+60 > my > 520:  # CREDITS colour when hovered upon
        draw.rect(screen, LIGHT_YELLOW, (420, 520, 300, 60))
    else:
        draw.rect(screen, YELLOW, (420, 520, 300, 60))

    if 420+300 > mx > 420 and 605+60 > my > 605:  # EXIT colour when hovered upon
        draw.rect(screen, LIGHT_YELLOW, (420, 605, 300, 60))
    else:
        draw.rect(screen, YELLOW, (420, 605, 300, 60))

    # RECT OUTLINES
    draw.rect(screen, BLACK, (420, 300, 300, 82), 4)
    draw.rect(screen, BLACK, (420, 425, 300, 60), 4)
    draw.rect(screen, BLACK, (420, 520, 300, 60), 4)
    draw.rect(screen, BLACK, (420, 605, 300, 60), 4)

    # PLAY
    Text_Surf, Text_Rect = text_obj_T('PLAY', small_text)
    Text_Rect.center = ((420+(300/2)), (300+(82/2)))
    screen.blit(Text_Surf, Text_Rect)

    # INSTRUCTIONS
    Text_Surf, Text_Rect = text_obj_B('INSTRUCTIONS', small_text)
    Text_Rect.center = ((420+(300/2)), (425+(60/2)))
    screen.blit(Text_Surf, Text_Rect)

    # CREDITS
    Text_Surf, Text_Rect = text_obj_B('CREDITS', small_text)
    Text_Rect.center = ((420+(300/2)), (520+(60/2)))
    screen.blit(Text_Surf, Text_Rect)

    # EXIT
    Text_Surf, Text_Rect = text_obj_B('EXIT', small_text)
    Text_Rect.center = ((420+(300/2)), (605+(60/2)))
    screen.blit(Text_Surf, Text_Rect)

    #Functions for buttons#

    if 420+300 > mx > 420 and 300+82 > my > 300 and mb[0] == 1:
        return None
    # Instructions
    if 420+300 > mx > 420 and 425+60 > my > 425:
        if mb[0] == 1:
            screen.blit(instructions, (0, 0))

    # Credits
    if 420+300 > mx > 420 and 520+60 > my > 520:
        if mb[0] == 1:
            screen.blit(Credits, (0, 0))
    # Exit
    if 420+300 > mx > 420 and 605+60 > my > 605 and mb[0] == 1:
        quit()

    mouse.set_visible(True)

    display.flip()
    return "intro"

#######################################################################################


###############################    IN-GAME     #######################################

# Show this when you outnumber the enemies
def outlast():

    outlast_text_big = font.Font('freesansbold.ttf', 100)
    outlast_text_small = font.Font('freesansbold.ttf', 50)

    Text_Surf_big, Text_Rect_big = text_obj_M('VICTORY', outlast_text_big)
    Text_Surf_small, Text_Rect_small = text_obj_B(
        'YOU OUTNUMBERED THE ENEMIES ', outlast_text_small)

    Text_Rect_big.center = ((width//2), (height//2))
    Text_Rect_small.center = ((width//2), 500)
    outlast = True

    while outlast:
        for e in event.get():
            if e.type == QUIT:
                quit()

        screen.blit(Text_Surf_big, Text_Rect_big)
        screen.blit(Text_Surf_small, Text_Rect_small)

        display.flip()

# Show this when you win


def win():

    win_text_big = font.Font('freesansbold.ttf', 100)
    win_text_small = font.Font('freesansbold.ttf', 50)

    Text_Surf_big, Text_Rect_big = text_obj_M('VICTORY', win_text_big)
    Text_Surf_small, Text_Rect_small = text_obj_B(
        'YOU KILLED ALL THE ENEMIES ', win_text_small)

    Text_Rect_big.center = ((width//2), (height//2))
    Text_Rect_small.center = ((width//2), 500)
    pause = True

    while win:
        for e in event.get():
            if e.type == QUIT:
                quit()

        screen.blit(Text_Surf_big, Text_Rect_big)
        screen.blit(Text_Surf_small, Text_Rect_small)

        display.flip()

# Show this when you lose


def game_over():

    game_over_text_big = font.Font('freesansbold.ttf', 100)
    game_over_text_small = font.Font('freesansbold.ttf', 50)

    Text_Surf_big, Text_Rect_big = text_obj_M('GAME OVER', game_over_text_big)
    Text_Surf_small, Text_Rect_small = text_obj_B(
        'YOU DIED ', game_over_text_small)

    Text_Rect_big.center = ((width//2), (height//2))
    Text_Rect_small.center = ((width//2), 500)
    pause = True

    while game_over:
        for e in event.get():
            if e.type == QUIT:
                quit()

        screen.blit(Text_Surf_big, Text_Rect_big)
        screen.blit(Text_Surf_small, Text_Rect_small)

        display.flip()


def move_jet(guy, x, y):
    # The enemy will B-Line towards the player. Have to draw a similar
    # triangle to get the x,y components of the move and use trig to
    # get the angle. The angle is needed to rotate the picture.
    #returns (x,y,ang)

    dist = max(1, distance(guy[X], guy[Y], x, y))
    moveX = (x-guy[X])*BADSPEED/dist
    moveY = (y - guy[Y])*BADSPEED/dist
    ang = atan2(-moveY, moveX)

    return moveX, moveY, degrees(ang)


def move_birds(guy, x, y):
    dist = max(1, distance(guy[0], guy[1], x, y))
    moveX = (x-guy[X])*BADSPEED2/dist
    moveY = (y - guy[Y])*BADSPEED2/dist
    ang = atan2(-moveY, moveX)

    return moveX, moveY, degrees(ang)


def moveBadGuys(jet, birds, goodX, goodY):
    # The AI for the badGuys is real simple. If the goodGuy is left/right
    # they move left/right. Same with up/down.
    # badGuys - A list of bad guy positions ([x,y] lists)
    # goodX, goodY - good guy position

    for guy in jet:
        mx, my, ang = move_jet(guy, goodX, goodY)  # Follow the mouse
        guy[X] += mx
        guy[Y] += my
        guy[2] = ang

    for guy in birds:
        mx, my, ang = move_birds(guy, goodX, goodY)  # Follow the mouse
        guy[X] += mx
        guy[Y] += my
        guy[2] = ang


def checkHits(jet, birds, goodX, goodY):
    # Both good and bad guys are circles, so to check hits we just need to check if the
    # distance from center to center is < 130 (for jet) or <40 (for birds).
    # For this part, when they do collide we re-set the bad guy
    # I also put the health / shield / enemy_count bar

    global soldier_HEALTH, soldier_SHIELD, soldier_HEALTH_colour, soldier_SHIELD_colour, enemy_tot, enemy_tot_colour

    for i, enemy_jet in enumerate(jet):
        if ((goodX-enemy_jet[X])**2 + (goodY-enemy_jet[Y])**2)**0.5 < 130:
            # random set integers for random spawn locations
            enemy_jet[X], enemy_jet[Y] = i*-80, randint(-40, 800)

            soldier_HEALTH -= 20
            soldier_SHIELD -= 20
            enemy_tot -= 2

            if soldier_HEALTH > 85 and soldier_SHIELD > 66:
                soldier_HEALTH_colour = GREEN
                soldier_SHIELD_colour = BLUE

            elif soldier_HEALTH > 65 and soldier_SHIELD > 33:
                soldier_HEALTH_colour = YELLOW
                soldier_SHIELD_colour = TURQUOISE

            else:
                soldier_HEALTH_colour = RED
                soldier_SHIELD_colour = SKYBLUE
                enemy_tot_colour = DARKRED

        draw.rect(screen, soldier_HEALTH_colour, (20, 740, soldier_HEALTH, 15))
        draw.rect(screen, soldier_SHIELD_colour,
                  (240, 740, soldier_SHIELD, 15))
        draw.rect(screen, enemy_tot_colour, (680, 740, enemy_tot*2, 15))

    for z, enemy_birds in enumerate(birds):
        if ((goodX-enemy_birds[X])**2 + (goodY-enemy_birds[Y])**2)**0.5 < 40:
            # random set integers for random spawn locations
            enemy_birds[X], enemy_birds[Y] = z * \
                randint(-20, 1030), randint(-20, 800)

            soldier_HEALTH -= 10
            soldier_SHIELD -= 10
            enemy_tot -= 2

            if soldier_HEALTH > 85 and soldier_SHIELD > 66:
                soldier_HEALTH_colour = GREEN
                soldier_SHIELD_colour = BLUE

            elif soldier_HEALTH > 65 and soldier_SHIELD > 33:
                soldier_HEALTH_colour = YELLOW
                soldier_SHIELD_colour = TURQUOISE

            else:
                soldier_HEALTH_colour = RED
                soldier_SHIELD_colour = SKYBLUE
                enemy_tot_colour = DARKRED

        draw.rect(screen, soldier_HEALTH_colour, (20, 740, soldier_HEALTH, 15))
        draw.rect(screen, soldier_SHIELD_colour,
                  (240, 740, soldier_SHIELD, 15))
        draw.rect(screen, enemy_tot_colour, (680, 740, enemy_tot*2, 15))

        # You lose when you lose all your shield and health
        if soldier_HEALTH == 0 or soldier_HEALTH < 0:
            if soldier_SHIELD == 0 or soldier_SHIELD < 0:
                game_over()

        # If the enemy number reaches zero, print the victory screen
        if enemy_tot == 0:
            outlast()

        display.flip()


def move_soldier(guy, keys):  # Move my character with arrow

    if keys[K_a] and guy[X] > 40 or keys[K_LEFT] and guy[X] > 40:
        guy[0] -= 10

    if keys[K_d] and guy[X] < 1100 or keys[K_RIGHT] and guy[X] < 1100:
        guy[0] += 10

    if keys[K_s] and guy[Y] < 680 or keys[K_DOWN] and guy[Y] < 680:
        guy[1] += 10

    if keys[K_w] and guy[Y] > 50 or keys[K_UP] and guy[Y] > 50:
        guy[1] -= 10

 # For my bullets


def Bullets_soldier(BULLETSPEED, goodX, goodY):
    global cooldown

    cooldown -= 1

    if mb[0] == 1 and cooldown <= 0:
        bigX = mx - (goodX)
        bigY = my - (goodY)

        distance = hypot(bigX, bigY)

        # Small triangle ratio
        sx = BULLETSPEED*bigX/distance
        sy = BULLETSPEED*bigY/distance

        ang = atan2(bigY, bigX)
        ang += 0.5  # Radians (~ 28.6 degrees)
        shotX = goodX + cos(ang)*60
        shotY = goodY + sin(ang)*60

        bullet.append([shotX, shotY, sx, sy])

        cooldown = 3

    for i in bullet:
        i[X] += i[VX]
        i[Y] += i[VY]


def Bullets_Jet(BULLETSPEED, goodX, goodY):

    global cooldown_enemy

    cooldown_enemy -= 1

    for enemy_jet in jet:
        if cooldown_enemy <= 0:
            BIGX = goodX - enemy_jet[X]
            BIGY = goodY - enemy_jet[Y]

            distance = hypot(BIGX, BIGY)

            # Small triangle ratio
            sx = BULLETSPEED*BIGX/distance
            sy = BULLETSPEED*BIGY/distance

            ang = atan2(BIGY, BIGX)
            ang += 0.5  # Radians (~ 28.6 degrees)
            shotX = enemy_jet[X] + cos(ang)*10
            shotY = enemy_jet[Y] + sin(ang)*55

            jet_bullets.append([shotX, shotY, sx, sy])

            cooldown_enemy = 55

    for i in jet_bullets:
        i[X] += i[VX]
        i[Y] += i[VY]


# Check if bullets hit enemies, then make them respawn
def bullet_hit_enemy(jet, birds, birds_HEALTH, jet_HEALTH):

    global num_jet, num_birds, enemy_tot

    main_text_big = font.Font('freesansbold.ttf', 100)
    main_text_small = font.Font('freesansbold.ttf', 50)

    Text_Surf_big, Text_Rect_big = text_obj_T('VICTORY', main_text_big)
    Text_Surf_small, Text_Rect_small = text_obj_T(
        'YOU KILLED ALL ENEMIES', main_text_small)

    Text_Rect_big.center = ((width//2), (height//2))
    Text_Rect_small.center = ((width//2), 500)

    for i, enemy_jet in enumerate(jet):
        for pain in bullet:
            if ((pain[X]-enemy_jet[X])**2+(pain[Y]-enemy_jet[Y])**2)**0.5 < 200:
                jet_HEALTH -= 1
                if jet_HEALTH == 0:
                    enemy_jet[X], enemy_jet[Y] = i*-80, randint(-40, 800)
                    pain[X], pain[Y] = 0, 0
                    enemy_tot -= 2
                    num_jet += 1
                    print('You destroyed ', num_jet, ' jets')
                    print('\n')

                draw.rect(screen, enemy_tot_colour,
                          (680, 740, enemy_tot*2, 15))

    for i, enemy_birds in enumerate(birds):
        for pain in bullet:
            if ((pain[X]-enemy_birds[X])**2+(pain[Y]-enemy_birds[Y])**2)**0.5 < 80:
                birds_HEALTH -= 1
                if birds_HEALTH == 0:
                    enemy_birds[X], enemy_birds[Y] = i*-80, randint(-40, 800)
                    pain[X], pain[Y] = 0, 0
                    enemy_tot -= 2
                    num_birds += 1
                    print('You killed ', num_birds, ' birds')

                draw.rect(screen, enemy_tot_colour,
                          (680, 740, enemy_tot*2, 15))

    # Checking if certain number 10 jets and 50 birds have been taken down, then display victory
    if num_jet == 10 or num_jet > 10:
        if num_birds == 50 or num_birds > 50:
            win()

# Check if bullets hits you, then display 'GAME OVER' if dead


def bullet_hit_soldier():

    global soldier_HEALTH, soldier_SHIELD, soldier_HEALTH_colour, soldier_SHIELD_colour

    main_text = font.Font('freesansbold.ttf', 100)
    Text_Surf, Text_Rect = text_obj_W('GAME OVER', main_text)
    Text_Rect.center = ((width//2), (height//2))

    for i, soldier_hit in goodGuy:
        for pain in jet_bullets:
            if ((pain[X]-soldier_hit[X])**2 + (pain[Y]-soldier_hit[Y])**2)**0.5 < 50:
                soldier_HEALTH -= 10
                soldier_SHIELD -= 10

                if soldier_HEALTH > 85 and soldier_SHIELD > 66:
                    soldier_HEALTH_colour = GREEN
                    soldier_SHIELD_colour = BLUE

                elif soldier_HEALTH > 65 and soldier_SHIELD > 33:
                    soldier_HEALTH_colour = YELLOW
                    soldier_SHIELD_colour = TURQUOISE

                else:
                    soldier_HEALTH_colour = RED
                    soldier_SHIELD_colour = SKYBLUE

            draw.rect(screen, soldier_HEALTH_colour,
                      (20, 740, soldier_HEALTH, 15))
            draw.rect(screen, soldier_SHIELD_colour,
                      (240, 740, soldier_SHIELD, 15))

            if soldier_HEALTH == 0 or soldier_HEALTH < 0:
                if soldier_SHIELD == 0 or soldier_SHIELD < 0:
                    screen.blit(Text_Surf, Text_Rect)


def drawScene(screen, jet, birds, goodGuy, goodAng):

    # In-game BG
    screen.blit(background, (0, 0))

    # The bullets shot by the SOLDIER
    for bull in bullet:
        draw.circle(screen, GREEN, (int(bull[X]), int(bull[Y])), 4)

    # The bullets shot by the JET
    for watch_out in jet_bullets:
        draw.circle(screen, BLACK, (int(watch_out[X]), int(watch_out[Y])), 10)

    # My In-Game Title
    screen.blit(textsurface, ((width//4), 0))

    # The jet pic
    for guy in jet:
        pic = transform.rotate(badPic, guy[2])
        pic = transform.smoothscale(pic, (270, 270))
        screen.blit(pic, (guy[:2]))

    # The birds pic
    for guy in birds:
        pic = transform.rotate(badPic2, guy[2])
        pic = transform.smoothscale(pic, (90, 90))
        screen.blit(pic, guy[:2])

    # For my good guy
    angle = degrees(atan2(mx-goodGuy[X], my-goodGuy[Y]))-90
    main_guy = transform.rotate(goodPic, angle)

    rotate = (goodGuy[X]-main_guy.get_width()//2,
              goodGuy[Y]-main_guy.get_height()//2)

    screen.blit(main_guy, rotate)

    # For my health / shield / ammo / enemy bars on the bottom of the screen
    # 1st line from each group of trios is the black background for when losing shield / health
    # 2nd line is for outlining the 2nd rect.

    draw.rect(screen, BLACK, (20, 740, 200, 15), 0)  # HEALTH
    draw.rect(screen, BLACK, (20, 740, 200, 15), 2)

    draw.rect(screen, BLACK, (240, 740, 200, 15), 0)  # SHIELD
    draw.rect(screen, BLACK, (240, 740, 200, 15), 2)

    draw.rect(screen, (BLACK), (460, 740, 200, 15), 0)  # AMMO COUNT
    # (The rect itself, not the outline)
    draw.rect(screen, (192, 192, 192), (460, 740, 200, 15), 0)
    draw.rect(screen, BLACK, (460, 740, 200, 15), 2)  # Outline

    draw.rect(screen, (BLACK), (680, 740, 200, 15), 0)  # ENEMY COUNT
    draw.rect(screen, BLACK, (680, 740, 200, 15), 2)

    ammo_font = font.Font('freesansbold.ttf', 14)
    ammo_text = ammo_font.render('**Infinite**', True, BLACK)
    screen.blit(ammo_text, (520, 741))

    # Health Pic
    screen.blit(health, (16, 700))

    # Shield Pic
    screen.blit(shield, (240, 700))

    # Ammo Pic
    screen.blit(ammo, (460, 700))

    # Enemy Pic
    screen.blit(enemy, (674, 700))

    display.flip()


BULLETSPEED = 10  # Speed of my bullet

BADSPEED = 2  # For the speed of my jet
jet = [[1170, (width//2), 0]]    # inital x,y location for my jet

BADSPEED2 = 7  # For the speed of my birds
birds = [[-200, randint(-30, 800), 0],  [(width//2), -randint(-30, 800), 0],
         [200, randint(-30, 800), 0]]  # inital x,y location for my 3 birds


goodGuy = [width//2, height//2]  # Initial spot of the character


# My Main Pictures
###################

# Menu Image
menu_bg = image.load('images\menu.jpg').convert_alpha()
instructions = image.load('images\Instructions.png').convert_alpha()
Credits = image.load('images\Credits.png').convert_alpha()

# Characters
badPic = image.load("images\plane.png").convert_alpha()
badPic2 = image.load("images\small_jet.png").convert_alpha()
goodPic = image.load("images\soldier.png").convert_alpha()
backPic = image.load("images\\fire.jpg").convert_alpha()

# Bottom part
health = image.load('images\health.png').convert_alpha()
shield = image.load('images\shield.png').convert_alpha()
ammo = image.load('images\\ammo.png').convert_alpha()
enemy = image.load('images\enemy.png').convert_alpha()

# Scaling my pics
###################

# MENU
menu_bg = transform.smoothscale(menu_bg, (1152, 768))
instructions = transform.smoothscale(instructions, (1152, 768))
Credits = transform.smoothscale(Credits, (1152, 768))

# IN-GAME
background = transform.smoothscale(backPic, (1152, 768))  # Background Pic

goodPic = transform.smoothscale(goodPic, (130, 130))  # Soldier

# Bottom Part
health = transform.smoothscale(health, (40, 40))
shield = transform.smoothscale(shield, (34, 34))
ammo = transform.smoothscale(ammo, (30, 32))
enemy = transform.smoothscale(enemy, (43, 36))

###################

page = "intro"   # Setting up for my menu page

mouse.set_visible(False)


while running():
    mx, my = mouse.get_pos()
    mb = mouse.get_pressed()
    keys = key.get_pressed()

    if page == "intro":
        page = intro()  # page to go right to game

    elif page == None:
        move_soldier(goodGuy, keys)

        Bullets_soldier(BULLETSPEED, goodGuy[X], goodGuy[Y])
        Bullets_Jet(BULLETSPEED, goodGuy[X], goodGuy[Y])

        bullet_hit_enemy(jet, birds, birds_HEALTH, jet_HEALTH)
        # bullet_hit_soldier()

        goodAng = degrees(atan2(my-goodGuy[Y], mx-goodGuy[X]))

        moveBadGuys(jet, birds, goodGuy[X], goodGuy[Y])
        checkHits(jet, birds, goodGuy[X], goodGuy[Y])

        drawScene(screen, jet, birds, goodGuy, goodAng)

    myClock.tick(60)                    # delay

quit()
