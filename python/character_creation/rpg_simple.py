# cpex_framerate.py

import pygame
import os
import random
pygame.init()

def hello() :
    # declare constants
    screen_width = 1300
    screen_height = 900
    screen_size = (screen_width,screen_height)
    screen_mode = 0
    show_mouse = True

    

    # colors
    RED = (255,0,0,255) # (red,green,blue,alpha(transparentcy) )
    BLUE = (0,0,255,255) # alpha = 255 no transparency(full color)
    GREEN = (0,255,0,255) # alpha = 0 fully transparent
    BLACK = (0,0,0,255)
    TRANSPARENT = (0,0,0,0)
    NETTING = (0,0,0,130)
    NIGHTSKY = (8,8,40,255)
    STARLIGHT = (220,220,220,255)
    GOLD = (240,230,20,255)
    BROWN = (151,71,0,255)
    ORANGE = (240,12,12,255)
    WHITE = (255,255,255,255)
    GREY = (40,40,40,255)

    # surfaces
    screen = pygame.display.set_mode(screen_size,screen_mode,32)
    map_surface = pygame.Surface((screen_size))
    mask_surface = pygame.Surface((screen_size))
    characters_surface = pygame.Surface((screen_size))
    pygame.display.set_caption('stub')
    font = pygame.font.SysFont('LittleLordFontleroy',80)
    pygame.mouse.set_visible(show_mouse)

    path = os.getcwd()
    selection_screen = pygame.image.load('%s\character_selection.png'%(path))
    creation_mask = pygame.image.load('%s\creation_mask.png'%(path))
    hats = {}
    skins = {}
    shirts = {}
    pants = {}
    eyes = {}
    hats [0] = ((0,0,100),pygame.image.load('%s\Hats\Ballcap.png'%(path)))
    hats [1] = ((100,0,100),pygame.image.load('%s\Hats\Tophat.png'%(path)))
    hats [2] = ((100,100,0),pygame.image.load('%s\Hats\Chefhat.png'%(path)))
    hats [3] = ((0,100,100),pygame.image.load('%s\Hats\Sombrero.png'%(path)))
    skins [0] = ((255,0,0),pygame.image.load('%s\Skins\Character_skin_1.png'%(path)))
    skins [1] = ((0,255,0),pygame.image.load('%s\Skins\Character_skin_2.png'%(path)))
    skins [2] = ((0,0,255),pygame.image.load('%s\Skins\Character_skin_3.png'%(path)))
    skins [3] = ((255,255,0),pygame.image.load('%s\Skins\Character_skin_4.png'%(path)))
    shirts [0] = ((0,0,200),pygame.image.load('%s\Shirts\Tshirt.png'%(path)))
    shirts [1] = ((100,100,100),pygame.image.load('%s\Shirts\Longsleeve.png'%(path)))
    shirts [2] = ((200,0,0),pygame.image.load('%s\Shirts\Tanktop.png'%(path)))
    shirts [3] = ((0,200,0),pygame.image.load('%s\Shirts\Buttonup.png'%(path)))
    pants [0] = ((200,0,200),pygame.image.load('%s\Bottoms\Slacks.png'%(path)))
    pants [1] = ((200,200,200),pygame.image.load('%s\Bottoms\Shorts.png'%(path)))
    pants [2] = ((200,200,0),pygame.image.load('%s\Bottoms\Shortskirt.png'%(path)))
    pants [3] = ((0,200,200),pygame.image.load('%s\Bottoms\Pencilskirt.png'%(path)))
    eyes [0] = ((255,0,255),pygame.image.load('%s\Eyes\Eyes_1.png'%(path)))
    eyes [1] = ((0,255,255),pygame.image.load('%s\Eyes\Eyes_2.png'%(path)))
    eyes [2] = ((100,0,0),pygame.image.load('%s\Eyes\Eyes_3.png'%(path)))
    eyes [3] = ((0,100,0),pygame.image.load('%s\Eyes\Eyes_4.png'%(path)))
    female = pygame.image.load('%s\Female.png'%(path))
    
    class Player():
        def __init__(self,health,attack,role,level,up_images,down_images,left_images,right_images,attack_images,xp):
            self.name = name
            self.health = health
            self.attack = attack
            self.role = role
            self.level = level
            self.animate = 0
            self.x = screen_width/2
            self.y = screen_height/2
            self.up_images = up_images
            self.down_images = down_images
            self.left_images = left_images
            self.right_images = right_images
            self.attack_images = attack_images
            self.move_up = False
            self.move_down = False
            self.move_left = False
            self.move_right = False
            self.xp = xp
            self.inventory = []

    class Enemy():
        def __init__(self,health,attack,up_images,down_images,left_images,right_images,attack_images,level,xp):
            self.name = name
            self.health = health
            self.items = []
            self.attack = attack
            self.up_images = up_images
            self.down_images = down_images
            self.left_images = left_images
            self.right_images = right_images
            self.attack_image = attack_image
            self.move_up = False
            self.move_down = False
            self.move_left = False
            self.move_right = False
            self.level = level
            self.xp = xp

    class NPC():
        def __init__ (self,text,image,name):
            self.text = text
            self.image = image
            self.name = name

    class Room():
        def __init__ (self,image,adjacent):
            self.image = image
            self.adjacent = adjacent
    
    
    shirt = shirts[random.randint(0,3)]
    pant = pants[random.randint(0,3)]
    hat = hats[random.randint(0,3)]
    skin = skins[random.randint(0,3)]
    eye = eyes[random.randint(0,3)]
    gender = 'male'

    name = 'NAME'
    naming = False
    GO = False
    role = random.choice(['Wizard','Assassin','Barbarian','Knight'])
    letter = {0:[97,'A'],1:[98,'B'],2:[99,'C'],3:[100,'D'],4:[101,'E'],5:[102,'F'],6:[103,'G'],7:[104,'H'],8:[105,'I'],9:[106,'J'],10:[107,'K'],11:[108,'L'],12:[109,'M'],
              13:[110,'N'],14:[111,'O'],15:[112,'P'],16:[113,'Q'],17:[114,'R'],18:[115,'S'],19:[116,'T'],20:[117,'U'],21:[118,'V'],22:[119,'W'],23:[120,'X'],24:[121,'Y'],25:[122,'Z']}
    
    while True :
        name_text = font.render(name,True,WHITE)
        role_text = font.render('The %s'%(role),True,WHITE)
        mouse_pos = pygame.mouse.get_pos()
        mouse_x = mouse_pos[0]
        mouse_y = mouse_pos[1]
        detect = mask_surface.get_at((mouse_x,mouse_y))

        mask_surface.blit(creation_mask,(0,0))
        map_surface.blit(selection_screen,(0,0))
        map_surface.blit(skin[1],(908,111))
        map_surface.blit(shirt[1],(908,111))
        map_surface.blit(pant[1],(908,111))
        map_surface.blit(eye[1],(908,111))
        map_surface.blit(hat[1],(880,0))
        if gender == 'female':
            map_surface.blit(female,(908,111))
        screen.blit(mask_surface,(0,0))
        screen.blit(map_surface,(0,0))
        screen.blit(name_text,(745,569))
        screen.blit(role_text,(900,0))

        pygame.display.update()

        for event in pygame.event.get() :
            if naming == True:
                if event.type == 2:
                    if event.key >= 97 and event.key <= 122:
                        name += letter[event.key-97][1]
                    elif event.key == 8:
                        name = ""
                    elif event.key == 32:
                        name += " "
                    
            if event.type == 5:
                if detect == (255,100,255):
                    naming = True
                    name = ""
                elif detect == (255,100,0):
                    naming = False
                    gender = 'female'
                elif detect == (255,0,100):
                    naming = False
                    gender = 'male'
                elif detect == (255,100,100):
                    naming = False
                    role = 'Wizard'
                elif detect == (100,255,100):
                    naming = False
                    role = 'Knight'
                elif detect == (0,255,100):
                    naming = False
                    role = 'Assassin'
                elif detect == (100,100,255):
                    naming = False
                    role = 'Barbarian'
                elif detect == (255,255,255):
                    GO = True
                else:
                    for count in hats:
                        if detect == hats[count][0]:
                            hat = hats[count]
                    for count in shirts:
                        if detect == shirts[count][0]:
                            shirt = shirts[count]
                    for count in pants:
                        if detect == pants[count][0]:
                            pant = pants[count]
                    for count in skins:
                        if detect == skins[count][0]:
                            skin = skins[count]
                    for count in eyes:
                        if detect == eyes[count][0]:
                            eye = eyes[count]
                    
                    naming = False
        if GO == True:
            up_hat = pygame.image.load('%s\Hats\%s_up.png'%(path,hat[0]))
            left_hat = pygame.image.load('%s\Hats\%s_left.png'%(path,hat[0]))
            down_hat = pygame.image.load('%s\Hats\%s_down.png'%(path,hat[0]))
            right_hat = pygame.image.load('%s\Hats\%s_right.png'%(path,hat[0]))
            vertical_shirts = [pygame.image.load('%s\Shirts\%s_vertical_1.png'%(path,shirt[0])),pygame.image.load('%s\Shirts\%s_vertical_2.png'%(path,shirt[0])),
                        pygame.image.load('%s\Shirts\%s_vertical_3.png'%(path,shirt[0]))]
            horizontal_shirts = [pygame.image.load('%s\Shirts\%s_horizontal_1.png'%(path,shirt[0])),pygame.image.load('%s\Shirts\%s_horizontal_2.png'%(path,shirt[0])),
                        pygame.image.load('%s\Shirts\%s_horizontal_3.png'%(path,shirt[0]))]
            vertical_skins = [pygame.image.load('%s\Skins\%s_vertical_1.png'%(path,skin[0])),pygame.image.load('%s\Skins\%s_vertical_2.png'%(path,skin[0]))]
            horizontal_skins = [pygame.image.load('%s\Skins\%s_horizontal_1.png'%(path,skin[0])),pygame.image.load('%s\Skins\%s_horizontal_2.png'%(path,skin[0]))]
            up_images = [up_hat,vertical_shirts,vertical_skins]
            down_images = [down_hat,vertical_shirts,vertical_skins]
            left_images = [left_hat,horizontal_shirts,horizontal_skins]
            right_images = [right_hat,horizontal_shirts,horizontal_skins]
            attack_images = 15
            player = Player(100,10,role,0,up_images,down_images,left_images,right_images,attack_images,0)
            break
    room_number = 5
    room = pygame.image.load('%s\Maps\Room_%i.png'%(path,room_number))
    mask = pygame.image.load('%s\Maps\Room_%i_mask.png'%(path,room_number))
    while True:
        map_surface.fill(WHITE)
        mask_surface.blit(mask,(0,0))
        map_surface.blit(room,(0,0))
        if player.x <= 7 and room_number != 1 and room_number != 4 and room_number != 7:
            print(1)
            room_number -= 1
            player.x = screen_width-81
            room = pygame.image.load('%s\Maps\Room_%i.png'%(path,room_number))
            mask = pygame.image.load('%s\Maps\Room_%i_mask.png'%(path,room_number))
        elif player.x >= screen_width-80 and room_number != 3 and room_number != 6 and room_number != 9:
            room_number += 1
            room = pygame.image.load('%s\Maps\Room_%i.png'%(path,room_number))
            mask = pygame.image.load('%s\Maps\Room_%i_mask.png'%(path,room_number))
            player.x = 8
        elif player.y <= 7 and room_number >= 4:
            room_number -= 3
            room = pygame.image.load('%s\Maps\Room_%i.png'%(path,room_number))
            mask = pygame.image.load('%s\Maps\Room_%i_mask.png'%(path,room_number))
            player.y = screen_height-86
        elif player.y >= screen_height-85 and room_number <= 6:
            room_number +=3
            room = pygame.image.load('%s\Maps\Room_%i.png'%(path,room_number))
            mask = pygame.image.load('%s\Maps\Room_%i_mask.png'%(path,room_number))
            player.y = 8
        if player.move_down == True:
            player.animate += 1
            detect = mask_surface.get_at((int(player.x),int(player.y+81)))
            if detect != RED:
                player.y += 2
            if player.animate <= 50:
                map_surface.blit(player.down_images[2][1],(player.x,player.y))
                map_surface.blit(player.down_images[1][0],(player.x,player.y))
                map_surface.blit(player.down_images[0],(player.x,player.y))
            elif player.animate >= 51 and player.animate <= 100:
                map_surface.blit(player.down_images[1][1],(player.x,player.y))
                map_surface.blit(player.down_images[0],(player.x,player.y))
            elif player.animate >= 101 and player.animate <= 150:
                map_surface.blit(player.down_images[2][0],(player.x,player.y))
                map_surface.blit(player.down_images[1][2],(player.x,player.y))
                map_surface.blit(player.down_images[0],(player.x,player.y))
            elif player.animate >= 151 and player.animate <= 200:
                map_surface.blit(player.down_images[1][1],(player.x,player.y))
                map_surface.blit(player.down_images[0],(player.x,player.y))
            elif player.animate >= 201:
                map_surface.blit(player.down_images[1][1],(player.x,player.y))
                map_surface.blit(player.down_images[0],(player.x,player.y))
                player.animate = 0
        elif player.move_up == True:
            player.animate += 1
            detect = mask_surface.get_at((int(player.x),int(player.y-3)))
            if detect != RED:
                player.y -= 2
            if player.animate <= 50:
                map_surface.blit(player.up_images[2][1],(player.x,player.y))
                map_surface.blit(player.up_images[1][0],(player.x,player.y))
                map_surface.blit(player.up_images[0],(player.x,player.y))
            elif player.animate >= 51 and player.animate <= 100:
                map_surface.blit(player.up_images[1][1],(player.x,player.y))
                map_surface.blit(player.up_images[0],(player.x,player.y))
            elif player.animate >= 101 and player.animate <= 150:
                map_surface.blit(player.up_images[2][0],(player.x,player.y))
                map_surface.blit(player.up_images[1][2],(player.x,player.y))
                map_surface.blit(player.up_images[0],(player.x,player.y))
            elif player.animate >= 151 and player.animate <= 200:
                map_surface.blit(player.up_images[1][1],(player.x,player.y))
                map_surface.blit(player.up_images[0],(player.x,player.y))
            elif player.animate >= 201:
                map_surface.blit(player.up_images[1][1],(player.x,player.y))
                map_surface.blit(player.up_images[0],(player.x,player.y))
                player.animate = 0
        if player.move_right == True:
            detect = mask_surface.get_at((int(player.x+78),int(player.y)))
            if detect != RED:
                player.x += 2
            if player.move_up != True and player.move_down != True:
                player.animate += 1
                if player.animate <= 50:
                    map_surface.blit(player.right_images[2][1],(player.x,player.y))
                    map_surface.blit(player.right_images[1][0],(player.x,player.y))
                    map_surface.blit(player.right_images[0],(player.x,player.y))
                elif player.animate >= 51 and player.animate <= 100:
                    map_surface.blit(player.right_images[1][1],(player.x,player.y))
                    map_surface.blit(player.right_images[0],(player.x,player.y))
                elif player.animate >= 101 and player.animate <= 150:
                    map_surface.blit(player.right_images[2][0],(player.x,player.y))
                    map_surface.blit(player.right_images[1][2],(player.x,player.y))
                    map_surface.blit(player.right_images[0],(player.x,player.y))
                elif player.animate >= 151 and player.animate <= 200:
                    map_surface.blit(player.right_images[1][1],(player.x,player.y))
                    map_surface.blit(player.right_images[0],(player.x,player.y))
                elif player.animate >= 201:
                    map_surface.blit(player.right_images[1][1],(player.x,player.y))
                    map_surface.blit(player.right_images[0],(player.x,player.y))
                    player.animate = 0
        elif player.move_left == True:
            detect = mask_surface.get_at((int(player.x-3),int(player.y)))
            if detect != RED:
                player.x -= 2
            if player.move_up != True and player.move_down != True:
                player.animate += 1
                if player.animate <= 50:
                    map_surface.blit(player.left_images[2][1],(player.x,player.y))
                    map_surface.blit(player.left_images[1][0],(player.x,player.y))
                    map_surface.blit(player.left_images[0],(player.x,player.y))
                elif player.animate >= 51 and player.animate <= 100:
                    map_surface.blit(player.left_images[1][1],(player.x,player.y))
                    map_surface.blit(player.left_images[0],(player.x,player.y))
                elif player.animate >= 101 and player.animate <= 150:
                    map_surface.blit(player.left_images[2][0],(player.x,player.y))
                    map_surface.blit(player.left_images[1][2],(player.x,player.y))
                    map_surface.blit(player.left_images[0],(player.x,player.y))
                elif player.animate >= 151 and player.animate <= 200:
                    map_surface.blit(player.left_images[1][1],(player.x,player.y))
                    map_surface.blit(player.left_images[0],(player.x,player.y))
                elif player.animate >= 201:
                    map_surface.blit(player.left_images[1][1],(player.x,player.y))
                    map_surface.blit(player.left_images[0],(player.x,player.y))
                    player.animate = 0
        else:
            map_surface.blit(player.down_images[1][1],(player.x,player.y))
            map_surface.blit(player.down_images[0],(player.x,player.y))

        screen.blit(mask_surface,(0,0))
        screen.blit(map_surface,(0,0))
        
        pygame.display.update()
                                 
        for event in pygame.event.get() :
            if event.type == 2:
                if event.key == 274:
                    player.move_down = True
                elif event.key == 273:
                    player.move_up = True
                elif event.key == 276:
                    player.move_left = True
                elif event.key == 275:
                    player.move_right = True
            if event.type == 3:
                player.animate = 0
                if event.key == 274:
                    player.move_down = False
                elif event.key == 273:
                    player.move_up = False
                elif event.key == 276:
                    player.move_left = False
                elif event.key == 275:
                    player.move_right = False
    
if __name__ == '__main__' :
    hello()
