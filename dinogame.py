import pygame
import random

pygame.init()
screen = pygame.display.set_mode((720, 500))
clock = pygame.time.Clock()
dino_gif=pygame.image.load("dino.png")
cactus_image=pygame.image.load("cactus.png")
font_score=pygame.font.Font("PressStart2P-Regular.ttf",20)
text_surface_score = font_score.render("example" , True , "grey")

gameover_font=pygame.font.Font("PressStart2P-Regular.ttf",30)
text_surface_gameover = gameover_font.render("example" , True , "grey")

restart_font=pygame.font.Font("PressStart2P-Regular.ttf",10)
text_surface_restart = font_score.render("example" , True , "grey")


class Player:
    def __init__(self):
        self.x = 1
        self.y = 450
        self.height = 50
        self.width = 50
        self.color = "black"
        self.state = "standing"
        self.alive = True
        self.score = 0

    def gravity(self):
        if self.state == "jumping":
            self.y -= 10
        if self.y < 300:
            self.state = "falling"
        if self.state == "falling":
            self.y += 5
        if self.y >= 450:
            self.state = "standing"

    def move(self):
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_w] or keys[pygame.K_SPACE]) and self.state == "standing":
            self.state = "jumping"

class Cactus:

    def __init__(self):
        self.height = random.randint(20,30) 
        self.x = 720
        self.y =    500 - self.height
        self.width = 26 
        self.color = random.choice(["white"]) 
        self.speed = 7

    def move(self , other:'Cactus'):
        self.x -= self.speed
        if self.x < 0:

            while True : 
                self.x = random.randint(720, 1300)

                diff = abs(self.x - other.x) 

                if diff > 200 or diff < 20 :
                    break

            self.height = 62
            self.y =    500 - self.height
            self.color = "white"
            self.speed += 0.1

    def collision(self , player):
        
        if (player.x + player.width +3) >= self.x:
            if (player.y + player.height) >= self.y :
                screen.fill("white")
                player.alive = "false"


player = Player()
cactus1 = Cactus()
random_space = random.randint(100, 500)
cactus2 = Cactus()
cactus2.x = cactus1.x + random_space

game_start = False


def draw():
    pygame.draw.rect(screen, "white", [player.x, player.y, player.width, player.height])
    pygame.draw.rect(screen, cactus1.color, [cactus1.x, cactus1.y, cactus1.width, cactus1.height])
    pygame.draw.rect(screen, "white", [cactus2.x, cactus2.y, cactus2.width, cactus2.height])

def handle_score_restart():
    if player.alive == "true":
        player.move()
        player.gravity() 
        cactus1.move(cactus2)
        cactus2.move(cactus1)
        score =+ 1
        pass

    else : 
        keys = pygame.key.get_pressed()

        if (keys[pygame.K_w] or keys[pygame.K_r]):
            player.alive = "true" 
            cactus1.x = 500
            cactus2.x = 800
            player.score = 0

player.alive = "true"
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False



    screen.fill("white")

    if not game_start : 
        print("not started yet")
        pygame.display.flip()
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_s]):
            game_start = True
        continue
        

    cactus2.collision(player)
    cactus1.collision(player)  

 

    text_surface = font_score.render(f"Score : {player.score }" , True , "#535353")
    screen.blit(text_surface , [400,0,500,100])   
    restart="To restart press W or R key."
    gameover="G A M E  O V E R"
    if player.alive == "true":
      player.score += 1
    else:
        player.score = player.score
    if player.alive != "true":
        text_surface_restart = restart_font.render( restart , True , "#535353")
        screen.blit(text_surface_restart , [230,250,800,100])

        text_surface_gameover = gameover_font.render( gameover , True , "#535353")
        screen.blit(text_surface_gameover , [130,150,600,100])   
    draw()
    handle_score_restart()

    
    cactus_image = pygame.transform.scale(cactus_image , ( cactus1.width , cactus1.height))
    screen.blit(cactus_image , (cactus1.x , cactus1.y))
    screen.blit(cactus_image , (cactus2.x , cactus2.y))

    dino_image = pygame.transform.scale(dino_gif , ( player.width , player.height))
    screen.blit(dino_image, (player.x , player.y))
    pygame.display.flip()
    clock.tick(80)

pygame.quit()
 