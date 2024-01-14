import random
import sys

import pygame

from active_block import ActiveBlock
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
        self.block = ActiveBlock(random.choice(self.blocks), random.randint(1, 6), self.all_sprites, self.active_block_group)
        self.next_color = random.randint(1, 6)
        self.next_block_type = random.choice(self.blocks)
        self.next_block = NextBLock(self.next_block_type, self.next_color, self.all_sprites, self.next_block_group)

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
            field = Field()
            field.draw_field(screen)
            if not self.active_block_group:
                self.block = ActiveBlock(self.next_block_type, self.next_color, self.all_sprites,
                                         self.active_block_group)
                self.next_block_type = random.choice(self.blocks)
                self.next_color = random.randint(1, 6)
                self.next_block = NextBLock(self.next_block_type, self.next_color, self.all_sprites,
                                            self.next_block_group)
            if self.block.is_at_bottom(self.active_block_group, self.bottom_group):
                self.block.stop(self.active_block_group, self.bottom_group)
            else:
                self.block.fall(self.active_block_group)

            self.all_sprites.draw(screen)
            return True

    def terminate(self):
        pygame.quit()
        sys.exit()
