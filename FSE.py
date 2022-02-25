# FSE
# Night of the Invaders
# Salman Chowdhury - [ STUDENT ]
# Gr. 11
# Mr.McKenzie - [ TEACHER ]
# [ START DATE ] - Monday, April 8, 2019
# [ DUE DATE ] - Friday, June 14, 2019
# Enjoy the game

from pygame import *
from math import *
from random import *
from sys import exit

init()

size = width, height = (1152, 670)
screen = display.set_mode(size)

display.set_caption("Night of the Invaders")

song = mixer.Sound('music\\bg_music.wav')
song.play(loops=-1)

myClock = time.Clock()

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

# Font for in-game title
# font.init()
myfont = font.SysFont('Comic Sans MS', 50, bold=True)
textsurface = myfont.render(' Night of the Invaders', True, BLACK)

# EVENT LOOP
def running():  
    for evnt in event.get():
        if evnt.type == QUIT:
            return False

    return True

def distance(x1, y1, x2, y2):
    return ((x1-x2)**2 + (y1-y2)**2)**0.5


###########################################     MY MAIN IMAGES     ##############################################

# Menu Image
menu_bg = image.load('images\menu.jpg').convert_alpha()
menu_bg = transform.smoothscale(menu_bg, (1152, 768))

instructions = image.load('images\Instructions.png').convert_alpha()
instructions = transform.smoothscale(instructions, (1152, 768))

Credits = image.load('images\Credits.png').convert_alpha()
Credits = transform.smoothscale(Credits, (1152, 768))

