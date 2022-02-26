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

windowSize = width, height = (1152, 700)
screen = display.set_mode(windowSize)

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
health = image.load('images\health.png').convert_alpha() # Icon made by "nawicon" from www.flaticon.com
health = transform.smoothscale(health, (40, 40))

shield = image.load('images\shield.png').convert_alpha() # Icon made by "Freepik" from www.flaticon.com
shield = transform.smoothscale(shield, (39, 39))

ammo = image.load('images\\ammo.png').convert_alpha()
ammo = transform.smoothscale(ammo, (30, 32))

enemy = image.load('images\enemy.png').convert_alpha() # Icon made by "Nhor Phai" from www.flaticon.com
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

# Used for counting number of jets/small jets destroyed
num_jet = 0
num_birds = 0

# Number of enemies total
current_enemy_count = 40
enemy_total = 40
enemy_count_ratio = enemy_total / 160  # 160 is the length of the enemy_tot bar in pixels

# Health/Shield of all characters
soldier_CURRENT_HEALTH = 200
soldier_MAX_HEALTH = 200
soldier_HEALTH_RATIO = soldier_MAX_HEALTH / 160  # 160 is the length of the health bar in pixels

soldier_CURRENT_SHIELD = 200
soldier_MAX_SHIELD = 200
soldier_SHIELD_RATIO = soldier_MAX_SHIELD / 160 # 160 is the length of the shield bar in pixels

jet_HEALTH = 9
birds_HEALTH = 4

# Initial stats bar colors
soldier_HEALTH_colour = GREEN
soldier_SHIELD_colour = BLUE
enemy_tot_colour = DARKRED

SOLDIER_BULLET_SPEED = 10  # Speed of my bullet
JET_BULLET_SPEED = 15  # Speed of my bullet

BADSPEED = 2  # For the speed of my jet
jet = [jetPic_rect.centerx, jetPic_rect.centery, 0]   # inital x,y,angle values for my jet

