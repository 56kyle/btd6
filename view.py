import win32gui as gui
import win32api as api
import pyautogui


class View:
    def __init__(self):
        self.win = gui.GetForegroundWindow()
        self.dc = gui.GetDC(self.win)

    def get_pixel(self, x, y):
        return gui.GetPixel(self.dc, x, y)

    def get_pixels(self, pixels):
        results = []
        for pixel in pixels:
            results.append(self.get_pixel(pixel[0], pixel[1]))

    def __del__(self):
        gui.DeleteDC(self.dc)

