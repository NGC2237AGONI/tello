import cv2
from djitellopy import tello
import KeyPressModule as kp
import numpy as np
import math
from time import sleep

############ PARAMETERS ############
fSpeed = 117/10 #Forward Speed in cm/s   (15cm/s)
aSpeed = 360/10 #Angular Speed Degrees/s (50d/s)
interval = 0.25

dInterval = fSpeed*interval
aInterval = aSpeed*interval
####################################
#这是实际测得无人机各个方向的速度
x,y=500,500
a=0
#给出初始横纵坐标值

kp.init()
me = tello.Tello()
me.connect()
print(me.get_battery())

points=[(0,0),(0,0)]
#初始化原点
def getKeybordInput():
    lr,fb,ud,yv=0,0,0,0
    speed=15
    aspeed=50
    global x,y,yaw,a
    d=0

    if kp.getKey("LEFT"):
        lr=speed
        d=dInterval
        a=-180

    elif kp.getKey("RIGHT"):
        lr = -speed
        d = -dInterval
        a = 180

    if kp.getKey("UP"):
        fb = speed
        d = dInterval
        a = 270

    elif kp.getKey("DOWN"):
        fb = -speed
        d = -dInterval
        a = -90

    if kp.getKey("w"):ud = speed
    elif kp.getKey("s"): ud = -speed

    if kp.getKey("a"):
        yv = -2*aspeed
        yaw -= aInterval

    elif kp.getKey("d"):
        yv = 2*aspeed
        yaw += aInterval
#我们控制无人机的同时在地图上进行绘制，这里是将无人机的运动以获取按键被按情况的方式映射到map上的点的运动
    if kp.getKey("q"): me.land()
    if kp.getKey("e"): me.takeoff()

    sleep(interval)
    a += yaw
    x += int(d*math.cos(math.radians(a)))
    y += int(d * math.sin(math.radians(a)))
#d表示当前朝向上想要移动的距离，弧度转换之后通过角度与d计算出x，y方向的距离
    return [lr,fb,ud,yv]

def drawPoints(img,points):
    for point in points:
        cv2.circle(img, point, 5, (0, 0, 255), cv2.FILLED)
        # 在运动点位置生成一个可见红色圆（稍小）
        cv2.circle(img, point[-1], 8, (0, 225, 0), cv2.FILLED)
        # 在运动点位置生成一个可见绿色圆（稍大）
    cv2.putText(img,f'({(points[-1][0]-500)/100},{(points[-1][1]-500)/100})m',
                (points[-1][0]+10,points[-1][1]+30),cv2.FONT_HERSHEY_PLAIN,1,
                (255,0,255),1)
    #在点运动过程中实时记录运动路线（将点的坐标作为文本显示在图像上）


while True:
    vals = getKeybordInput()
    me.send_rc_control(vals[0],vals[1],vals[2],vals[3],x,y)

    img = np.zeros((1000,1000,3),np.uint8)
    #创建一个大小为 1000x1000 像素的黑色图像，并指定图像的数据类型为 np.uint8（每个像素的颜色值范围是 0 到 255）
    if (points[-1][0]!=vals[4] or points[-1][1]!=vals[5]):
        points.append=((vals[4],vals[5]))
    #检查是否需要将一个新的点添加到 points 列表中，并在图像上绘制这些点
    drawPoints(img,points)
    cv2.imshow("Output",img)
    cv2.waitKey(1)