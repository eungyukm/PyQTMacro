import json
import pyautogui
import time
import os

time.sleep(2)

# JSON 파일로부터 프로파일 위치 불러오기
with open('click_positions_memory_profile.json', 'r') as file:
    click_position_memory_profie = json.load(file)

# 유니티 프로파일 캡처
memory_profile_capture_pos = click_position_memory_profie[0]

# 마우스를 해당 위치로 이동합니다.
pyautogui.moveTo(memory_profile_capture_pos[0], memory_profile_capture_pos[1])

# 클릭 이벤트를 발생시킵니다.
pyautogui.click()

# 'click_positions'라는 폴더 내에 있는 모든 파일을 가져옵니다.
files = os.listdir('click_positions')

# 모든 파일에 대해
for file in files:
    # 파일 이름으로부터 절대 경로를 만듭니다.
    file_path = os.path.join('click_positions', file)

    # JSON 파일로부터 클릭 위치를 불러옵니다.
    with open(file_path, 'r') as f:
        click_positions = json.load(f)

    # 스크린샷 캡처
    screenshot = pyautogui.screenshot()

    # 파일명과 확장자를 분리
    filename, _ = os.path.splitext(file)

    # 스크린샷 저장
    screenshot.save(f'{filename}_start.png')

    # 각 클릭 위치를 순회
    for _ in range(100):
        for position in click_positions:
            # 마우스를 해당 위치로 이동
            pyautogui.moveTo(position[0], position[1])
            # 클릭 이벤트 발생
            pyautogui.click()
            # 5초 대기
            time.sleep(5)

    # 스크린샷 캡처
    screenshot = pyautogui.screenshot()

    # 스크린샷 저장
    screenshot.save(f'{filename}_end.png')

    time.sleep(3)

    # 유니티 프로파일 캡처
    memory_profile_capture_pos = click_position_memory_profie[0]

    # 마우스를 해당 위치로 이동합니다.
    pyautogui.moveTo(memory_profile_capture_pos[0], memory_profile_capture_pos[1])

    # 클릭 이벤트를 발생시킵니다.
    pyautogui.click()

    time.sleep(15)
