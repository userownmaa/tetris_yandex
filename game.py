import random
import sys

import pygame

from active_block import ActiveBlock
from constant import Constant
from database import Database
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
        self.image = Image()
        self.db = Database()
        pygame.time.set_timer(self.GAME_UPDATE, self.game_speed)

    def start_screen(self, screen, clock):

        fon = pygame.transform.scale(self.image.load_image("fon_start.jpg"), (Constant.WIDTH, Constant.HEIGHT))
        screen.blit(fon, (0, 0))

        pygame.draw.rect(screen, Constant.WHITE, (220, 285, 160, 60), 1)

        font = pygame.font.Font(None, 40)
        text = font.render("Играть", True, Constant.WHITE)
        screen.blit(text, (255, 300))

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.terminate()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    if 220 <= mouse_x <= 220 + 160 and 285 <= mouse_y <= 285 + 60:
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

            fon = pygame.transform.scale(self.image.load_image("fon_main.jpg"), (Constant.WIDTH, Constant.HEIGHT))
            screen.blit(fon, (0, 0))
            self.field.draw_field(screen)
            self.field.draw_frame(screen, self.next_block_type)

            font = pygame.font.Font(None, 22)
            text = font.render("Следующая фигура:", True, Constant.WHITE)
            screen.blit(text, (20, 160))
            text = font.render("Уровень:", True, Constant.WHITE)
            screen.blit(text, (440, 140))
            text = font.render("Очки:", True, Constant.WHITE)
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

                for level in range(1, 8):
                    if self.score // 10 == level - 1:
                        self.level = level
                        self.game_speed = abs(level * 100 - 800)

            self.all_sprites.draw(screen)

            if self.field.is_over(self.bottom_group, self.next_block):
                return False

            return True

    def finish_screen(self, screen, clock):
        fon = pygame.transform.scale(self.image.load_image("fon_fin.jpg"), (Constant.WIDTH, Constant.HEIGHT))
        screen.blit(fon, (0, 0))

        pygame.draw.rect(screen, Constant.WHITE, (170, 90, 260, 250), 1)
        self.db.add_result(self.score)
        best_score = self.db.get_result()
        font = pygame.font.Font(None, 30)
        text = font.render("Ваш результат:", True, Constant.WHITE)
        screen.blit(text, (200, 130))
        text = font.render("Лучший результат:", True, Constant.WHITE)
        screen.blit(text, (200, 230))

        font = pygame.font.Font(None, 40)
        text = font.render(f"{self.score}", True, Constant.WHITE)
        screen.blit(text, (200, 160))
        text = font.render(f"{best_score}", True, Constant.WHITE)
        screen.blit(text, (200, 260))

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
            pygame.display.flip()
            clock.tick(Constant.FPS)


    def terminate(self):
        pygame.quit()
        sys.exit()
