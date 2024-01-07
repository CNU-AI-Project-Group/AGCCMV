# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 12:14:29 2020

@author: analoganddigital   ( GitHub )
"""
import cv2
import numpy as np
import win32gui, win32ui, win32con, win32api


def grab_screen(region=None):
    """
      获取Windows系统屏幕上指定区域的截图

      :param region: 指定的区域，如果没有指定，则默认为整个屏幕
      :return: 返回截图的Numpy数组，数组的形状为(height, width, 4)
      """

    # 获取桌面窗口的句柄
    hwin = win32gui.GetDesktopWindow()

    # 如果指定了区域，则计算出区域的宽度和高度
    if region:
        left, top, x2, y2 = region
        width = x2 - left + 1
        height = y2 - top + 1
    # 如果没有指定区域，则获取整个屏幕的宽度和高度
    else:
        width = win32api.GetSystemMetrics(win32con.SM_CXVIRTUALSCREEN)
        height = win32api.GetSystemMetrics(win32con.SM_CYVIRTUALSCREEN)
        left = win32api.GetSystemMetrics(win32con.SM_XVIRTUALSCREEN)
        top = win32api.GetSystemMetrics(win32con.SM_YVIRTUALSCREEN)

    # 获取窗口的设备上下文句柄
    hwindc = win32gui.GetWindowDC(hwin)
    # 创建一个源设备上下文，将其与窗口的设备上下文相关联
    srcdc = win32ui.CreateDCFromHandle(hwindc)
    # 创建一个兼容的设备上下文，用于在内存中创建位图
    memdc = srcdc.CreateCompatibleDC()
    # 创建一个位图对象，并将其与兼容的设备上下文相关联
    bmp = win32ui.CreateBitmap()

    bmp.CreateCompatibleBitmap(srcdc, width, height)

    memdc.SelectObject(bmp)
    # 使用位块传输操作将屏幕上的位图复制到内存中的位图中
    memdc.BitBlt((0, 0), (width, height), srcdc, (left, top), win32con.SRCCOPY)

    # 从位图对象中获取位图的位信息
    signedIntsArray = bmp.GetBitmapBits(True)
    # 将位信息转换成Numpy数组
    img = np.fromstring(signedIntsArray, dtype='uint8')
    # 重塑数组的形状，使其变成一个(height, width, 4)的数组
    img.shape = (height, width, 4)
    # 释放相关资源
    srcdc.DeleteDC()
    memdc.DeleteDC()
    win32gui.ReleaseDC(hwin, hwindc)
    win32gui.DeleteObject(bmp.GetHandle())
    # 返回截图的Numpy数组
    return img
