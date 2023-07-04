import json
import pyautogui
import time

time.sleep(2)

# JSON 파일로부터 클릭 위치 불러오기
with open('click_positions_dungeon.json', 'r') as file:
    click_positions = json.load(file)

# JSON 파일로부터 프로파일 위치 불러오기
with open('click_positions_memory_profile.json', 'r') as file:
    click_position_memory_profie = json.load(file)

# 스크린샷 캡처
screenshot = pyautogui.screenshot()

# 유니티 프로파일 캡쳐
memory_profile_capture_pos = click_position_memory_profie[0]

# 마우스를 해당 위치로 이동합니다.
pyautogui.moveTo(memory_profile_capture_pos[0], memory_profile_capture_pos[1])

# 클릭 이벤트를 발생시킵니다.
pyautogui.click()

# 스크린샷 저장
screenshot.save('click_positions_dungeon_start.png')

# 각 클릭 위치를 순회
for _ in range(500):
    for position in click_positions:
        # 마우스를 해당 위치로 이동
        pyautogui.moveTo(position[0], position[1])
        # 클릭 이벤트 발생
        pyautogui.click()
        # 2초 대기
        time.sleep(3)


# 스크린샷 캡처
screenshot = pyautogui.screenshot()

# 스크린샷 저장
screenshot.save('click_positions_dungeon_end.png')