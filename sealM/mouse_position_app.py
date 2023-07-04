import sys
import pyautogui
import time
import os
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QTimer
from macro_ui import Ui_Dialog
from PyQt5.QtGui import QCursor
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QFileDialog

# 화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.saved_position = None
        self.timer = QTimer(self)
        self.timer_interval = 1000  # 초기 값: 1초
        self.timer.setInterval(self.timer_interval)
        self.timer.timeout.connect(self.click_saved_position)

        self.screenshot_timer = QTimer(self)  # 스크린샷 타이머 초기화
        self.screenshot_timer.timeout.connect(self.take_screenshot)

        # 버튼에 기능을 연결하는 코드
        self.ui.check_mouse_position_button.clicked.connect(self.check_mouse_position)
        self.ui.click_saved_position_button.clicked.connect(self.click_saved_position)
        self.ui.check_memory_profile_button.clicked.connect(self.check_memory_profile)
        self.ui.time_click_button.clicked.connect(self.start_timer)
        self.ui.select_directory_button.clicked.connect(self.open_directory_dialog)  # 디렉토리 선택 버튼 연결

        self.profile_path = ""
        self.screenshot_directory = ""

    # check_mouse_position_button이 눌리면 작동할 함수
    def check_mouse_position(self):
        self.saved_position = QCursor.pos()
        print("Saved position:", self.saved_position)
        self.ui.mouse_position_label.setText(f"Saved position: ({self.saved_position.x()}, {self.saved_position.y()})")

    # click_saved_position_button이 눌리면 작동할 함수
    def click_saved_position(self):
        if self.saved_position is not None:
            pyautogui.moveTo(self.saved_position.x(), self.saved_position.y())
            pyautogui.click()
        else:
            print("No position saved.")

    # time_click_button이 눌리면 작동할 함수
    def start_timer(self):
        try:
            self.timer_interval = int(self.ui.time_textEdit.toPlainText()) * 1000  # 초를 밀리초로 변환
            self.timer.setInterval(self.timer_interval)
            self.timer.start()
            print("Timer started")

            # 타이머 시작 후 일정 시간마다 스크린샷
            screenshot_interval = int(self.ui.screnn_shot_time_textEdit.toPlainText())
            self.screenshot_timer.start(screenshot_interval * 1000)

        except ValueError:
            print("Invalid timer interval")

    # 스크린샷을 찍는 함수
    def take_screenshot(self):
        if self.screenshot_directory:
            timestamp = time.strftime("%Y%m%d_%H%M%S")
            filename = f"{timestamp}.png"
            filepath = os.path.join(self.screenshot_directory, filename)
            pyautogui.screenshot(filepath)
            print(f"Screenshot saved: {filepath}")
        else:
            print("Screenshot directory is not set.")

    # memory_profile_check_button이 눌리면 작동할 함수
    def check_memory_profile(self):
        self.profile_path = self.ui.memory_profile_edit.toPlainText()
        if os.path.exists(self.profile_path):
            print("Memory profile file exists")
        else:
            print("Memory profile file does not exist")

    # 키보드 이벤트 처리
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_F3:
            self.check_mouse_position()
        elif event.key() == Qt.Key_F4:
            self.close()

        elif event.key() == Qt.Key_F5:
            self.click_saved_position()
            self.start_timer()

        elif event.key() == Qt.Key_F6:
            self.click_saved_position()

    # 종료 이벤트 처리
    def closeEvent(self, event):
        self.timer.stop()
        self.screenshot_timer.stop()
        super().closeEvent(event)

    # 디렉토리 선택 다이얼로그 열기
    def open_directory_dialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ShowDirsOnly
        directory = QFileDialog.getExistingDirectory(self, "Select Directory", options=options)
        if directory:
            self.screenshot_directory = directory
            self.ui.directory_label.setText(f"Selected directory: {directory}")
        else:
            print("Directory selection canceled.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()
