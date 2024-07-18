import sys
import pygame
import math
import random

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
spell_color_players1 = [(64, 0, 0), (127, 0, 0), (255, 0, 0)]
spell_color_players2 = [(0, 0, 64), (0, 0, 127), (0, 0, 255)]


main_menu_font=pygame.font.Font(None, 36)
text_color = (255, 255, 255)
hover_color = (200, 200, 200)
centerx= 100
centery= 100
length = 10
spell_speed = 6
spells = []
spell_delay = 100
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


def cast_spell(from_pos, to_pos, spell_color, player_num):
    angle = math.atan2(to_pos[1] - from_pos[1], to_pos[0] - from_pos[0])
    velocity = (spell_speed * math.cos(angle), spell_speed * math.sin(angle))
    spells.append({'pos': list(from_pos), 'velocity': velocity, 'distance': 0,
                   'spell_color': spell_color, 'player_num' : player_num})

def update_spells(circle_pos, circle_radius, player_spells):
    for spell in player_spells:
        old_pos = spell['pos'].copy()
        spell['pos'][0] += spell['velocity'][0]
        spell['pos'][1] += spell['velocity'][1]
        spell['distance'] += spell_speed

         # Перевірка перетину з колом
        if line_circle_intersection(old_pos, spell['pos'], circle_pos, circle_radius):
            print("Промінь перетнув коло!")
            spells.remove(spell)
        else:
            pygame.draw.line(screen, spell['spell_color'], old_pos, spell['pos'], 5)


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

def line_circle_intersection(line_start, line_end, circle_center, circle_radius):
    dx = line_end[0] - line_start[0]
    dy = line_end[1] - line_start[1]
    fx = line_start[0] - circle_center[0]
    fy = line_start[1] - circle_center[1]

    a = dx * dx + dy * dy
    b = 2 * (fx * dx + fy * dy)
    c = (fx * fx + fy * fy) - circle_radius * circle_radius

    discriminant = b * b - 4 * a * c
    if discriminant < 0:
        return False

    t1 = (-b + math.sqrt(discriminant)) / (2 * a)
    t2 = (-b - math.sqrt(discriminant)) / (2 * a)

    if 0 <= t1 <= 1 or 0 <= t2 <= 1:
        return True

    return False

def game():
    global spells
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
    can_cast_player1 = True
    can_cast_player2 = True




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



        #стостується першого гравця
        if keys[pygame.K_s] and can_cast_player1:
            cast_spell([ball_x1, ball_y1], [ball_x2, ball_y2],
                       spell_color = random.choice(spell_color_players1), player_num=1)
            can_cast_player1 = False
        #стосується другого гравця
        if keys[pygame.K_DOWN] and can_cast_player2:
            cast_spell([ball_x2, ball_y2], [ball_x1, ball_y1],
                       spell_color = random.choice(spell_color_players2), player_num=2)
            can_cast_player2 = False
        # перевірка чи може луч запускати
        spells_player1 = [spell for spell in spells if spell['player_num'] == 1]
        spells_player2 = [spell for spell in spells if spell['player_num'] == 2]
        if spells_player1 and spells_player1[-1]['distance'] >= spell_delay:
            can_cast_player1 = True

        if spells_player2 and spells_player2[-1]['distance'] >= spell_delay:
            can_cast_player2 = True
        # Видаляємо лучі які вийшли за межі екрана
        spells = [spell for spell in spells if
                  0 <= spell['pos'][0] <= screen_size[0] and 0 <= spell['pos'][1] <= screen_size[1]]

        screen.fill((0, 0, 0))

        pygame.draw.rect(screen, color_sky, (sky_x, sky_y, width_sky, height_sky))
        pygame.draw.rect(screen, color_grass, (grass_x, grass_y, width_grass, height_grass))
        pygame.draw.circle(screen, color1, (ball_x1, ball_y1), ball_radius)
        pygame.draw.circle(screen, color2, (ball_x2, ball_y2), ball_radius)
        update_spells([ball_x2, ball_y2], ball_radius, spells_player1)
        update_spells([ball_x1, ball_y1], ball_radius, spells_player2)
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
