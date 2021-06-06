# 《外星人入侵》

# 导入sys模块用于游戏退出
import sys

# 导入pygame模块，该模块包含游戏所有功能
import pygame

# 创建游戏运行函数run_game()


def run_game():
    # 初始化游戏并创建屏幕对象
    pygame.init()
    """1、创建sereen对象，该对象在pygame中为一个syrface
       2、surface是屏幕的一部分，用于显示游戏元素
       3、display.set_mode()返回的surface表示整个游戏窗口
       我们激活游戏的动画循环后，每经过一次循环都将自动重绘这个surface"""
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Alien Incasion")

    # 游戏主循环
    while True:
        # py.game.event.get()检测所用事件，当检测到的事件类型为pygame.QUIT时，通过sys,exit()退出
        for enent in pygame.event.get():
            if enent.type == pygame.QUIT:
                sys.exit()
        # 让最近绘制的屏幕可见
        """每次执行while循环时都绘制一个空屏幕，
        并擦去旧屏幕，使得只有新屏幕可见。
        在我们移动游戏元素时，pygame.display.flip()将不断更新屏幕，
        以显示元素的新位置，并在原来的位置隐藏元素， 从而营造平滑移动的效果。"""
        pygame.display.flip()


# 运行游戏
run_game()
