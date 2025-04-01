import google.generativeai as genai
import speech_recognition as sr
import pyttsx3
import re

# API 키 설정
API_KEY = ""
genai.configure(api_key=API_KEY)

# 모델 설정
MODEL_NAME = "gemini-2.0-flash-thinking-exp"
model = genai.GenerativeModel(MODEL_NAME)

# 음성 인식 객체 생성
r = sr.Recognizer()

# TTS 엔진 초기화
try:
    engine = pyttsx3.init()  # 기본 엔진 사용 시도
except Exception as e:
    print(f"기본 TTS 엔진 초기화 실패")
    engine = None # TTS 엔진 사용 불가능

def remove_markdown(text):
    """텍스트에서 기본적인 마크다운 문법을 제거합니다."""
    text = re.sub(r'\*\*([^*]+)\*\*', r'\1', text)  # 굵게
    text = re.sub(r'\*([^*]+)\*', r'\1', text)    # 기울임꼴
    text = re.sub(r'#+\s(.+)', r'\1', text)       # 제목
    text = re.sub(r'`(.+?)`', r'\1', text)         # 코드
    text = re.sub(r'\[(.+?)\]\((.+?)\)', r'\1', text) # 링크
    text = re.sub(r'!\[(.+?)\]\((.+?)\)', r'\1', text) # 이미지
    text = re.sub(r'\n+', r'\n', text)           # 과도한 개행 제거
    return text

def create_prompt(user_question):
    """프롬프트 템플릿을 사용하여 질문을 생성합니다."""
    template = f"""
    [지시사항]
    - 질문에 대해 간결하고 명확하게 답변하세요.
    - 마크다운 문법을 사용하지 마세요.
    - 답변은 2문장 이내로 요약하세요.
    - 답변은  한국어로 하세요

    [질문]
    {user_question}

    [답변]
    """
    return template

def listen_and_convert_to_text():
    """마이크에서 음성을 듣고 텍스트로 변환합니다."""
    with sr.Microphone() as source:
        print("말씀하세요...")
        r.adjust_for_ambient_noise(source)  # 주변 소음 적응
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio, language="ko-KR")  # 한국어 인식
        print("음성 인식 결과:", text)
        if text.lower().strip() in ["exit", "엑시트", "이그짓", "프로그램 종료","종료"]:
            return "SHUTDOWN"  # 종료 신호 반환
        return text
    except sr.UnknownValueError:
        print("음성을 이해할 수 없습니다.")
        return None
    except sr.RequestError as e:
        print(f"Google Speech Recognition API에 연결할 수 없습니다: {e}")
        return None

def speak(text):
    """텍스트를 음성으로 변환하여 출력합니다."""
    if engine: # TTS 엔진이 초기화되었을 경우에만 실행
        engine.say(text)
        engine.runAndWait()

# 채팅 세션 시작
print("Gemini와 음성 대화를 시작합니다. 질문 후 Enter 키를 누르세요. 'exit' 또는 '프로그램 종료'를 말씀하시면 종료됩니다.")
speak("Gemini와 음성 대화를 시작합니다.") # 시작 안내 음성 출력

try:
    while True:
        user_question = listen_and_convert_to_text()  # 항상 음성으로 질문 받음

        if user_question is None:
            speak("다시 시도해주세요.") # 음성 안내
            input("다시 시도하려면 Enter 키를 누르세요...")  # 음성 인식 실패 시 Enter 대기
            continue  # 루프 재시작

        if user_question == "SHUTDOWN":  # 종료 신호 확인
            print("대화를 종료합니다.")
            speak("대화를 종료합니다.") # 음성 안내
            break

        prompt = create_prompt(user_question) # 프롬프트 생성
        try:
            response = model.generate_content(prompt)
            if response and hasattr(response, 'text'):
                cleaned_text = remove_markdown(response.text) # 마크다운 제거
                print("Gemini 응답:", cleaned_text)
                speak(cleaned_text) # 응답 음성 출력
            else:
                print("Gemini 응답이 없습니다.")
                speak("Gemini 응답이 없습니다.") # 음성 안내
                if response:
                    print("응답 객체 정보:", response)  # 전체 응답 객체 정보 출력
                else:
                    print("response 객체가 None입니다.")
        except Exception as e:
            print(f"오류 발생: {e}")
            speak(f"오류가 발생했습니다. {e}")  # 오류 음성 출력

        input("다음 질문을 하려면 Enter 키를 누르세요...")  # 답변 후 Enter 대기

except KeyboardInterrupt:
    print("\n프로그램을 종료합니다.")
    speak("프로그램을 종료합니다.")  # 종료 안내 음성 출력

print("프로그램 종료.")

