from PIL import Image
import pytesseract
import cv2
import numpy as np

# Tesseract 설치 경로를 환경변수로 설정 (Windows 사용자만 필요)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# 이미지 파일 열기
img = cv2.imread('Numbers/test.png')
if img is None:
    print('Image not loaded')

    # 이미지 처리 코드...


# 이미지 전처리: 흑백으로 변환 및 노이즈 제거
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.medianBlur(gray, 5)

# 이미지에서 텍스트 추출 (한국어 설정)
custom_config = r'--oem 3 --psm 6 outputbase digits'
text = pytesseract.image_to_string(gray, config=custom_config, lang='kor')

# 추출한 텍스트 출력
print(text)
