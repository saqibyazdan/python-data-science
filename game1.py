# run this in terminal -> pip install pgzero
import pgzrun
from random import randint
WIDTH = 800
HEIGHT = 600
score = 0
music.play("avenger_piano")
player = Actor("ironman", (WIDTH//2, HEIGHT//2))
coin = Actor('coin', (randint(50, WIDTH-50), 
                      randint(50, HEIGHT-50)))
alien = Actor('alien', (-100, HEIGHT//2,))
ps = 5 # player speed
es = 1 # enemy speed
def player_movement():
    global score
    if keyboard.left:
        player.x -= ps
        player.angle = 10
    elif keyboard.right:
        player.x += ps
        player.angle = -10
    elif keyboard.up:
        player.y -= ps
    elif keyboard.down:
        player.y += ps
    else:
        player.angle = 0
    # collision detection
    if player.colliderect(coin):
        player.image = 'ironman'
        coin.x = randint(50, WIDTH-50)
        coin.y = randint(50, HEIGHT-50)
        score += 1
        sounds.action2.play()
        

def enemy_movement():
    global score
    if alien.x < player.x:
        alien.x += es
    elif alien.x > player.x:
        alien.x -= es
    if alien.y < player.y:
        alien.y += es
    elif alien.y > player.y:
        alien.y -= es
    if alien.colliderect(player):
        player.image = 'dead_ironman'
        sounds.action3.play()
        score = score-1
        
    

def draw():
    screen.fill("black")
    screen.draw.text(
        f"Score:{score}",
        color="red",
        topleft=(10, 10),
        fontsize=30
    )
    player.draw()
    coin.draw()
    alien.draw()
   

def update(dt):
    player_movement()
    enemy_movement()
pgzrun.go()