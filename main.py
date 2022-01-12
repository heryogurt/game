import pygame

size = 400, 300
pygame.init()
screen = pygame.display.set_mode(size)


class First_screen:
    screen.fill(pygame.Color("black"))
    pygame.display.set_caption("первый скрин")
    pygame.draw.rect(screen, "purple", (30, 20, 340, 200), 0)
    pygame.draw.rect(screen, "#E3C4F5", (35, 25, 330, 190), 0)
    pygame.draw.rect(screen, "orange", (30, 240, 155, 50), 0)
    pygame.draw.rect(screen, "orange", (214, 240, 155, 50), 0)
    intro_text = ["Описание истории"]
    font = pygame.font.Font(None, 25)
    text_coord = 25
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('black'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 40
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)
    play_text = ["Играть сначала"]
    for line in play_text:
        string_rendered = font.render(line, 1, pygame.Color('black'))
        intro_rect = string_rendered.get_rect()
        text_coord = 255
        intro_rect.top = text_coord
        intro_rect.x = 43
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)


while pygame.event.wait().type != pygame.QUIT:
    pygame.display.update()
pygame.quit()
