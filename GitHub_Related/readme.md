# 라즈베리파이와 GitHub 연동하기

라즈베리파이에서 Git을 설정하고 GitHub에 연동하는 방법을 단계별로 정리한 가이드입니다.

## 1. Git 설치 확인 및 설정

### (1) Git 설치 여부 확인
```
git --version
```
Git이 설치되어 있지 않다면 아래 명령어로 설치합니다.
```
sudo apt update
sudo apt install git
```

### (2) Git 사용자 정보 설정
Git 커밋 시 사용할 사용자 정보를 설정합니다.
```
git config --global user.name "사용자이름"
git config --global user.email "이메일주소"
```

## 2. SSH 키 생성 및 GitHub 등록

GitHub와 보안 연결을 위해 SSH 키를 생성하고 등록하는 과정입니다.

### (1) SSH 키 생성
```
ssh-keygen -t rsa -b 4096 -C "이메일주소"
```
- 기본 저장 경로(`/home/username/.ssh/id_rsa`)로 저장하려면 **Enter**를 누릅니다.
- 패스프레이즈 없이 진행하려면 **Enter**를 두 번 입력합니다.

### (2) SSH 에이전트 시작 및 키 추가
```
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_rsa
```

### (3) SSH 공개 키 확인 및 복사
```
cat ~/.ssh/id_rsa.pub
```
출력된 공개 키를 복사합니다.

### (4) GitHub에 SSH 키 등록
1. GitHub에 로그인 후 **Settings** → **SSH and GPG keys**로 이동합니다.
2. **New SSH key** 버튼 클릭
3. 제목 입력 후 공개 키를 붙여넣고 **Add SSH key** 클릭

## 3. 원격 저장소 연결 및 코드 관리

### (1) 저장소 클론
```
cd /home/pi/projects/
git clone git@github.com:사용자이름/저장소이름.git
```

### (2) SSH 연결 테스트
```
ssh -T git@github.com
```
성공적으로 인증되면 "Hi `<사용자명>`! You've successfully authenticated..." 메시지가 출력됩니다.

## 4. 코드 수정 및 GitHub 푸시

### (1) 파일 수정
```
nano 파일이름
```

### (2) 변경 사항 확인
```
git status
```

### (3) 변경 사항 스테이징
```
git add .
```

### (4) 커밋
```
git commit -m "커밋 메시지"
```

### (5) 원격 저장소로 푸시
```
git push origin main
```

## 5. 원격 저장소 URL을 SSH로 변경 (HTTPS → SSH)

현재 원격 저장소가 HTTPS 방식이라면 SSH 방식으로 변경해야 합니다.

### (1) 현재 원격 저장소 URL 확인
```
git remote -v
```
만약 `https://github.com/사용자이름/저장소이름.git`이라면 SSH URL로 변경해야 합니다.

### (2) SSH URL로 변경
```
git remote set-url origin git@github.com:사용자이름/저장소이름.git
```
이제 `git push` 시 SSH 키로 인증됩니다.

## 6. 요약

- **Git 설치**: `sudo apt install git`
- **Git 사용자 정보 설정**: `git config --global user.name/email`
- **SSH 키 생성**: `ssh-keygen -t rsa -b 4096 -C "이메일주소"`
- **GitHub에 SSH 키 등록**
- **원격 저장소 클론**: `git clone git@github.com:사용자이름/저장소이름.git`
- **파일 수정 및 푸시**: `git add .`, `git commit -m "메시지"`, `git push origin main`
- **HTTPS → SSH 변경**: `git remote set-url origin git@github.com:사용자이름/저장소이름.git`
