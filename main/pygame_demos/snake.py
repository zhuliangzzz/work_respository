import pygame
import sys
import random
import time

# 初始化 Pygame
pygame.init()

# 游戏参数
WIDTH, HEIGHT = 600, 600
GRID_SIZE = 20
GRID_WIDTH = WIDTH // GRID_SIZE
GRID_HEIGHT = HEIGHT // GRID_SIZE
FPS = 10

# 颜色定义
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (50, 205, 50)
RED = (255, 0, 0)
BLUE = (30, 144, 255)
GRAY = (40, 40, 40)

# 方向常量
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)


class Snake:
    def __init__(self):
        self.reset()

    def reset(self):
        self.length = 3
        self.positions = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.score = 0
        self.grow_to = 3
        self.color = GREEN

    def get_head_position(self):
        return self.positions[0]

    def turn(self, point):
        if self.length > 1 and (point[0] * -1, point[1] * -1) == self.direction:
            return
        else:
            self.direction = point

    def move(self):
        head = self.get_head_position()
        x, y = self.direction
        new_x = (head[0] + x) % GRID_WIDTH
        new_y = (head[1] + y) % GRID_HEIGHT
        new_position = (new_x, new_y)

        if new_position in self.positions[1:]:
            return False  # 游戏结束

        self.positions.insert(0, new_position)

        if len(self.positions) > self.grow_to:
            self.positions.pop()

        return True

    def draw(self, surface):
        for i, p in enumerate(self.positions):
            # 蛇头用不同颜色
            color = BLUE if i == 0 else self.color

            rect = pygame.Rect((p[0] * GRID_SIZE, p[1] * GRID_SIZE), (GRID_SIZE, GRID_SIZE))
            pygame.draw.rect(surface, color, rect)
            pygame.draw.rect(surface, BLACK, rect, 1)

            # 绘制蛇的眼睛
            if i == 0:
                eye_size = GRID_SIZE // 5
                # 根据方向调整眼睛位置
                if self.direction == RIGHT:
                    pygame.draw.circle(surface, BLACK,
                                       (p[0] * GRID_SIZE + GRID_SIZE - eye_size, p[1] * GRID_SIZE + eye_size * 2),
                                       eye_size)
                    pygame.draw.circle(surface, BLACK, (
                    p[0] * GRID_SIZE + GRID_SIZE - eye_size, p[1] * GRID_SIZE + GRID_SIZE - eye_size * 2), eye_size)
                elif self.direction == LEFT:
                    pygame.draw.circle(surface, BLACK, (p[0] * GRID_SIZE + eye_size, p[1] * GRID_SIZE + eye_size * 2),
                                       eye_size)
                    pygame.draw.circle(surface, BLACK,
                                       (p[0] * GRID_SIZE + eye_size, p[1] * GRID_SIZE + GRID_SIZE - eye_size * 2),
                                       eye_size)
                elif self.direction == UP:
                    pygame.draw.circle(surface, BLACK, (p[0] * GRID_SIZE + eye_size * 2, p[1] * GRID_SIZE + eye_size),
                                       eye_size)
                    pygame.draw.circle(surface, BLACK,
                                       (p[0] * GRID_SIZE + GRID_SIZE - eye_size * 2, p[1] * GRID_SIZE + eye_size),
                                       eye_size)
                elif self.direction == DOWN:
                    pygame.draw.circle(surface, BLACK,
                                       (p[0] * GRID_SIZE + eye_size * 2, p[1] * GRID_SIZE + GRID_SIZE - eye_size),
                                       eye_size)
                    pygame.draw.circle(surface, BLACK, (
                    p[0] * GRID_SIZE + GRID_SIZE - eye_size * 2, p[1] * GRID_SIZE + GRID_SIZE - eye_size), eye_size)


class Food:
    def __init__(self):
        self.position = (0, 0)
        self.color = RED
        self.randomize_position()

    def randomize_position(self):
        self.position = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))

    def draw(self, surface):
        rect = pygame.Rect((self.position[0] * GRID_SIZE, self.position[1] * GRID_SIZE), (GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(surface, self.color, rect)
        pygame.draw.rect(surface, BLACK, rect, 1)

        # 绘制食物内部细节
        inner_rect = pygame.Rect(
            (self.position[0] * GRID_SIZE + GRID_SIZE // 4, self.position[1] * GRID_SIZE + GRID_SIZE // 4),
            (GRID_SIZE // 2, GRID_SIZE // 2)
        )
        pygame.draw.rect(surface, (255, 200, 200), inner_rect)


def draw_grid(surface):
    for y in range(0, HEIGHT, GRID_SIZE):
        for x in range(0, WIDTH, GRID_SIZE):
            rect = pygame.Rect((x, y), (GRID_SIZE, GRID_SIZE))
            pygame.draw.rect(surface, GRAY, rect, 1)


def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('贪吃蛇游戏')
    clock = pygame.time.Clock()

    font = pygame.font.SysFont('microsoftyahei', 20)
    big_font = pygame.font.SysFont('microsoftyahei', 50)

    snake = Snake()
    food = Food()

    game_over = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if game_over:
                    if event.key == pygame.K_SPACE:
                        snake.reset()
                        food.randomize_position()
                        game_over = False
                else:
                    if event.key == pygame.K_UP:
                        snake.turn(UP)
                    elif event.key == pygame.K_DOWN:
                        snake.turn(DOWN)
                    elif event.key == pygame.K_LEFT:
                        snake.turn(LEFT)
                    elif event.key == pygame.K_RIGHT:
                        snake.turn(RIGHT)

        if not game_over:
            # 移动蛇
            if not snake.move():
                game_over = True

            # 检查是否吃到食物
            if snake.get_head_position() == food.position:
                snake.grow_to += 1
                snake.score += 10
                food.randomize_position()
                # 确保食物不出现在蛇身上
                while food.position in snake.positions:
                    food.randomize_position()

        screen.fill(BLACK)
        draw_grid(screen)
        snake.draw(screen)
        food.draw(screen)

        # 显示分数
        score_text = font.render(f'分数: {snake.score}', True, WHITE)
        screen.blit(score_text, (5, 5))

        # 显示长度
        length_text = font.render(f'长度: {snake.grow_to}', True, WHITE)
        screen.blit(length_text, (5, 30))

        if game_over:
            game_over_text = big_font.render('游戏结束!', True, RED)
            restart_text = font.render('按空格键重新开始', True, WHITE)
            screen.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 2 - 50))
            screen.blit(restart_text, (WIDTH // 2 - restart_text.get_width() // 2, HEIGHT // 2 + 20))

        pygame.display.update()
        clock.tick(FPS)


if __name__ == "__main__":
    main()