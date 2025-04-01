import google.generativeai as genai
import speech_recognition as sr
import pyttsx3
import re
import pygame
import random

# API 키 설정
API_KEY = ""
genai.configure(api_key=API_KEY)

# 모델 설정
MODEL_NAME = "gemini-2.0-flash-thinking-exp"
model = genai.GenerativeModel(MODEL_NAME)

# 감정별 이미지 매핑
emotion_images = {
    '기쁨': ["9.jpg", "1.jpg", "15.jpg"],
    '슬픔': ["22.jpg", "4.jpg", "24.jpg"],
    '화남': ["14.jpg", "17.jpg", "21.jpg"],
    '중립': ["3.jpg"]
}

# 이미지 기본 경로
IMAGE_PATH = "/home/spam/GitHub/image/"

# Pygame 초기화
pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("AI 감정 표현")

# 초기 이미지 로드
def load_image(image_name):
    try:
        img = pygame.image.load(IMAGE_PATH + image_name)
        img = pygame.transform.scale(img, (500, 500))
        return img
    except pygame.error:
        print(f"⚠️ 이미지 로드 실패: {image_name}")
        return None

current_image = load_image("3.jpg")
if current_image:
    screen.blit(current_image, (0, 0))
    pygame.display.update()

# 음성 인식 객체 생성
r = sr.Recognizer()

# TTS 엔진 초기화
try:
    engine = pyttsx3.init()
except Exception:
    print("TTS 엔진 초기화 실패")
    engine = None

def remove_markdown(text):
    text = re.sub(r'\*\*([^*]+)\*\*', r'\1', text)
    text = re.sub(r'\*([^*]+)\*', r'\1', text)
    text = re.sub(r'#+\s(.+)', r'\1', text)
    text = re.sub(r'`(.+?)`', r'\1', text)
    text = re.sub(r'\[(.+?)\]\((.+?)\)', r'\1', text)
    text = re.sub(r'!\[(.+?)\]\((.+?)\)', r'\1', text)
    text = re.sub(r'\n+', r'\n', text)
    return text

def create_prompt(user_question):
    return f"""
    [지시사항]
    - 질문에 대해 간결하고 명확하게 답변하세요.
    - 마크다운 문법을 사용하지 마세요.
    - 답변은 2문장 이내로 요약하세요.
    - 독일어로 대화할게요.
    -기초 독일어 수준으로 대화해줘.

    [질문]
    {user_question}

    [답변]
    """

def listen_and_convert_to_text():
    with sr.Microphone() as source:
        print("말씀하세요...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio, language="ko-KR")
        print("음성 인식 결과:", text)
        if text.lower().strip() in ["exit", "엑시트", "이그짓", "프로그램 종료", "종료"]:
            return "SHUTDOWN"
        return text
    except sr.UnknownValueError:
        print("음성을 이해할 수 없습니다.")
        return None
    except sr.RequestError as e:
        print(f"Google Speech Recognition API 연결 실패: {e}")
        return None

def speak(text):
    if engine:
        engine.say(text)
        engine.runAndWait()

def detect_emotion(text):
    if any(word in text for word in ["행복", "기뻐", "즐거워", "신나", "웃음"]):
        return "기쁨"
    elif any(word in text for word in ["슬퍼", "눈물", "우울", "속상해"]):
        return "슬픔"
    elif any(word in text for word in ["화나", "짜증", "열받아", "분노"]):
        return "화남"
    else:
        return "중립"

print("Gemini와 음성 대화를 시작합니다. 질문 후 Enter 키를 누르세요. 'exit' 또는 '프로그램 종료'를 말씀하시면 종료됩니다.")
speak("Gemini와 음성 대화를 시작합니다.")

try:
    while True:
        user_question = listen_and_convert_to_text()

        if user_question is None:
            speak("다시 시도해주세요.")
            input("다시 시도하려면 Enter 키를 누르세요...")
            continue

        if user_question == "SHUTDOWN":
            print("대화를 종료합니다.")
            speak("대화를 종료합니다.")
            break

        prompt = create_prompt(user_question)
        try:
            response = model.generate_content(prompt)
            if response and hasattr(response, 'text'):
                cleaned_text = remove_markdown(response.text)
                print("Gemini 응답:", cleaned_text)
                speak(cleaned_text)

                # 감정 감지 및 이미지 변경
                detected_emotion = detect_emotion(cleaned_text)
                new_image = random.choice(emotion_images[detected_emotion])
                current_image = load_image(new_image)
                if current_image:
                    screen.blit(current_image, (0, 0))
                    pygame.display.update()
                    pygame.event.pump()
            else:
                print("Gemini 응답이 없습니다.")
                speak("Gemini 응답이 없습니다.")
        except Exception as e:
            print(f"오류 발생: {e}")
            speak(f"오류가 발생했습니다. {e}")

        input("다음 질문을 하려면 Enter 키를 누르세요...")

except KeyboardInterrupt:
    print("\n프로그램을 종료합니다.")
    speak("프로그램을 종료합니다.")

print("프로그램 종료.")
pygame.quit()
