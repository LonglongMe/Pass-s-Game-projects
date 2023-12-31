import pygame

# 初始化Pygame
pygame.init()

# 创建一个800x600的窗口
screen = pygame.display.set_mode((800, 600))

# 创建一个透明矩形
transparent_rect = pygame.Surface((200, 100), pygame.SRCALPHA)
transparent_rect.fill((255, 255, 255, 128))

# 在窗口上绘制矩形
screen.blit(transparent_rect, (300, 200))

# 刷新窗口
pygame.display.flip()

# 游戏主循环
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# 退出Pygame
pygame.quit()
