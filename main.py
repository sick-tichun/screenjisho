#import pyautogui
from torch.nn.functional import pad
import win32gui, win32ui, win32con, win32api
from pynput import keyboard
import easyocr
import ocr



#yo thanks  Amessihel stakcopverflow.com my gs would have to actually program something for myself if it wasnt for reddit chungus
def saveScreenShot(x,y,width,height,path):
    # grab a handle to the main desktop window
    hdesktop = win32gui.GetDesktopWindow()

    # create a device context
    desktop_dc = win32gui.GetWindowDC(hdesktop)
    img_dc = win32ui.CreateDCFromHandle(desktop_dc)

    # create a memory based device context
    mem_dc = img_dc.CreateCompatibleDC()

    # create a bitmap object
    screenshot = win32ui.CreateBitmap()
    screenshot.CreateCompatibleBitmap(img_dc, width, height)
    mem_dc.SelectObject(screenshot)


    # copy the screen into our memory device context
    mem_dc.BitBlt((0, 0), (width, height), img_dc, (x, y),win32con.SRCCOPY)

    # save the bitmap to a file
    screenshot.SaveBitmapFile(mem_dc, path)
    # free our objects
    mem_dc.DeleteDC()
    win32gui.DeleteObject(screenshot.GetHandle())




#MODE IDEA SCRAPPED SOLVED PROBLEM WITH CSGO
#mode = input('mode "0": keybind to capture screen (use when possible cuz its better) \n mode "1": captures to the right of the mouse by some pixels every 1.5s (usefull for games with raw input ich thing refuses to work)' )
#if mode == '0':
#print('using mode 0')


#listenning to keyboard inputs 
print('ready')
current = set()
COMBINATIONS = [
    {keyboard.Key.f7}
    #{keyboard.Key.shift, keyboard.KeyCode(char='a')},
    #{keyboard.Key.shift, keyboard.KeyCode(char='A')}
]

 #varibles for gathering mousepos  
mpos1 = [0,0]
mpos2 = [0,0]
#needed so that press function wont update mpos1's coords after initial press
switch = True
def press(key):
    global mpos1, mpos2, switch 
    if any([key in COMBO for COMBO in COMBINATIONS]):
        current.add(key)
        if any(all(k in current for k in COMBO) for COMBO in COMBINATIONS):
            if switch == True:
                mpos1 = win32gui.GetCursorPos()
                switch = False



def relese(key):
    global mpos1, mpos2, switch
    if any([key in COMBO for COMBO in COMBINATIONS]):
        mpos2 = win32api.GetCursorPos()
        finalcoord = [0, 0]
        for i in range(0,2):
            if mpos1[i] < mpos2[i]:
                finalcoord[i] = mpos1[i]
            else:
                finalcoord[i] = mpos2[i]
        extentions = [abs(mpos1[0]-mpos2[0]), abs(mpos1[1]-mpos2[1])]
        padding = 2
        saveScreenShot(finalcoord[0] - padding , finalcoord[1] - padding, extentions[0] + padding, extentions[1] + padding, 'temp.png')
        current.remove(key)
        ocr.read('piss.png')
        switch = True

with keyboard.Listener(on_press=press, on_release=relese) as listener:
    listener.join()
