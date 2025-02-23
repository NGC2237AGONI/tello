from djitellopy import tello
import KeyPressModule as kp
from time import sleep
kp.init()
me = tello.Tello()
me.connect()
print(me.get_battery())
#import KeyPressModule as kp 导入了相应的模块

def getKeybordInput():#定义键盘位置对应的无人机控制效果
    lr,fb,ud,yv=0,0,0,0#初始化四个方向速度为0（左右，前后，上下，旋转）
    speed=50#单位是cm/s，在旋转那就是度
    if kp.getKey("LEFT"):lr=speed
    elif kp.getKey("RIGHT"): lr = -speed

    if kp.getKey("UP"):fb = speed
    elif kp.getKey("DOWN"): fb = -speed

    if kp.getKey("w"):ud = speed
    elif kp.getKey("s"): ud = -speed

    if kp.getKey("a"):yv = 2*speed
    elif kp.getKey("d"): yv = -2*speed
    #定义了不同方向的速度和对应的控制按键
    if kp.getKey("q"): me.land()
    if kp.getKey("e"): me.takeoff()
    #定义起飞和着陆的按键
    return [lr,fb,ud,yv]

while True:
    vals = getKeybordInput()
    me.send_rc_control(vals[0],vals[1],vals[2],vals[3])
    sleep(0.05)#给出持续时间
    #依据按的情况实时返回各个方向的速度