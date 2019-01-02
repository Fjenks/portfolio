# pyLife.py

#LIFE SIMULATION INCLUDING:
#   - HERBIVORES/PREY THAT TRAVEL IN HERDS TO CONSUME PLANTS
#   - CARNIVORES/PREDATORS THAT IDLE UNTIL HUNGER BECOMES HIGH ENOUGH TO HUNT
#   - PLANTS THAT SPREAD AND GROW

import pygame
import time
import random
import os
pygame.init()


class Herd():
    def __init__(self):
        self.moving = False
        self.members = {}
        self.destination_x = 0
        self.destination_y = 0
        self.begin = 0
class Predator():
    def __init__(self,x,y,sight,speed):
        self.x = x
        self.y = y
        self.sight = sight
        self.speed = speed
        self.alive = True
        self.destination_x = x
        self.destination_y = y
        self.hunger = 0
        self.size = 3
        self.stopped = True
        self.food = None
        self.age = 0
        self.life = random.randint(1300,1500)
        self.hungry = random.randint(1000,1750)
    
    
class Prey():
    def __init__(self,x,y,sight,speed,herd):
        self.x = x
        self.y = y
        self.sight = sight
        self.speed = speed
        self.alive = True
        self.destination_x = x
        self.destination_y = y
        self.food = False
        self.age = 0
        self.stopped = True
        self.hunger = 0
        self.size = 2
        self.herd = herd
        self.death_count = 0
    
class Plant():
    def __init__(self,number,x,y,age,life,fertility):
        self.number = number
        self.x = x
        self.y = y
        self.age = age
        self.life = life
        self.fertility = fertility
        self.alive = True
        self.size = 4


