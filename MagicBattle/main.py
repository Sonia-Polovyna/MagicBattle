import sys
import pygame


def empty ():
    return


def exit_game():
    pygame.quit()
    sys.exit()


pygame.init()
screen_size = (640, 480)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("New game")

background_color=(0,0,0)
ball_radius = 15
ball_x1 = 15
ball_y1 = screen_size[1]/1.8
ball_x2 = 625
ball_y2 = screen_size[1]/1.8

main_menu_font=pygame.font.Font(None, 36)
text_color = (255, 255, 255)
hover_color = (200, 200, 200)
centerx= 100
centery= 100


def draw_text(text, font, color, screen, centerx, centery):
    text_test = font.render(text, True, color)
    text_field = text_test.get_rect()
    text_field.centerx = centerx
    text_field.centery = centery
    screen.blit(text_test, text_field)


def main_menu():
    while True:
        mx, my = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for i, button in enumerate(menu_items):
                    if screen_size[1] / 2 + 50 * i - 25 < my < screen_size[1] / 2 + 50 * i + 25:
                        menu_items_map[button]()
        screen.fill(background_color)
        for i, button in enumerate(menu_items):
            if screen_size[1]/2+50*i -25 < my < screen_size[1]/2+50*i +25:
                draw_text(button, main_menu_font, hover_color, screen, screen_size[0]/2, screen_size[1]/2+50*i)
            else:
                draw_text(button, main_menu_font, text_color, screen, screen_size[0]/2, screen_size[1]/2 + 50 * i)
        pygame.display.flip()


def settings():
    while True:
        mx, my = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for i, button in enumerate(settings_items):
                    if 35 + 50*i - 25 < my < 35 + 50*i + 25:
                        settings_items_map[button]()
        screen.fill(background_color)
        for i, button in enumerate(settings_items):
            if 35 + 50*i - 25 < my < 35 + 50*i + 25:
                draw_text(button, main_menu_font, hover_color, screen, screen_size[0] / 2, 35 + 50*i)
            else:
                draw_text(button, main_menu_font, text_color, screen, screen_size[0] / 2, 35 + 50*i)
        pygame.display.flip()


def game():
    running = True
    color1 = (215, 57, 57)
    color_sky = (153, 204, 255)
    color_grass = (102, 204, 102)
    color2 = (51, 51, 204)
    padding = 50
    ball_x1 = padding
    ball_y1 = screen_size[1]/1.8
    ball_x2 = screen_size[0] - padding
    ball_y2 = ball_y1
    movement = 5
    sky_x = 0
    sky_y = 0
    grass_x = 0
    grass_y = screen_size[1]/1.8
    width_grass = screen_size[0]
    height_grass = screen_size[1]/1.8
    width_sky = screen_size[0]
    height_sky = screen_size[1]
    is_jumping1 = False
    is_jumping2 = False
    jump_speed = 20
    gravity = 1
    vertical_speed1 = 0
    vertical_speed2 = 0

    clock = pygame.time.Clock()
    #music = pygame.mixer.Sound("Name of the song")
    #music.play(-1)
    while running:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and not is_jumping1:
                    is_jumping1 = True
                    vertical_speed1 = -jump_speed
                if event.key == pygame.K_UP and not is_jumping2:
                    is_jumping2 = True
                    vertical_speed2 = -jump_speed

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and ball_x1 > 0:
             ball_x1 = ball_x1 - movement
        if keys[pygame.K_d] and ball_x1 > 0:
             ball_x1 = ball_x1 + movement
        if keys[pygame.K_LEFT] and ball_x2 > 0:
             ball_x2 = ball_x2 - movement
        if keys[pygame.K_RIGHT] and ball_x2 > 0:
             ball_x2 = ball_x2 + movement
        if is_jumping1:
            vertical_speed1 += gravity
            ball_y1 += vertical_speed1
            if ball_y1 >= screen_size[1] // 1.8:
                ball_y1 = screen_size[1] // 1.8
                is_jumping1 = False
        if is_jumping2:
            vertical_speed2 += gravity
            ball_y2 += vertical_speed2
            if ball_y2 >= screen_size[1] // 1.8:
                ball_y2 = screen_size[1] // 1.8
                is_jumping2 = False

        screen.fill((0, 0, 0))

        pygame.draw.rect(screen, color_sky, (sky_x, sky_y, width_sky, height_sky))
        pygame.draw.rect(screen, color_grass, (grass_x, grass_y, width_grass, height_grass))
        pygame.draw.circle(screen, color1, (ball_x1, ball_y1), ball_radius)
        pygame.draw.circle(screen, color2, (ball_x2, ball_y2), ball_radius)

        pygame.display.flip()
        clock.tick(60)
    pygame.quit()
    sys.exit()


menu_items = ["Start","Settings","Exit"]
menu_items_map = {
    "Start": game,
    "Settings": settings,
    "Exit": exit_game
}
settings_items = ["Continue","Restart","Sound","Language","Change player name","Change player color","Write a feedback","Return to menu","Quit"]
settings_items_map = {
    "Continue": game,
    "Restart": game,
    "Sound": empty,
    "Language": empty,
    "Change player name": empty,
    "Change player color": empty,
    "Write a feedback": empty,
    "Return to menu": main_menu,
    "Quit": exit_game
}


if __name__ == "__main__":
    main_menu()
