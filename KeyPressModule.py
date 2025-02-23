import pygame

def init():
    pygame.init()
    win = pygame.display.set_mode((400, 400))
#创造一个（400,400）的像素窗口
def getKey(keyName):
    ans = False
    #初始时默认没有按键被按下
    for eve in pygame.event.get(): pass
    #只是清空队列，防止事件积压导致不必要的延迟
    keyInput = pygame.key.get_pressed()
    #获取当前键盘的状态，返回一个布尔值列表，每个元素对应一个键的状态（按下为 True，未按下为 False）
    myKey = getattr(pygame, 'K_{}'.format(keyName))
    #使得我们可以传入键名作为字符串，而无需硬编码每个键的常量（比方说LEFT就是键盘上的左键）
    if keyInput[myKey]:
        ans = True
    #如果目标键被按下就为True
    pygame.display.update()
    #更新显示，确保屏幕刷新
    return ans

def main():
    if getKey("LEFT"):
        print('Left key pressed')
    if getKey('RIGHT'):
        print('Right key pressed')
    #试验函数，如果开始后按左键显示了'Left key pressed'，松开后消失即为成功

if __name__ == '__main__':
    init()
    while True:
        main()
    #试验程序