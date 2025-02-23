from djitellopy import tello
import cv2

me = tello.Tello()
me.connect()
print(me.get_battery())

me.streamon()#启用无人机的视频流

while True:#持续进行
    img = me.get_frame_read().frame#从无人机视频流或摄像头中获取当前帧（图像）
    img = cv2.resize(img,(360,240))#使用 OpenCV 库对图像进行缩放的代码，数字调节大小
    cv2.imshow("Image", img)#弹出一个名为“Image”的窗口显示之前获取的图像
    cv2.waitKey(1)#控制每帧之间的延迟，从而控制视频播放的帧率（1ms）
