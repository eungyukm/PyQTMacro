import pyautogui
import os
from PIL import Image
import time

# 현재 마우스 위치 얻기
while(True):
    current_mouse_position = pyautogui.position()

    print(current_mouse_position)

print(os.getcwd())

# 파일의 절대 경로 출력
print(os.path.abspath("your_file_name_here"))

# 이미지 파일 열기
# img = Image.open('./sealM/dungeon_icon.png')

# 이미지 파일을 화면에 표시
# img.show()

time.sleep(1)
# 이동하려는 지점의 이미지를 찾습니다.
location = pyautogui.locateOnScreen('./sealM/dungeon_icon.png', confidence=0.5)

# 이미지의 위치를 찾았다면,
if location:
    # 해당 위치로 마우스를 이동합니다.
    pyautogui.moveTo(location)
    # 클릭 이벤트 전송
    pyautogui.click()
else:
    print('위치 찾지 못함')

# 이동하려는 지점의 이미지를 찾습니다.
location = pyautogui.locateOnScreen('./sealM/back_icon.png', confidence=0.65)

time.sleep(1)

# 이미지의 위치를 찾았다면,
if location:
    # 해당 위치로 마우스를 이동합니다.
    pyautogui.moveTo(location)
    # 클릭 이벤트 전송
    pyautogui.click()
else:
    print('위치 찾지 못함')


