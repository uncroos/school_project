# GEMINITARS - 지능형 서비스 로봇

![GEMINITARS Logo](https://i.insider.com/5481ffc3eab8ea566b049f67?width=1600&format=jpeg&auto=webp)

## 🎯 프로젝트 개요
**GEMINITARS**는 영화 *인터스텔라*의 TARS에서 영감을 받아 개발한 **지능형 서비스 로봇**입니다. 
Google Gemini API를 활용하여 음성 대화 기능을 제공하며, 얼굴 인식, 물체 집기, 원격 조작 기능을 갖추고 있습니다.

## 🚀 주요 기능
### 1. 🤖 음성 인식 및 대화
- Google Gemini API 기반 AI 대화 시스템
- "TARS" 호출 후 음성 명령 인식
- 사용자 맞춤형 응답 제공

### 2. 👤 얼굴 인식
- OpenCV 기반 얼굴 인식 기능
- 사용자 등록 및 식별 가능
- 개인화된 대화 제공

### 3. ✋ 물체 집기 (그리퍼)
- 서보모터를 이용한 그리퍼 제어
- 특정 명령에 따라 물체 집기 및 놓기 수행

### 4. 📱 안드로이드 앱 연동
- 블루투스 또는 Wi-Fi 기반 원격 조작
- 앱에서 로봇 상태 모니터링 및 명령 전송 가능

## 🛠️ 사용 기술
### 📌 하드웨어
- **Raspberry Pi 5**
- **서보모터 & DC 모터** (그리퍼 및 이동 기능)
- **5인치 디스플레이** (상태 출력)
- **배터리** (이동 가능하도록 설계)
- **마이크 & 스피커** (음성 입출력)

### 📌 소프트웨어
- Python 3
- Google Gemini API (음성 인식 & 대화)
- OpenCV (얼굴 인식)
- SpeechRecognition (음성 인식)
- pyttsx3 (TTS 음성 출력)
- Flask (앱 연동)

## 🔧 설치 및 실행 방법
1. **필요한 라이브러리 설치**
   ```
   pip install opencv-python google-generativeai speechrecognition pyttsx3 flask
   ```
2. **GEMINITARS 실행**
   ```
   python main.py
   ```
3. **안드로이드 앱 연동**
   - 앱을 실행하고 로봇과 연결
   - 원격 조작 기능 사용 가능

## 🏆 팀 "현인무"
- **안요한** - 프로젝트 총괄 & AI 개발
- **이주민** - 하드웨어 설계 & 제작
- **박재우** - 안드로이드 개발 & 제어 담당
- **촤준명** - UI/UX 디자인 & 하드웨어 제작
- **송연우** - 하드웨어 제작

## 📞 문의
궁금한 점이 있다면 언제든지 문의하세요!
- 이메일: any492266@gmail.com
- GitHub Issues를 통해 문의 가능

