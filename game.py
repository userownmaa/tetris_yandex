import random
import sys

import pygame

from active_block import ActiveBlock
from bottom import Bottom
from constant import Constant
from field import Field
from image import Image
from next_block import NextBLock


class Game:

    blocks = ["O", "T", "L", "I", "Z", "Z_rev", "L_rev"]

    def __init__(self):
        self.all_sprites = pygame.sprite.Group()
        self.active_block_group = pygame.sprite.Group()
        self.next_block_group = pygame.sprite.Group()
        self.bottom_group = pygame.sprite.Group()
        self.score = 0
        self.level = 1
        self.game = True
        self.field = Field()
        self.block = ActiveBlock(random.choice(self.blocks), random.randint(1, 6), self.all_sprites, self.active_block_group)
        self.next_color = random.randint(1, 6)
        self.next_block_type = random.choice(self.blocks)
        self.next_block = NextBLock(self.next_block_type, self.next_color, self.all_sprites, self.next_block_group)
        self.game_speed = 700
        self.GAME_UPDATE = pygame.USEREVENT
        pygame.time.set_timer(self.GAME_UPDATE, self.game_speed)

    def start_screen(self, screen, clock):
        intro_text = []

        fon = pygame.transform.scale(Image.load_image(""), (Constant.WIDTH, Constant.HEIGHT))
        screen.blit(fon, (0, 0))
        font = pygame.font.Font(None, 30)
        text_coord = 50
        for line in intro_text:
            string_rendered = font.render(line, 1, Constant.BLACK)
            intro_rect = string_rendered.get_rect()
            text_coord += 10
            intro_rect.top = text_coord
            intro_rect.x = 10
            text_coord += intro_rect.height
            screen.blit(string_rendered, intro_rect)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.terminate()
                elif event.type == pygame.KEYDOWN or \
                        event.type == pygame.MOUSEBUTTONDOWN:
                    return
            pygame.display.flip()
            clock.tick(Constant.FPS)

    def run_game(self, screen):

        while True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False
                if event.type == pygame.USEREVENT:
                    self.block.move_down(self.active_block_group)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.block.move_side("L", self.active_block_group)
                    if event.key == pygame.K_RIGHT:
                        self.block.move_side("R", self.active_block_group)
                    if event.key == pygame.K_UP:
                        self.block.rotate(self.active_block_group)
                    if event.key == pygame.K_SPACE:
                        self.block.drop(self.active_block_group, self.bottom_group)

            self.field.draw_field(screen)
            self.field.draw_frame(screen, self.next_block_type)

            font = pygame.font.Font(None, 22)
            text = font.render("Следующая фигура:", True, Constant.WHITE)
            screen.blit(text, (20, 160))
            text = font.render("Уровень:", True, Constant.WHITE)
            screen.blit(text, (440, 140))
            text = font.render("Счёт:", True, Constant.WHITE)
            screen.blit(text, (440, 280))

            font = pygame.font.Font(None, 35)
            text = font.render(str(self.level), True, Constant.WHITE)
            screen.blit(text, (450, 170))
            text = font.render(str(self.score), True, Constant.WHITE)
            screen.blit(text, (450, 310))

            if not self.active_block_group:
                self.block = ActiveBlock(self.next_block_type, self.next_color, self.all_sprites,
                                         self.active_block_group)
                self.next_block_type = random.choice(self.blocks)
                self.next_color = random.randint(1, 6)
                self.next_block = NextBLock(self.next_block_type, self.next_color, self.all_sprites,
                                            self.next_block_group)
            if self.block.is_at_bottom(self.active_block_group, self.bottom_group):
                self.block.move_up(self.active_block_group)
                self.block.stop(self.active_block_group, self.bottom_group)
                self.next_block.close(self.next_block_group)
            if self.block.is_out_of_border(self.active_block_group) == "R":
                self.block.move_side("L", self.active_block_group)
            elif self.block.is_out_of_border(self.active_block_group) == "L":
                self.block.move_side("R", self.active_block_group)
            if self.field.is_row_completed(self.bottom_group):
                self.field.clear_row(self.bottom_group)
                self.score += self.field.get_score()
                # print(self.score, "*****", self.level, "*****", self.game_speed)
                if self.score % 10 == 0:
                    self.level += 1
                    self.game_speed -= 100
            if self.block.is_over(self.active_block_group, self.bottom_group):
                return False

            self.all_sprites.draw(screen)

            return True

    def terminate(self):
        pygame.quit()
        sys.exit()