# Characters 
goodPic = image.load("images\soldier.png").convert_alpha() # Soldier
goodPic = transform.smoothscale(goodPic, (130, 130))  
goodPic_rect = goodPic.get_rect(center = (width//2, height//2))

jetPic = image.load("images\plane.png").convert_alpha()
jetPic = transform.smoothscale(jetPic, (270, 270))
def initial_jet_spawn(): # To be used in the very next line
    random_respawn = randint(1,2)

    if random_respawn == 1:
        return (randint(-500,-100), randint(-500, 1000))

    elif random_respawn == 2:
        return (randint(1400,2000), randint(-500, 1000))
jetPic_rect = jetPic.get_rect(center = initial_jet_spawn())

small_jetPic = image.load("images\small_jet.png").convert_alpha()
small_jetPic = transform.smoothscale(small_jetPic, (90, 90))
small_jetPic_rect1 = small_jetPic.get_rect(center = (randint(-1000,-400), randint(-500, 800)))
small_jetPic_rect2 = small_jetPic.get_rect(center = (randint(-600,1900), randint(-500, 800)))
small_jetPic_rect3 = small_jetPic.get_rect(center = (randint(1500,1900), randint(-500, 800)))

# Background Pic
backPic = image.load("images\\fire.jpg").convert_alpha()
background = transform.smoothscale(backPic, (1152, 768))  

# Crosshair
crosshair = image.load('images\crosshair.png').convert_alpha()
crosshair = transform.smoothscale(crosshair, (43, 43))
crosshair_rect = crosshair.get_rect()

bullet = image.load('images\\bullet.png').convert_alpha()
bullet = transform.smoothscale(bullet, (100, 15))

# Bottom part
health = image.load('images\health.png').convert_alpha()
health = transform.smoothscale(health, (40, 40))

shield = image.load('images\shield.png').convert_alpha()
shield = transform.smoothscale(shield, (34, 34))

ammo = image.load('images\\ammo.png').convert_alpha()
ammo = transform.smoothscale(ammo, (30, 32))

enemy = image.load('images\enemy.png').convert_alpha()
enemy = transform.smoothscale(enemy, (43, 36))

#########################################################################################


###########################################     EXTRA INFO     ##############################################

# Positions
X = 0
Y = 1
VX = 2
VY = 3

# Lists to store bullet values
soldier_bullet = []
jet_bullets = []

# Cooldown for weapons
cooldown = 0
cooldown_enemy = 0

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

BULLETSPEED = 10  # Speed of my bullet

BADSPEED = 2  # For the speed of my jet
jet = [jetPic_rect.centerx, jetPic_rect.centery, 0]   # inital x,y,angle values for my jet

BADSPEED2 = [3,6,8]  # For the speed of my birds
# inital x,y,angle, small_jet Rect values for my 3 birds
birds = [[small_jetPic_rect1.centerx, small_jetPic_rect1.centery, 0, small_jetPic_rect1],  
        [small_jetPic_rect2.centerx, small_jetPic_rect2.centery, 0, small_jetPic_rect2], 
        [small_jetPic_rect3.centerx, small_jetPic_rect3.centery, 0, small_jetPic_rect3]]


goodGuy = [goodPic_rect.centerx, goodPic_rect.centery]  # Initial spot of the character

#########################################################################################


###########################################     MENU     ##############################################

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

    if 420 < mx < 420 + 300 and 300 < my < 300 + 82:  # PLAY colour when hovered upon
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
    if 420+300 > mx > 420 and 300+82 > my > 300 and mb[0]:
        return None

    # Instructions
    if 420+300 > mx > 420 and 425+60 > my > 425 and mb[0]:
        while running():
            screen.blit(instructions, (0, 0))

    # Credits
    if 420+300 > mx > 420 and 520+60 > my > 520 and mb[0]:
        while running():
            screen.blit(Credits, (0, 0))

    # Exit
    if 420+300 > mx > 420 and 605+60 > my > 605 and mb[0]:
        quit()
        exit()

    return "intro"


#########################################################################################


###########################################     IN-GAME     ##############################################

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

        display.update()


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

        display.update()


# Show this when you lose
def game_over():

    game_over_text_big = font.Font('freesansbold.ttf', 100)
    game_over_text_small = font.Font('freesansbold.ttf', 50)

    Text_Surf_big, Text_Rect_big = text_obj_M('GAME OVER', game_over_text_big)
    Text_Surf_small, Text_Rect_small = text_obj_B(
        'YOU DIED ', game_over_text_small)

    Text_Rect_big.center = ((width//2), (height//2))
    Text_Rect_small.center = ((width//2), 500)
    
    game_over = True

    while game_over:
        for e in event.get():
            if e.type == QUIT:
                quit()
                exit()        
            
            # elif e.type == KEYDOWN and e.key == K_ESCAPE:
            #     return False

        screen.blit(Text_Surf_big, Text_Rect_big)
        screen.blit(Text_Surf_small, Text_Rect_small)

        display.update()

# Move my soldier by keys (WASD and arrow keys) (also putting boundaries so the soldier doesn't go off the screen)
def move_soldier(guy, keys):

    if ( keys[K_a] or keys[K_LEFT] ) and guy[X] > 55:        
        goodPic_rect.centerx -= 10  # Move the Rect
        guy[0] = goodPic_rect.centerx

    if ( keys[K_d] or keys[K_RIGHT] ) and guy[X] < 1100:
        goodPic_rect.centerx += 10
        guy[0] = goodPic_rect.centerx

    if ( keys[K_s] or keys[K_DOWN] ) and guy[Y] < 620:
        goodPic_rect.centery += 10
        guy[1] = goodPic_rect.centery

    if ( keys[K_w] or keys[K_UP] ) and guy[Y] > 50:
        goodPic_rect.centery -= 10
        guy[1] = goodPic_rect.centery

def move_jet(soldierX, soldierY):
    # The enemy will B-Line towards the player. Have to draw a similar
    # triangle to get the x,y components of the move and use trig to
    # get the angle. The angle is needed to rotate the picture.
    # returns angle

    dx = soldierX - jet[X]
    dy = soldierY - jet[Y]

    return atan2(dy, dx)

def move_birds(birdObject, soldierX, soldierY):
    dx = soldierX - birdObject[X]
    dy = soldierY - birdObject[Y]

    return atan2(dy, dx)


def moveBadGuys(jet, birds, goodX, goodY):
    # The AI for the badGuys is real simple. If the goodGuy is left/right
    # they move left/right. Same with up/down.
    # badGuys - A list of bad guy positions ([x,y] lists)
    # goodX, goodY - good guy position

    angle = move_jet(goodX, goodY)
    
    jetPic_rect.centerx += cos(angle) * BADSPEED
    jet[X] = jetPic_rect.centerx

    jetPic_rect.centery += sin(angle) * BADSPEED
    jet[Y] = jetPic_rect.centery

    jet[2] = degrees(angle)

    for i in birds:
        angle = move_birds(i, goodX, goodY)

        i[3].centerx += cos(angle) * BADSPEED2[randint(0,2)]
        i[X] = i[3].centerx

        i[3].centery += sin(angle) * BADSPEED2[randint(0,2)]
        i[Y] = i[3].centery

        i[2] = degrees(angle)

#ENEMY RESPAWNS
def jet_random_respawn():
    random_respawn = randint(1,2)

    if random_respawn == 1:
        jetPic_rect.centerx, jetPic_rect.centery = randint(-500,-100), randint(-500, 1000)
        jet[X], jet[Y] = jetPic_rect.centerx, jetPic_rect.centery

    elif random_respawn == 2:
        jetPic_rect.centerx, jetPic_rect.centery  = randint(1400,2000), randint(-500, 1000)
        jet[X], jet[Y] = jetPic_rect.centerx, jetPic_rect.centery

def smalljet_random_respawn(enemy_smalljet):
    random_respawn = randint(1,2)

    if random_respawn == 1:
        enemy_smalljet[3].centerx, enemy_smalljet[3].centery = randint(-400,-100), randint(-500, 1000)
        enemy_smalljet[X], enemy_smalljet[Y] = enemy_smalljet[3].centerx, enemy_smalljet[3].centery

    elif random_respawn == 2:
        enemy_smalljet[3].centerx, enemy_smalljet[3].centery = randint(1300,1600), randint(-500, 1000)
        enemy_smalljet[X], enemy_smalljet[Y] = enemy_smalljet[3].centerx, enemy_smalljet[3].centery


def checkHits(birds):
    # Both good and bad guys are circles, so to check hits we just need to check if the
    # distance from center to center is < 130 (for jet) or <40 (for birds).
    # For this part, when they do collide we re-set the bad guy
    # I also put the health / shield / enemy_count bar

    global soldier_HEALTH, soldier_SHIELD, soldier_HEALTH_colour, soldier_SHIELD_colour, enemy_tot, enemy_tot_colour

    if distance(goodGuy[X], goodGuy[Y], jet[X], jet[Y]) <= 40:
        
        # random set integers for random spawn locations
        jet_random_respawn()      

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
    draw.rect(screen, soldier_SHIELD_colour, (240, 740, soldier_SHIELD, 15))
    draw.rect(screen, enemy_tot_colour, (680, 740, enemy_tot*2, 15))
        

    for enemy_smalljet in birds:
        if distance(goodGuy[X], goodGuy[Y], enemy_smalljet[X], enemy_smalljet[Y]) <= 20:
            
            # random set integers for random spawn locations
            smalljet_random_respawn(enemy_smalljet)

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
            # if game_over() == False:
            #     return "Continue"


    # If the enemy number reaches zero, print the victory screen
    if enemy_tot == 0:
        outlast()

# For my soldier's bullets
def Bullets_soldier(BULLETSPEED, goodX, goodY):
    global cooldown

    cooldown -= 1

    if mb[0] == 1 and cooldown <= 0:

        # Use these coordinates as a starting reference (Between mouse and central position of the Soldier)
        referenceX = mx - goodX
        referenceY = my - goodY

        ang = atan2(referenceY, referenceX)
        ang += 0.5  # Radians (~ 28.6 degrees)  --> Angle adjustment to align it with the barrel of the gun

        # The starting position of a specified bullet (which is located at the barrel of the gun)
        # Using this, I can increment the bullet using the "incrementX/Y"
        # Multiply by 57 on each x and y to bring it further from the central point of the Soldier to the barrel of the gun
        gunBarrelPosX = goodX + cos(ang)*57
        gunBarrelPosY = goodY + sin(ang)*57

        # This is used to make the bullets go through the center of the crosshair (and not slightly to the right like it would without it...)
        centralizeX = mx - gunBarrelPosX
        centralizeY = my - gunBarrelPosY

        centralizeAngle = atan2(centralizeY, centralizeX)

        # Small triangle ratio --> To make the specified bullet increment in a linear direction        
        incrementX = cos(centralizeAngle) * BULLETSPEED
        incrementY = sin(centralizeAngle) * BULLETSPEED

        soldier_bullet.append( [gunBarrelPosX, gunBarrelPosY, incrementX, incrementY] ) # Each list is one bullet

        cooldown = 7

    # The positions of "gunBarrelPosX" and "gunBarrelPosY" gets incremented and used for the postion of the bullet circles (in drawScene function)
    for i in soldier_bullet:
        i[X] += i[VX]
        i[Y] += i[VY]

# For my jet's bullets
def Bullets_Jet(BULLETSPEED, goodX, goodY):

    global cooldown_enemy

    cooldown_enemy -= 1

    if cooldown_enemy <= 0:
        BIGX = goodX - jet[X]
        BIGY = goodY - jet[Y]

        ang = atan2(BIGY, BIGX)

        # Small triangle ratio
        incrementX = cos(ang) * BULLETSPEED
        incrementY = sin(ang) * BULLETSPEED
       
        ang += 0.5  # Radians (~ 28.6 degrees)
        missileBarrelX = jet[X] + cos(ang)*10
        missileBarrelY = jet[Y] + sin(ang)*55

        jet_bullets.append( [missileBarrelX, missileBarrelY, incrementX, incrementY] )

        cooldown_enemy = 50

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

    for pain in soldier_bullet:
        if ((pain[X]-jet[X])**2+(pain[Y]-jet[Y])**2)**0.5 < 200:
            jet_HEALTH -= 1
            if jet_HEALTH == 0:
                jet_random_respawn()
                pain[X], pain[Y] = 0, 0
                enemy_tot -= 2
                num_jet += 1
                print('You destroyed ', num_jet, ' jets')
                print('\n')

            draw.rect(screen, enemy_tot_colour, (680, 740, enemy_tot*2, 15))

    for enemy_smalljet in birds:
        for pain in soldier_bullet:
            if ((pain[X]-enemy_smalljet[X])**2+(pain[Y]-enemy_smalljet[Y])**2)**0.5 < 80:
                birds_HEALTH -= 1
                if birds_HEALTH == 0:
                    smalljet_random_respawn(enemy_smalljet)
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


def drawScene(screen, jet, birds, goodGuy):

    # In-game BG
    screen.blit(background, (0, 0))

    # The bullets shot by the SOLDIER
    for bull in soldier_bullet:
        draw.circle(screen, GREEN, (int(bull[X]), int(bull[Y])), 4)
        # screen.blit(bullet,(int(bull[X]), int(bull[Y])))

    # The bullets shot by the JET
    for missiles in jet_bullets:
        draw.circle(screen, BLACK, (int(missiles[X]), int(missiles[Y])), 10)

    # The jet pic
    jetAng = degrees( atan2( -(goodGuy[Y] - jet[Y]), goodGuy[X] - jet[X] ) )
    rotate_jet = transform.rotate(jetPic, jetAng - 90) # a Surface

    # Center the rotation
    jet_rotate_coordinate = (jet[X]-rotate_jet.get_width()//2, jet[Y]-rotate_jet.get_height()//2)
    screen.blit(rotate_jet, jet_rotate_coordinate)

    # The birds pic
    for birdObject in birds:
        birdAng = degrees( atan2( -(goodGuy[Y] - birdObject[Y]), goodGuy[X] - birdObject[X] ) )
        rotate_smallJet = transform.rotate(small_jetPic, birdAng - 90) # a Surface

        # Center the rotation
        smallJet_rotate_coordinate = (birdObject[X]-rotate_smallJet.get_width()//2, birdObject[Y]-rotate_smallJet.get_height()//2)    
        screen.blit(rotate_smallJet, smallJet_rotate_coordinate)

        # draw.circle(screen, MAGENTA, birdObject[3].topleft, 5, 0)
        # draw.circle(screen, MAGENTA, birdObject[3].center, 5, 0)
        # draw.rect(screen, TURQUOISE, birdObject[3], 2)

    # For my soldier
    goodAng = degrees( atan2( -(my-goodGuy[Y]), mx-goodGuy[X] ) )
    rotate_soldier = transform.rotate(goodPic, goodAng + 6)  # a Surface    

    # Center the rotation
    soldier_rotate_coordinate = (goodGuy[X]-rotate_soldier.get_width()//2, goodGuy[Y]-rotate_soldier.get_height()//2)
    screen.blit(rotate_soldier,  soldier_rotate_coordinate)    

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
    screen.blit(health, (16, 640))

    # Shield Pic
    screen.blit(shield, (240, 640))

    # Ammo Pic
    screen.blit(ammo, (460, 640))

    # Enemy Pic
    screen.blit(enemy, (674, 640))

#########################################################################################

# Setting up for my menu page
page = "intro"

while running():
    mx, my = mouse.get_pos()
    mb = mouse.get_pressed()
    keys = key.get_pressed()

    if page == "intro":
        page = intro()  # page to go right to game
        mouse.set_visible(True)

    elif page == None:
        mouse.set_visible(False)        

        move_soldier(goodGuy, keys)
        moveBadGuys(jet, birds, goodGuy[X], goodGuy[Y])

        Bullets_soldier(BULLETSPEED, goodGuy[X], goodGuy[Y])    
        Bullets_Jet(BULLETSPEED, goodGuy[X], goodGuy[Y])

        bullet_hit_enemy(jet, birds, birds_HEALTH, jet_HEALTH)
        # bullet_hit_soldier()

        checkHits(birds)

        drawScene(screen, jet, birds, goodGuy)

        crosshair_rect.center = mx, my
        screen.blit(crosshair, crosshair_rect)

        draw.circle(screen, MAGENTA, goodPic_rect.topleft, 5, 0)
        draw.circle(screen, MAGENTA, goodPic_rect.center, 5, 0)
        draw.rect(screen, TURQUOISE, goodPic_rect, 2)

        draw.circle(screen, MAGENTA, jetPic_rect.topleft, 5, 0)
        draw.circle(screen, MAGENTA, jetPic_rect.center, 5, 0)
        draw.rect(screen, TURQUOISE, jetPic_rect, 2)


    myClock.tick(30)     # delay

    display.flip()