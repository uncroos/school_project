# Raspberry Pi 환경 설정 가이드

## 1. 기본 설정
### 라즈베리파이 환경 설정
1. `메뉴 -> Preferences -> Raspberry Pi Configuration` 실행
2. `Localisation` 탭에서 `Set Wi-Fi Country` 선택 후 `KR Korea (South)`로 설정

### 패키지 업데이트
```bash
sudo apt-get update && sudo apt-get upgrade -y
```

## 2. 현지화 설정
1. `메인 메뉴 -> Preferences -> Raspberry Pi Configuration` 실행
2. `Localisation` 탭에서 `Set TimeZone` 선택 후 `Asia/Seoul` 설정
3. `Localisation -> Set Keyboard` 선택 후 다음과 같이 설정:
   - **Model**: Generic 105-key PC
   - **Layout**: Korean
   - **Variant**: Korean (101/104 key compatible)

## 3. 한글 입력기 및 폰트 설치
```bash
sudo apt-get install ibus
sudo apt-get install ibus-hangul
sudo apt-get install fonts-unfonts-core
```

### 리부팅
```bash
sudo reboot
```

### 한글 입력기 설치 및 설정
```bash
sudo apt-get install nabi
```
1. `메인 메뉴 -> Preferences -> Input Method` 실행
2. `OK` 클릭 후 `Ibus` 선택 -> `OK` 클릭