BADSPEED2 = [3,6,8]  # For the speed of my birds
# inital x,y,angle, small_jet Rect values for my 3 birds
small_Jets = [[small_jetPic_rect1.centerx, small_jetPic_rect1.centery, 0, small_jetPic_rect1],  
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
                exit()

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
                exit()

        screen.blit(Text_Surf_big, Text_Rect_big)
        screen.blit(Text_Surf_small, Text_Rect_small)

        display.update()


# Show this when you lose
def game_over():

    game_over_text_big = font.Font('freesansbold.ttf', 100)
    game_over_text_small = font.Font('freesansbold.ttf', 50)

    Text_Surf_big, Text_Rect_big = text_obj_M('GAME OVER', game_over_text_big)
    Text_Surf_small, Text_Rect_small = text_obj_B('YOU DIED ', game_over_text_small)

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

def move_birds(smallJetObject, soldierX, soldierY):
    dx = soldierX - smallJetObject[X]
    dy = soldierY - smallJetObject[Y]

    return atan2(dy, dx)

def moveBadGuys(jet, small_Jets, goodX, goodY):
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

    for i in small_Jets:
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
        jet[X], jet[Y] = jetPic_rect.centerx, jetPic_rect.centery = randint(-500,-150), randint(-500, 1000)

    elif random_respawn == 2:
        jet[X], jet[Y] = jetPic_rect.centerx, jetPic_rect.centery  = randint(1400,2000), randint(-500, 1000)

def smalljet_random_respawn(enemy_smalljet):
    random_respawn = randint(1,2)

    if random_respawn == 1:
        enemy_smalljet[X], enemy_smalljet[Y] = enemy_smalljet[3].centerx, enemy_smalljet[3].centery = randint(-400,-100), randint(-500, 1000)
        

    elif random_respawn == 2:
        enemy_smalljet[X], enemy_smalljet[Y] = enemy_smalljet[3].centerx, enemy_smalljet[3].centery = randint(1300,1600), randint(-500, 1000)


# For my soldier's bullets
def Bullets_soldier(goodX, goodY):
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
        incrementX = cos(centralizeAngle) * SOLDIER_BULLET_SPEED
        incrementY = sin(centralizeAngle) * SOLDIER_BULLET_SPEED

        soldier_bullet.append( [gunBarrelPosX, gunBarrelPosY, incrementX, incrementY] ) # Each list is one bullet

        cooldown = 7

    # The positions of "gunBarrelPosX" and "gunBarrelPosY" gets incremented and used for the postion of the bullet circles (in drawScene function)
    for i in soldier_bullet:
        i[X] += i[VX]
        i[Y] += i[VY]

# For my jet's bullets
def Bullets_Jet(goodX, goodY):

    global cooldown_enemy

    cooldown_enemy -= 1

    if cooldown_enemy <= 0:
        BIGX = goodX - jet[X]
        BIGY = goodY - jet[Y]

        ang = atan2(BIGY, BIGX)

        # Small triangle ratio
        incrementX = cos(ang) * JET_BULLET_SPEED
        incrementY = sin(ang) * JET_BULLET_SPEED
       
        ang += 0.5  # Radians (~ 28.6 degrees)
        missileBarrelX = jet[X] + cos(ang)*10
        missileBarrelY = jet[Y] + sin(ang)*55

        jet_bullets.append( [missileBarrelX, missileBarrelY, incrementX, incrementY] )

        cooldown_enemy = 50

    for i in jet_bullets:
        i[X] += i[VX]
        i[Y] += i[VY]


# Animating the bullets fired by soldier and jets
def bulletsFired():
    # The bullets shot by the SOLDIER
    for bull in soldier_bullet:
        draw.circle(screen, GREEN, (int(bull[X]), int(bull[Y])), 4)
        # screen.blit(bullet,(int(bull[X]), int(bull[Y])))

    # The bullets shot by the JET
    for bull in jet_bullets:
        draw.circle(screen, BLACK, (int(bull[X]), int(bull[Y])), 10)


# For my health / shield / ammo / enemy bars on the bottom of the screen
def soldier_enemy_Stats():
    # 1st line from each group of trios is the black background for when losing shield / health
    # 2nd line is for outlining the 2nd rect.

    # HEALTH
    draw.rect(screen, BLACK, (55, 669, 160, 15), 0)  
    draw.rect(screen, WHITE, (55, 669, 160, 15), 3)

    # SHIELD
    draw.rect(screen, BLACK, (277, 669, 160, 15), 0)  
    draw.rect(screen, WHITE, (277, 669, 160, 15), 3)

    # AMMO COUNT
    draw.rect(screen, BLACK, (503, 669, 160, 15), 0)     
    draw.rect(screen, WHITE, (503, 669, 160, 15), 3)

    # ENEMY COUNT
    draw.rect(screen, BLACK, (735, 669, 160, 15), 0)  
    draw.rect(screen, WHITE, (735, 669, 160, 15), 3)

    # Health Pic
    screen.blit(health, (16, 655))

    # Shield Pic
    screen.blit(shield, (240, 655))

    # Ammo Pic
    screen.blit(ammo, (471, 655))

    # Enemy Pic
    screen.blit(enemy, (697, 655))

# Used for the health and shield bar animations
def soldier_health_shield_BAR(inflict_damage):
    global soldier_CURRENT_SHIELD, soldier_CURRENT_HEALTH, soldier_SHIELD_colour, soldier_HEALTH_colour

    # Soldier SHIELD gets taken away first, then when SHIELD is all taken away, starts taking away Soldier HEALTH
    if soldier_CURRENT_SHIELD > 0:
        soldier_CURRENT_SHIELD -= inflict_damage

        if soldier_CURRENT_SHIELD >= 66:
            soldier_SHIELD_colour = BLUE
        
        elif soldier_CURRENT_SHIELD >= 33:
            soldier_SHIELD_colour = TURQUOISE
        
        else:
            soldier_SHIELD_colour = SKYBLUE


    elif soldier_CURRENT_SHIELD <= 0:
        soldier_CURRENT_HEALTH -= inflict_damage

        if soldier_CURRENT_SHIELD >= 66:
            soldier_HEALTH_colour = GREEN
        
        elif soldier_CURRENT_SHIELD >= 33:
            soldier_HEALTH_colour = YELLOW
        
        else:
            soldier_HEALTH_colour = RED

# Check for the physical collisions between the soldier and the jets (Big or Small)
def checkCollisions(small_Jets):
    # Need to check if the distance from center to center is <= 40 (for jet) or <= 20 (for small jets).
    # For this part, when they do collide, I re-set the bad guy
    # I also put the health / shield / enemy_count bar

    global soldier_CURRENT_HEALTH, soldier_CURRENT_SHIELD, soldier_HEALTH_colour, soldier_SHIELD_colour, current_enemy_count, enemy_tot_colour

    if distance(goodGuy[X], goodGuy[Y], jet[X], jet[Y]) <= 40:
        
        # random set integers for random spawn locations
        jet_random_respawn()

        current_enemy_count -= 1

        soldier_health_shield_BAR(30)

    draw.rect(screen, soldier_SHIELD_colour, (277, 669, soldier_CURRENT_SHIELD / soldier_SHIELD_RATIO, 15))
    draw.rect(screen, soldier_HEALTH_colour, (55, 669, soldier_CURRENT_HEALTH / soldier_HEALTH_RATIO, 15))
    draw.rect(screen, enemy_tot_colour, (735, 669, current_enemy_count / enemy_count_ratio, 15))


    for enemy_smalljet in small_Jets:
        if distance(goodGuy[X], goodGuy[Y], enemy_smalljet[X], enemy_smalljet[Y]) <= 20:
            
            # random set integers for random spawn locations
            smalljet_random_respawn(enemy_smalljet)

            current_enemy_count -= 1
            
            soldier_health_shield_BAR(20)

        draw.rect(screen, soldier_SHIELD_colour, (277, 669, soldier_CURRENT_SHIELD / soldier_SHIELD_RATIO, 15))
        draw.rect(screen, soldier_HEALTH_colour, (55, 669, soldier_CURRENT_HEALTH / soldier_HEALTH_RATIO, 15))
        draw.rect(screen, enemy_tot_colour, (735, 669, current_enemy_count / enemy_count_ratio, 15))

    
    # You lose when you lose all your shield and health
    if soldier_CURRENT_HEALTH <= 0:            
        game_over()
        # if game_over() == False:
        #     return "Continue"

    # If the enemy number reaches zero, print the victory screen
    if current_enemy_count == 0:
        outlast()

# Check if the soldier's bullets hit enemies, then make them respawn
def bullet_hit_enemy(jet, small_Jets, birds_HEALTH, jet_HEALTH):

    global num_jet, num_birds, current_enemy_count

    main_text_big = font.Font('freesansbold.ttf', 100)
    main_text_small = font.Font('freesansbold.ttf', 50)

    Text_Surf_big, Text_Rect_big = text_obj_T('VICTORY', main_text_big)
    Text_Surf_small, Text_Rect_small = text_obj_T('YOU KILLED ALL ENEMIES', main_text_small)

    Text_Rect_big.center = ((width//2), (height//2))
    Text_Rect_small.center = ((width//2), 500)

    for pain in soldier_bullet:
        if ((pain[X]-jet[X])**2+(pain[Y]-jet[Y])**2)**0.5 < 200:
            jet_HEALTH -= 1
            if jet_HEALTH == 0:
                jet_random_respawn()
                pain[X], pain[Y] = 0, 0
                current_enemy_count -= 1
                num_jet += 1
                print('You destroyed ', num_jet, ' jets')
                print('\n')

            draw.rect(screen, enemy_tot_colour, (735, 669, current_enemy_count / enemy_count_ratio, 15))

    for enemy_smalljet in small_Jets:
        for pain in soldier_bullet:
            if ((pain[X]-enemy_smalljet[X])**2+(pain[Y]-enemy_smalljet[Y])**2)**0.5 < 80:
                birds_HEALTH -= 1
                if birds_HEALTH == 0:
                    smalljet_random_respawn(enemy_smalljet)
                    pain[X], pain[Y] = 0, 0
                    current_enemy_count -= 1
                    num_birds += 1
                    print('You killed ', num_birds, ' birds')

                draw.rect(screen, enemy_tot_colour, (735, 669, current_enemy_count / enemy_count_ratio, 15))

    # Checking if certain number 3 jets and 10 birds have been taken down, then display victory
    if num_jet >= 5 and  num_birds >= 15:
        win()

# Check if jet bullets hit you, then display 'GAME OVER' if dead
def bullet_hit_soldier():

    global soldier_CURRENT_HEALTH, soldier_CURRENT_SHIELD, soldier_HEALTH_colour, soldier_SHIELD_colour

    for pain in jet_bullets:
        if distance(pain[X], pain[Y], goodGuy[X], goodGuy[Y]) < 35:

            # This deletes the accumulating bullets in the "jet_bullets" list
            # The bullets that have not hit the soldier and gone out of the window screen will still be in the list in chronological order
            # As soon as one of the bullet hits, I have a list of redundant bullet items in the list
            # To delete all previous bullet items from the list, including this one, I delete from current bullet item to the first bullet shot
            del jet_bullets[:jet_bullets.index(pain) + 1]
            
            soldier_health_shield_BAR(15)

        draw.rect(screen, soldier_SHIELD_colour, (277, 669, soldier_CURRENT_SHIELD / soldier_SHIELD_RATIO, 15))
        draw.rect(screen, soldier_HEALTH_colour, (55, 669, soldier_CURRENT_HEALTH / soldier_HEALTH_RATIO, 15))        

        if soldier_CURRENT_HEALTH <= 0:                 
            game_over()


# For the rotations of the images
def soldier_enemy_Rotate(screen, jet, small_Jets, goodGuy):
    #ROTATING SURFACES

    # The jet pic
    jetAng = degrees( atan2( -(goodGuy[Y] - jet[Y]), goodGuy[X] - jet[X] ) )
    rotate_jet = transform.rotate(jetPic, jetAng - 90) # a Surface

    # Center the rotation
    jet_rotate_coordinate = (jet[X]-rotate_jet.get_width()//2, jet[Y]-rotate_jet.get_height()//2)
    screen.blit(rotate_jet, jet_rotate_coordinate)

    # The small jets pic (sJet = small Jet)
    for sJet in small_Jets:
        birdAng = degrees( atan2( -(goodGuy[Y] - sJet[Y]), goodGuy[X] - sJet[X] ) )
        rotate_smallJet = transform.rotate(small_jetPic, birdAng - 90) # a Surface

        # Center the rotation
        smallJet_rotate_coordinate = (sJet[X]-rotate_smallJet.get_width()//2, sJet[Y]-rotate_smallJet.get_height()//2)    
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
        # In-game BG
        screen.blit(background, (0, 0))

        mouse.set_visible(False)

        soldier_enemy_Stats()       

        soldier_enemy_Rotate(screen, jet, small_Jets, goodGuy)
        move_soldier(goodGuy, keys)
        moveBadGuys(jet, small_Jets, goodGuy[X], goodGuy[Y])

        Bullets_soldier(goodGuy[X], goodGuy[Y])    
        Bullets_Jet(goodGuy[X], goodGuy[Y])
        bulletsFired()

        bullet_hit_enemy(jet, small_Jets, birds_HEALTH, jet_HEALTH)
        bullet_hit_soldier()

        checkCollisions(small_Jets)

        crosshair_rect.center = mx, my
        screen.blit(crosshair, crosshair_rect)

        # draw.circle(screen, MAGENTA, goodPic_rect.topleft, 5, 0)
        # draw.circle(screen, MAGENTA, goodPic_rect.center, 5, 0)
        # draw.rect(screen, TURQUOISE, goodPic_rect, 2)

        # draw.circle(screen, MAGENTA, jetPic_rect.topleft, 5, 0)
        # draw.circle(screen, MAGENTA, jetPic_rect.center, 5, 0)
        # draw.rect(screen, TURQUOISE, jetPic_rect, 2)


    myClock.tick(30)     # delay

    display.flip()