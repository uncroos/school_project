# 라즈베리파이와 GitHub 연동하기

이 문서는 라즈베리파이에서 Git과 GitHub을 설정하고, 원격 저장소에 푸시하는 과정에 대한 안내입니다.

## 1. Git 설치 확인

라즈베리파이에서 Git이 설치되어 있는지 확인하려면, 아래 명령어를 실행하세요:

```
git --version
```

만약 Git이 설치되어 있지 않다면, 아래 명령어로 설치합니다:

```
sudo apt update
sudo apt install git
```

## 2. Git 사용자 정보 설정

Git을 사용할 때 커밋에 사용하는 사용자 이름과 이메일을 설정해야 합니다. 아래 명령어를 사용해 설정하세요:

```
git config --global user.name "uncroos"
git config --global user.email "any492266@gmail.com"
```

이렇게 설정하면, Git에서 이 사용자 정보가 모든 커밋에 사용됩니다.

## 3. SSH 키 생성 및 GitHub에 등록

GitHub와 안전하게 연동하려면 SSH 키를 생성해야 합니다.

### (1) SSH 키 생성

터미널에서 아래 명령어를 입력하여 SSH 키를 생성합니다:

```
ssh-keygen -t rsa -b 4096 -C "any492266@gmail.com"
```

- 기본 경로(`/home/username/.ssh/id_rsa`)로 저장하려면 **Enter**를 누릅니다.
- 패스프레이즈를 설정하지 않으려면 **Enter**를 두 번 누릅니다.

### (2) SSH 에이전트 시작

SSH 키를 추가하려면 먼저 SSH 에이전트를 시작해야 합니다:

```
eval "$(ssh-agent -s)"
```

그 후 생성한 SSH 키를 SSH 에이전트에 추가합니다:

```
ssh-add ~/.ssh/id_rsa
```

### (3) SSH 공개 키 복사

생성한 SSH 공개 키를 복사하려면 아래 명령어를 사용하세요:

```
cat ~/.ssh/id_rsa.pub
```

출력된 공개 키를 복사하세요.

### (4) GitHub에 SSH 키 등록

1. GitHub에 로그인 후, 오른쪽 상단의 **Profile Picture** → **Settings**를 클릭합니다.
2. 왼쪽 사이드바에서 **SSH and GPG keys**를 선택합니다.
3. **New SSH key** 버튼을 클릭하고, 제목을 입력한 후 복사한 공개 키를 붙여넣고 **Add SSH key**를 클릭합니다.

## 4. 원격 저장소 연결

이제 SSH 키가 GitHub에 등록되었으므로, GitHub 저장소와 연결할 수 있습니다.

### (1) 저장소 클론

원격 저장소를 클론하려면 아래 명령어를 입력합니다:

```
cd /home/lenovo/Documents/Github/
git clone https://github.com/uncroos/school_project.git
```

위 명령어는 GitHub에 있는 `school_project` 저장소를 `/home/lenovo/Documents/Github/` 폴더에 클론합니다.

### (2) SSH로 연결 확인

SSH 연결을 확인하려면 아래 명령어를 실행합니다:

```
ssh -T git@github.com
```

GitHub에서 "Hi `<사용자명>`! You've successfully authenticated..."라는 메시지가 나오면, SSH 연결이 정상적으로 설정된 것입니다.

## 5. 파일 수정 후 푸시

저장소를 클론하고 파일을 수정한 후, 변경 사항을 GitHub에 푸시하려면 다음 단계를 따릅니다.

### (1) 파일 수정

원하는 파일을 편집기에서 수정합니다. 예를 들어, `nano`로 파일을 수정할 수 있습니다:

```
nano <파일이름>
```

### (2) 변경 사항 확인

수정된 파일을 Git에 반영하려면 아래 명령어를 입력해 변경 사항을 확인합니다:

```
git status
```

### (3) 변경 사항 스테이징

수정한 파일을 스테이징 영역에 추가하려면 아래 명령어를 사용합니다:

```
git add .
```

### (4) 커밋

변경 사항을 커밋하려면 아래 명령어를 사용합니다:

```bash
git commit -m "커밋 메시지"
```

### (5) 푸시

수정한 내용을 원격 저장소에 푸시하려면 아래 명령어를 사용합니다:

```
git push origin master
```

푸시가 완료되면 GitHub 저장소에 수정된 파일이 반영됩니다.

## 6. 요약

- **Git 설치**: `sudo apt install git`
- **Git 사용자 정보 설정**: `git config --global user.name` 및 `git config --global user.email`
- **SSH 키 생성**: `ssh-keygen`
- **GitHub에 SSH 키 등록**: 공개 키를 GitHub에 추가
- **원격 저장소 클론**: `git clone https://github.com/uncroos/school_project.git`
- **파일 수정 및 푸시**: `git add .`, `git commit`, `git push`

이 과정들을 통해 라즈베리파이에서 GitHub과 연동하여 파일을 수정하고 푸시하는 작업을 수행할 수 있습니다.
```

위의 내용은 **마크다운 형식**으로 작성된 `README.md` 파일입니다. 이 파일을 그대로 `README.md`로 저장하고, 프로젝트 폴더에 넣어두시면 됩니다. 이 문서는 처음부터 끝까지 라즈베리파이에서 GitHub과의 연동 작업을 단계별로 안내합니다.

3. GitHub의 SSH 인증 방식 사용

HTTPS 방식 대신 SSH 방식으로 원격 저장소를 푸시하려면, SSH를 통해 인증을 설정해야 합니다. 아래는 SSH로 푸시하는 방법입니다.
해결 방법: SSH로 원격 저장소 연결
(1) GitHub SSH URL 사용

현재 git push 명령어에서 HTTPS URL을 사용하고 있지만, SSH URL로 변경해야 합니다. SSH는 Personal Access Token을 요구하지 않으며, SSH 키 인증을 사용하여 푸시할 수 있습니다.

    현재 연결된 원격 저장소의 URL을 확인하려면 아래 명령어를 실행하세요:

    git remote -v

    만약 https://github.com/uncroos/school_project.git로 표시된다면, 이를 SSH URL로 변경해야 합니다. SSH URL은 git@github.com:uncroos/school_project.git 형식입니다.

(2) 원격 저장소 URL을 SSH로 변경

git remote set-url origin git@github.com:uncroos/school_project.git

이제 GitHub에서 SSH 방식으로 푸시할 수 있습니다.
(3) SSH 키를 GitHub에 등록

이전에 SSH 키를 생성하고 GitHub에 등록한 상태여야 SSH로 인증이 가능합니다. 아직 SSH 키를 등록하지 않았다면, 다음 단계를 진행합니다.

    SSH 키를 생성하고 GitHub에 등록하는 방법은 앞서 설명한 대로 진행하면 됩니다. ~/.ssh/id_rsa.pub 파일의 공개 키를 GitHub의 SSH 설정에 추가해야 합니다.

(4) SSH로 푸시

SSH URL로 변경한 후에는 아래 명령어로 다시 푸시를 시도해보세요:

git push origin main

이제 SSH 키로 인증되므로 Personal Access Token이 필요하지 않습니다.
