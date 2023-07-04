from pynput.mouse import Listener as MouseListener
from pynput.keyboard import Listener as KeyboardListener, Key
import time
import json

time.sleep(1)

# 클릭 위치를 저장할 리스트
click_positions = []

def on_click(x, y, button, pressed):
    if pressed:
        # 마우스 클릭 위치를 리스트에 추가
        click_positions.append((x, y))
        print(f'Mouse clicked at ({x}, {y})')

def on_press(key):
    # 'q' 키를 누르면 종료
    if key == Key.esc or key.char == 'q':
        return False

# 마우스 리스너 시작
mouse_listener = MouseListener(on_click=on_click)
mouse_listener.start()

# 키보드 리스너 시작
with KeyboardListener(on_press=on_press) as keyboard_listener:
    keyboard_listener.join()

# 마우스 리스너 종료
mouse_listener.stop()

print(click_positions)


# JSON 파일로 클릭 위치 저장
with open('click_positions_memory_profile.json', 'w') as file:
    json.dump(click_positions, file)

print('Click positions have been saved to "click_positions.json".')