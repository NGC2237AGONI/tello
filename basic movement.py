from djitellopy import tello
from time import sleep
#调用这些库
me = tello.Tello()
me.connect()#连接名为me的无人机
print(me.get_battery())#显示无人机剩余电量
#这里基本上每次都是这样
me.takeoff()#无人机起飞
me.send_rc_control(0,50,0,0)
#这个函数赋予无人机各个方向上的速度（左右，前后，上下，旋转）
sleep(2)
#持续时间
me.send_rc_control(50,0,0,0)
sleep(2)
me.send_rc_control(0,0,-30,0)
sleep(2)
me.send_rc_control(0,0,0,50)
sleep(2)
me.send_rc_control(0,0,0,0)
me.land()