import requests
import time

ipp = 91
def tyre(center, dectcentx, dectcenty,rectangle_xy):
    # global last_x
    X = center[0]
    Y = center[1]
    # X=240
    # print("X:{},Y:{}".format(X,Y))
    loss_x = X-dectcentx
    loss_y = Y-dectcenty


    print('{},{}'.format(loss_x, loss_y))


    if loss_x > int(rectangle_xy[0])//4:

        r = requests.get(f'http://192.168.31.{ipp}/y')
        # time.sleep(0.020)
        print("左转")

        if loss_y > int(rectangle_xy[1])//4:
            r = requests.get(f'http://192.168.31.{ipp}/f')
            print("前进")

        elif loss_y < -(rectangle_xy[1])//4:
            r = requests.get(f'http://192.168.31.{ipp}/b')
            print('后退')
        else:
            r = requests.get(f'http://192.168.31.{ipp}/s')
            print("停止")
    elif loss_x < -(rectangle_xy[0])//4:
        r = requests.get(f'http://192.168.31.{ipp}/z')
        # time.sleep(0.020)
        print('右转')
        if loss_y > (rectangle_xy[1])//4:
            r = requests.get(f'http://192.168.31.{ipp}/f')
            print('前进')
        elif loss_y < -(rectangle_xy[1])//4:
            r = requests.get(f'http://192.168.31.{ipp}/b')
            print('后退')
        else:
            r = requests.get(f'http://192.168.31.{ipp}/s')
            print('停止')

    else:
        r = requests.get(f'http://192.168.31.{ipp}/s')
        print('停止')
        if loss_y > (rectangle_xy[1])//4:
            r = requests.get(f'http://192.168.31.{ipp}/f')
            print("前进")
        elif loss_y < -(rectangle_xy[1])//4:
            r = requests.get(f'http://192.168.31.{ipp}/b')
            print("后退")
        else:
            r = requests.get(f'http://192.168.31.{ipp}/s')
            print("停止")


def errortyre():#失去目标
    # r = requests.get('http://192.168.31.123/z')
    r=requests.get(f'http://192.168.31.{ipp}/s')
    # print('停止')
    # r=requests.get("http://192.168.31.123/y")
    #print("右转")
    # r=requests.get('http://192.168.31.123/s')
    #print(停止)
    # time.sleep(1)

# if __name__ == '__main__':
#     r = requests.get('http://192.168.31.110/f')
#     with open('质点.txt') as f: #读取质点文本内容
#         contents = f.read()
#         f.close()
#     t=tyre(float(contents))
