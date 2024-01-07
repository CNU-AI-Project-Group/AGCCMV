import requests
import time

# 创建一个 Session 对象，以减少网络请求
session = requests.Session()


def tyre(center, dectcenterx, dectcentery, rectangle_xy,ipp):
    # rectangle_xy 最近目标的窗宽与窗高
    loss_x = center[0] - dectcenterx
    loss_y = center[1] - dectcentery
    rww = rectangle_xy[0]
    rwh = rectangle_xy[1]
    print(f'{loss_x},{rww//2}')

    # 定义每个请求的 URL，减少代码重复
    urls = {
        'left': f'http://192.168.31.{ipp}/y',
        'right': f'http://192.168.31.{ipp}/z',
        'forward': f'http://192.168.31.{ipp}/f',
        'backward': f'http://192.168.31.{ipp}/b',
        'stop': f'http://192.168.31.{ipp}/s',
    }
    # r = session.get(urls['left'])
    if abs(loss_x) > int(rww // 2) and loss_x > 0:
        print("left")
        # r = session.get(urls['left'])
    elif abs(loss_x) > int(rww // 2) and loss_x < 0:
        print("right")
        # r = session.get(urls['right'])
    else:
        if rww < 600:
            print("forward")
            # r = session.get(f'http://192.168.31.{ipp}/f')
        elif rww > 650:
            print("backward")
            # r = session.get(f'http://192.168.31.{ipp}/b')
        else:
            print("stop")
            # r = session.get(f'http://192.168.31.{ipp}/s')
        # time.sleep(0.02)
