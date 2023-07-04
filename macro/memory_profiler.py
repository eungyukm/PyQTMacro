import pyautogui
import schedule
import time
from datetime import datetime

def take_screenshot():
    img = pyautogui.screenshot()
    img.save(f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.png")

def click_mouse():
    pyautogui.click(334, 1182)  # 좌표 수정 가능

# 일정 스케줄 설정
schedule.every(20).minutes.do(click_mouse)
schedule.every(1).minutes.do(take_screenshot)

while True:
    schedule.run_pending()
    time.sleep(1)  # 코드 실행 간격 설정
