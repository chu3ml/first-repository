import speech_recognition as sr
import pyautogui
import time

# 음성 인식 객체 생성
recognizer = sr.Recognizer()

for i in range(100) :
    
    # 마이크에서 입력받기
    with sr.Microphone() as source:
        print("말하세요...")
        audio = recognizer.listen(source)
    
    # Google Web Speech API를 사용하여 음성 인식
    try:
        text = recognizer.recognize_google(audio, language='ko-KR')
        print("인식된 텍스트: ", text)
        
        if "다음으로" in text :
            time.sleep(1)
            
            # 슬라이드 넘기기 (다음 슬라이드)
            pyautogui.press('right')  # 오른쪽 방향키로 슬라이드 넘기기
    except sr.UnknownValueError:
        print("Google Web Speech API가 당신의 말을 이해하지 못했습니다.")
    except sr.RequestError as e:
        print(f"Google Web Speech API 서비스에 문제가 발생했습니다; {e}")