def hello() :
    # declare constants
    screen_width = 1000
    screen_height = 700
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
    DARK_RED = (100,0,0,255)

    # surfaces
    sight_screen = pygame.Surface((screen_size))
    screen = pygame.display.set_mode(screen_size,screen_mode,32)
    pygame.display.set_caption('stub')
    font = pygame.font.SysFont('Parchment',48)
    small_font = pygame.font.SysFont('Parchment',24)
    pygame.mouse.set_visible(show_mouse)

    predators = {}
    prey = {}
    herds = []
    plants = {}
    new_plants = {}
    new_predator = {}
    new_prey = {}
    cull = []
    prey_cull = []
    new_prey_cull = []
    pred_cull = []
    new_pred_cull = []
    end = False
    new_herds = {}
    new_cull = []
    herds = {}
    genders = ['female','male']
    plant_count = 0
    pred_count = 0
    prey_count = 0
    pred_initial = random.randrange(3,7)
    no_plant = False
    prey_initial = random.randrange(25,50)
    plant_initial = random.randrange(10,20)
    for count in range(0,random.randrange(10,15)):
        herds[count] = Herd()
    for count in range(0,pred_initial):
        x = random.randrange(0,screen_width)
        y = random.randrange(0,screen_height)
        sight = random.randrange(25,50)
        speed = 1
        predators[pred_count] = Predator(x,y,sight,speed)
        pred_count += 1
    for count in range(0,prey_initial):
        x = random.randrange(0,screen_width)
        y = random.randrange(0,screen_height)
        sight = random.randrange(10,35)
        speed = 2
        herd = random.randint(0,len(herds)-1)
        prey[prey_count] = Prey(x,y,sight,speed,herd)
        herds[herd].members[prey_count] = (prey[prey_count])
        prey[prey_count].size = 6
        prey_count += 1
    for count in range(0,plant_initial):
        x = random.randrange(0,screen_width)
        y = random.randrange(0,screen_height)
        age = 0
        life = random.randrange(1000,5000)
        fertility = random.randrange(0,100)
        plants[plant_count] = Plant(plant_count,x,y,age,life,fertility)
        plant_count += 1

    
    # resources pics/sounds


    # frame loop
    while True:
        screen.fill(BLACK)
        sight_screen.fill(BLACK)
        screen.blit(sight_screen,(0,0))

        for count in prey:
            pygame.draw.circle(sight_screen,BLUE,(prey[count].x,prey[count].y),prey[count].sight,0)
            pygame.draw.circle(screen,GREY,(prey[count].x,prey[count].y),prey[count].sight,0)
            pygame.draw.rect(screen,WHITE,(prey[count].x,prey[count].y,prey[count].size,prey[count].size))
        for count in predators:
            pygame.draw.circle(sight_screen,ORANGE,(predators[count].x,predators[count].y),predators[count].sight,0)
            pygame.draw.circle(screen,DARK_RED,(predators[count].x,predators[count].y),predators[count].sight,0)
            pygame.draw.rect(screen,RED,(predators[count].x,predators[count].y,9,9))
        for count in plants:
            pygame.draw.rect(screen,GREEN,(plants[count].x,plants[count].y,plants[count].size,plants[count].size))
        plantline = font.render('Plants: %i'%(len(plants)),True,GREEN).convert_alpha()
        screen.blit(plantline,(10,10))
        preyline = font.render('Prey: %i'%(len(prey)),True,WHITE).convert_alpha()
        screen.blit(preyline,(10,50))
        predline = font.render('Predators: %i'%(len(predators)),True,RED).convert_alpha()
        screen.blit(predline,(10,90))
        

        pygame.draw.rect(screen,GOLD,(screen_width-125,20,100,280))
        pygame.draw.line(screen,BLACK,(screen_width-125,95),(screen_width-25,95),4)
        pygame.draw.line(screen,BLACK,(screen_width-125,170),(screen_width-25,170),4)
        pygame.draw.line(screen,BLACK,(screen_width-125,250),(screen_width-25,250),4)
        pygame.draw.rect(screen,GREEN,(screen_width-80,40,15,15))
        pygame.draw.rect(screen,WHITE,(screen_width-80,115,15,15))
        pygame.draw.rect(screen,RED,(screen_width-80,190,15,15))
        pygame.draw.line(screen,BLACK,(screen_width-115,80),(screen_width-95,80),4)
        pygame.draw.line(screen,BLACK,(screen_width-60,80),(screen_width-35,80),4)
        pygame.draw.line(screen,BLACK,(screen_width-105,70),(screen_width-105,90),4)
        
        pygame.draw.line(screen,BLACK,(screen_width-115,155),(screen_width-95,155),4)
        pygame.draw.line(screen,BLACK,(screen_width-60,155),(screen_width-35,155),4)
        pygame.draw.line(screen,BLACK,(screen_width-105,145),(screen_width-105,165),4)

        pygame.draw.line(screen,BLACK,(screen_width-115,230),(screen_width-95,230),4)
        pygame.draw.line(screen,BLACK,(screen_width-60,230),(screen_width-35,230),4)
        pygame.draw.line(screen,BLACK,(screen_width-105,220),(screen_width-105,240),4)
        continueline = small_font.render('CONTINUE',True,BLACK).convert_alpha()
        screen.blit(continueline,(screen_width-120,260))
        pygame.draw.rect(sight_screen,WHITE,(screen_width-115,220,20,20))
        pygame.draw.rect(sight_screen,GREEN,(screen_width-60,220,20,20))
        pygame.draw.rect(sight_screen,RED,(screen_width-115,145,20,20))
        pygame.draw.rect(sight_screen,BROWN,(screen_width-60,145,20,20))
        pygame.draw.rect(sight_screen,GREY,(screen_width-115,70,20,20))
        pygame.draw.rect(sight_screen,GOLD,(screen_width-60,70,20,20))
        pygame.draw.rect(sight_screen,STARLIGHT,(screen_width-125,250,100,50))
        mouse_pos = pygame.mouse.get_pos()
        detect = pygame.mouse.get_pressed()
        color = sight_screen.get_at((mouse_pos))
        if color == WHITE:
            pygame.draw.rect(screen,WHITE,(screen_width-118,217,26,26),3)
        elif color == GREEN:
            pygame.draw.rect(screen,WHITE,(screen_width-63,217,28,26),3)
        elif color == RED:
            pygame.draw.rect(screen,WHITE,(screen_width-118,142,26,26),3)
        elif color == BROWN:
            pygame.draw.rect(screen,WHITE,(screen_width-63,142,28,26),3)
        elif color == GREY:
            pygame.draw.rect(screen,WHITE,(screen_width-118,67,26,26),3)
        elif color == GOLD:
            pygame.draw.rect(screen,WHITE,(screen_width-63,67,28,26),3)
        elif color == STARLIGHT:
            pygame.draw.rect(screen,WHITE,(screen_width-125,250,100,50),3)

        for count in new_plants:
            plants[count] = new_plants[count]
            new_cull.append(new_plants[count].number)
        for count in new_predator:
            predators[count] = new_predator[count]
            new_pred_cull.append(count)
        for counter in new_cull:
            del new_plants[counter]
        for counter in new_pred_cull:
            del new_predator[counter]
        new_pred_cull.clear()
        new_cull.clear()
        new_predator.clear()
        new_plants.clear()
        for count in new_prey:
            prey[count] = new_prey[count]
            herds[prey[count].herd].members[count] = prey[count]
            new_prey_cull.append(count)
        for counter in cull:
            del plants[counter]
        cull.clear()
        for counter in pred_cull:
            del predators[counter]
        pred_cull.clear()
        for count in new_prey_cull :
            del new_prey[count]
        new_prey_cull.clear()
        new_prey.clear()
        for count in prey_cull :
            del prey[count]
        prey_cull.clear()
        if end == True:
            break
        pygame.display.update()
        # processes events
        for event in pygame.event.get() :
            if event.type == 5:
                if color == GREY:
                    x = random.randrange(0,screen_width)
                    y = random.randrange(0,screen_height)
                    age = 0
                    life = random.randrange(1000,5000)
                    fertility = random.randrange(0,100)
                    new_plants[plant_count] = Plant(plant_count,x,y,age,life,fertility)
                    plant_count += 1
                elif color == GOLD:
                    cull.append(plant_count-1)
                    plant_count -= 1
                elif color == RED:
                    x = random.randrange(0,screen_width)
                    y = random.randrange(0,screen_height)
                    sight = random.randrange(10,35)
                    herd = random.randint(0,len(herds)-1)
                    new_prey[prey_count] = Prey(x,y,sight,1,herd)
                    prey_count += 1
                elif color == BROWN:
                    prey_cull.append(prey_count-1)
                    prey_count -= 1
                elif color == WHITE:
                    x = random.randrange(0,screen_width)
                    y = random.randrange(0,screen_height)
                    sight = random.randrange(25,50)
                    speed = 1
                    predators[pred_count] = Predator(x,y,sight,speed)
                    pred_count += 1
                elif color == GREEN:
                    pred_cull.append(pred_count-1)
                    pred_count -= 1
                elif color == STARLIGHT:
                    end = True
    while True :
        screen.fill(BLACK)
        sight_screen.fill(BLACK)
        screen.blit(sight_screen,(0,0))
        random_plant = random.randint(0,100)
        if random_plant == 50:
            plants[plant_count] = Plant(plant_count,random.randrange(0,screen_width),random.randrange(0,screen_height),0,random.randrange(1,5000),random.randrange(0,100))
            plant_count += 1
        for count in prey:
            pygame.draw.circle(sight_screen,BLUE,(prey[count].x,prey[count].y),prey[count].sight,0)
            pygame.draw.circle(screen,GREY,(prey[count].x,prey[count].y),prey[count].sight,0)
            prey[count].age += 1
            if prey[count].age == 1000 :
                prey[count].size += 2
            elif prey[count].age == 2000:
                prey[count].speed = 2
                prey[count].size += 2
            elif prey[count].age == 1000 or prey[count].age == 2000 or prey[count].age == 3000 :
                chance = random.randint(0,100)
                if chance >= 85 :
                    for mating in prey:
                        if prey[mating].herd == prey[count].herd :
                            x = prey[count].x + 5
                            y = prey[count].y + 5
                            sight = int(((prey[count].sight+prey[mating].sight)/2)+1)
                            new_prey[prey_count] = Prey(x,y,sight,1,prey[count].herd)
                            prey_count += 1
        for count in predators:
            predators[count].age += 1
            pygame.draw.circle(sight_screen,ORANGE,(predators[count].x,predators[count].y),predators[count].sight,0)
            pygame.draw.circle(screen,DARK_RED,(predators[count].x,predators[count].y),predators[count].sight,0)
            if predators[count].food == None:
                predators[count].hunger += 1
                if predators[count].stopped == True:
                    predators[count].destination_x = random.randint(0,screen_width)
                    predators[count].destination_y = random.randint(0,screen_height)
                    predators[count].stopped = False
        for count in predators:
            predators[count].age += 1
            if predators[count].hunger >= predators[count].life:
                predators[count].alive = False
            if predators[count].alive == False:
                pred_cull.append(count)
        for count in prey :
            if prey[count].death_count >= 3000:
                prey[count].alive = False
            if prey[count].alive == True:
                prey[count].hunger += 1
                pygame.draw.rect(screen,WHITE,(prey[count].x,prey[count].y,prey[count].size,prey[count].size))
                if prey[count].hunger >= 2000:
                    prey_cull.append(count)
                    
        for count in predators:
            if predators[count].age == 3000 or predators[count].age == 1000 or predators[count].age == 2000 or predators[count].age == 4000 or predators[count].age == 5000:
                chance = random.randint(0,100)
                if chance >= 85 :
                    for mating in predators:
                        x = predators[count].x + 5
                        y = predators[count].y + 5
                        sight = int(((predators[count].sight+predators[mating].sight)/2)+1)
                        new_predator[pred_count] = Predator(x,y,sight,1)
                        pred_count += 1
                        break
            if predators[count].alive == True:
                pygame.draw.rect(screen,RED,(predators[count].x,predators[count].y,9,9))
                
        for count in plants:
            if plants[count].alive == True:
                pygame.draw.rect(screen,GREEN,(plants[count].x,plants[count].y,plants[count].size,plants[count].size))
                
        for count in plants:
            for check in plants:
                if plants[count].x == plants[check].x and plants[count].y == plants[check].y and plants[count].number != plants[check].number:
                    plants[count].alive = False
            if plants[count].alive == False:
                cull.append(plants[count].number)
                continue
            if plants[count].age == 1000:
                plants[count].size += 2
            elif plants[count].age == 1500:
                plants[count].size += 2
            elif plants[count].age == 2000:
                plants[count].size += 2
            elif plants[count].age == 2500:
                plants[count].size += 2
            elif plants[count].age == 3000:
                plants[count].size += 2
            elif plants[count].age >= plants[count].life:
                plants[count].alive = False
                continue
            plants[count].age += 1
            reproduce_chance = random.randrange(0,100)
            if plants[count].age >= 500 and plants[count].age <= 3000:
                if reproduce_chance <= plants[count].fertility :
                    direction = random.randint(0,4)
                    if direction == 0:
                        if plants[count].x+15 >= screen_width:
                            break
                        else:
                            detect = screen.get_at((plants[count].x+15,plants[count].y))
                        if detect == GREEN:
                            pass
                        else:
                            new_plants[plant_count] = Plant(plant_count,plants[count].x+15,plants[count].y,0,random.randrange(3000,5000),random.randrange(0,100))
                            plant_count += 1
                            plants[count].fertility -= 30
                            
                    elif direction == 1:
                        if plants[count].x-15 <= 0:
                            break
                        else:
                            detect = screen.get_at((plants[count].x-15,plants[count].y))
                        if detect == GREEN:
                            pass
                        else:
                            new_plants[plant_count] = Plant(plant_count,plants[count].x-15,plants[count].y,0,random.randrange(3000,5000),random.randrange(0,100))
                            plant_count += 1
                            plants[count].fertility -= 30
                            
                    elif direction == 2:
                        if plants[count].y+15 >= screen_height:
                            break
                        else:
                            detect = screen.get_at((plants[count].x,plants[count].y+15))
                        if detect == GREEN:
                            pass
                        else:
                            new_plants[plant_count] = Plant(plant_count,plants[count].x,plants[count].y+15,0,random.randrange(3000,5000),random.randrange(0,100))
                            plant_count += 1
                            plants[count].fertility -= 30
                            
                    elif direction == 3:
                        if plants[count].y-15 <= 0:
                            break
                        else:
                            detect = screen.get_at((plants[count].x,plants[count].y-15))
                        if detect == GREEN:
                            pass
                        else:
                            new_plants[plant_count] = Plant(plant_count,plants[count].x,plants[count].y-15,0,random.randrange(3000,5000),random.randrange(0,100))
                            plant_count += 1
                            plants[count].fertility -= 30
        
        for count in prey:
            if prey[count].alive == False:
                prey_cull.append(count)
        for movement in range(0,len(herds)):
            if herds[movement].moving == False:
                plant_select = random.randint(0,len(plants)-1)
                for count in plants:
                    if count == plant_select:
                        herds[movement].destination_x = plants[count].x
                        herds[movement].destination_y = plants[count].y
                        break
                
            if herds[movement].moving == False:
                for count in prey:
                    if prey[count].herd == movement:
                        prey[count].destination_x = random.randrange(herds[movement].destination_x-20,herds[movement].destination_x+20)
                        prey[count].destination_y = random.randrange(herds[movement].destination_y-20,herds[movement].destination_y+20)
                        prey[count].stopped = False
                herds[movement].moving = True

        for movement in herds:
            for count in herds[movement].members:
                if herds[movement].members[count].stopped == False:
                    break
                for food in plants:
                    try:
                        detect = sight_screen.get_at((plants[food].x-1,plants[food].y-1))
                    except:
                        pass
                    if detect == BLUE:
                        plants[food].alive = False
                        for eating in herds[movement].members:
                            herds[movement].members[eating].hunger -= 500*plants[food].size
                herds[movement].begin += 1
                if herds[movement].begin == len(herds[movement].members)-1:
                    herds[movement].moving = False
                    herds[movement].begin = 0

        for count in predators:
            if predators[count].hunger >= predators[count].hungry:
                if predators[count].food == None:
                    predators[count].food = random.randint(0,len(prey)-1)
                for counting in prey:
                    if counting == predators[count].food:
                        predators[count].stopped = False
                        predators[count].destination_x = prey[counting].x
                        predators[count].destination_y = prey[counting].y
                        predators[count].speed = 3
                    if prey[counting].stopped == True:
                        predators[count].stopped = False
                        predators[count].destination_x = prey[counting].x
                        predators[count].destination_y = prey[counting].y
                        predators[count].speed = 3
                
        for count in prey:
            if prey[count].stopped == True:
                prey[count].death_count += 1
                continue
            else:
                prey[count].death_count = 0
            if prey[count].x >= prey[count].destination_x :
                new_x = int(prey[count].x-(prey[count].speed))
                prey[count].x = new_x
            elif prey[count].x <= prey[count].destination_x:
                new_x = int(prey[count].x+(prey[count].speed))
                prey[count].x = new_x
            if prey[count].y >= prey[count].destination_y :
                new_y = int(prey[count].y-(prey[count].speed))
                prey[count].y = new_y
            elif prey[count].y <= prey[count].destination_y:
                new_y = int(prey[count].y+(prey[count].speed))
                prey[count].y = new_y
            if prey[count].y >= prey[count].destination_y-5 and prey[count].y <= prey[count].destination_y+5 and prey[count].x >= prey[count].destination_x-5 and prey[count].x <= prey[count].destination_x+5:
                prey[count].stopped = True

        for count in predators:
            if predators[count].stopped == True:
                continue
            if predators[count].x >= predators[count].destination_x :
                new_x = predators[count].x-predators[count].speed
                predators[count].x = new_x
            elif predators[count].x <= predators[count].destination_x:
                new_x = predators[count].x+predators[count].speed
                predators[count].x = new_x
            if predators[count].y >= predators[count].destination_y :
                new_y = predators[count].y-predators[count].speed
                predators[count].y = new_y
            elif predators[count].y <= predators[count].destination_y:
                new_y = predators[count].y+predators[count].speed
                predators[count].y = new_y
            if predators[count].y >= predators[count].destination_y-10 and predators[count].y <= predators[count].destination_y+10 and predators[count].x >= predators[count].destination_x-10 and predators[count].x <= predators[count].destination_x+10:
                predators[count].stopped = True
                if predators[count].food not in [None]:
                    try:
                        prey[predators[count].food].alive = False
                    except:
                        for please in prey:
                            if prey[please].x == predators[count].destination_x and prey[please].y == predators[count].destination_y:
                                prey[please].alive = False
                    predators[count].hunger -= 750
                    predators[count].speed = 1
                    predators[count].food = None

        for count in new_plants:
            plants[new_plants[count].number] = new_plants[count]
            new_cull.append(new_plants[count].number)
        for count in new_predator:
            predators[count] = new_predator[count]
            new_pred_cull.append(count)
        for counter in new_cull:
            del new_plants[counter]
        for counter in new_pred_cull:
            del new_predator[counter]
        new_pred_cull.clear()
        new_cull.clear()
        new_predator.clear()
        new_plants.clear()
        for count in new_prey:
            prey[count] = new_prey[count]
            herds[prey[count].herd].members[count] = prey[count]
            new_prey_cull.append(count)
        for counter in cull:
            del plants[counter]
        cull.clear()
        for counter in pred_cull:
            del predators[counter]
        pred_cull.clear()
        for count in new_prey_cull :
            del new_prey[count]
        new_prey_cull.clear()
        new_prey.clear()
        for count in prey_cull :
            del prey[count]
        prey_cull.clear()
        # time accounting

        # move things

        # interactions of things
        
        # blit things(draw)

        plantline = font.render('Plants: %i'%(len(plants)),True,GREEN).convert_alpha()
        screen.blit(plantline,(10,10))
        preyline = font.render('Prey: %i'%(len(prey)),True,WHITE).convert_alpha()
        screen.blit(preyline,(10,50))
        predline = font.render('Predators: %i'%(len(predators)),True,RED).convert_alpha()
        screen.blit(predline,(10,90))
        
        
        
        pygame.display.update()
        # processes events
        for event in pygame.event.get() :
            pass
        

    
if __name__ == '__main__' :
    hello()

