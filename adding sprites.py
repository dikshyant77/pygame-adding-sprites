import random
import pygame

surf_color = (0, 142, 204)
color = (142, 0, 23)

class Sprite(pygame.sprite.Sprite):

  def __init__(self, color, height, width):
    super().__init__()
    self.image = pygame.Surface([width, height])
    self.image.fill(surf_color)
    pygame.draw.rect(self.image, color, pygame.Rect(0, 0, width, height))
    self.rect = self.image.get_rect()
pygame.init()

all_sprites_list = pygame.sprite.Group()
screen = pygame.display.set_mode((500, 400))
pygame.display.set_caption("Creating Sprite")
screen.fill(surf_color)

new_color = (0, 255, 0)
bg_active_color = surf_color

new_sprite_color = (255, 255, 0)
sprite_active_color = color

CHANGE_COLOR = pygame.USEREVENT + 1
color1 = pygame.USEREVENT + 1

pygame.time.set_timer(CHANGE_COLOR, 500)
pygame.time.set_timer(color1, 500)

sp1 = Sprite(sprite_active_color, 20, 30)
sp1.rect.x = random.randint(0, 480)
sp1.rect.y = random.randint(0, 370)
all_sprites_list.add(sp1)

sp2 = Sprite(sprite_active_color, 20, 30)
sp2.rect.x = random.randint(0, 480)
sp2.rect.y = random.randint(0, 370)
all_sprites_list.add(sp2)
exit = True
clock = pygame.time.Clock()
while exit:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      exit = False

    if event.type == CHANGE_COLOR:
      if bg_active_color == new_color:
        screen.fill(new_color)
        bg_active_color = surf_color
    elif bg_active_color == surf_color:
        screen.fill(surf_color)
        bg_active_color = new_color
    if event.type == color1:
      if sprite_active_color == new_sprite_color:
        sp1.image.fill(new_sprite_color)
        sp2.image.fill(new_sprite_color)
        sprite_active_color = color
      elif sprite_active_color == color:
        sp1.image.fill(color)
        sp2.image.fill(color)
        sprite_active_color = new_sprite_color

    all_sprites_list.update()
    all_sprites_list.draw(screen)
    pygame.display.update()
  clock.tick(30)

pygame.quit()