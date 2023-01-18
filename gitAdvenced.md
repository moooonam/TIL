# Git advanced

<hr>
<br>

![git](https://miro.medium.com/max/686/1*diRLm1S5hkVoh5qeArND0Q.png)

![git2](https://i.stack.imgur.com/MgaV9.png)
## Git undoing

- Git에서 되돌리기는 작업 상태에 따라 크게 세 가지로 분류

<br>

- Working Directory 작업단계
  - Working Directory에서 수정한 파일 내용을 이전 커밋 상태로 되돌리기
  - git restore
    - Working Directory에서 수정한 파일 내용을 이전 커밋 상태(제일 직전 버전)로 되돌리기
    - 이미 버전 관리가 되고 있는 파일만 되돌리기 가능
    - **git restore를 통해 되돌리면, 해당 내용을 복원할 수 없으니 주의할 것!**
    - git restore {파일이름}

<br>

- Staging Area 작업단계 
  - Staging Area에 반영된 파일을 Working Directory로 되돌리기 
  - root-commit 여부에 따라 두 가지 명령어로 나뉨
    - root-commit이 없는경우 : git rm --cached {파일이름}
    - root-commit이 있는경우(Git 저장소에 한 개 이상의 커밋이 있는 경우) : git restore --staged {파일이름}

<br>

- Repository 작업단계
  - git commit --amend
  - 상황별로 두 가지 기능으로 나뉨
    - Staging Area에 새로 올라온 내용이 없다면, 직전 커밋의 메시지만 수정
    - Staging Area에 새로 올라온 내용이 있다면, 직전 커밋을 덮어쓰기
  - **이전 커밋을 완전히 고쳐서 새 커밋으로 변경하므로, 이전 커밋은 일어나지 않은 일이 되며 히스토리에도 남지 않음을 주의할 것!**

<br>

#### Git reset

- 시계를 마치 과거로 돌리는 듯한 행위로, 프로젝트를 특정 커밋(버전) 상태로 되돌림
- 특정 커밋으로 되돌아 갔을 때, **해당 커밋 이후로 쌓았던 커밋들은 전부 사라짐**
- git reset [옵션]{커밋ID}
  - 옵션은 soft,mixed,hard 중 하나를 작성
  - 커밋 ID는 되돌아가고 싶은 시점의 커밋 ID를 작성
  - --soft
    - 되돌아간 커밋 이후의 파일들은 Staging area로 돌려놓음
  - --mixed
    - 되돌아간 커밋 이후의 파일들은 Working Directory로 돌려놓음
    - reset의 기본값
  - --hard
    - 되돌아간 커밋 이후의 파일들은 모두 Working Directory에서 삭제

<br>

#### Git revert

- 과거를 없었던 일로 만드는 행위로, 이전 커밋을 취소한다는 새로운 커밋을 생성함
- git revert {커밋ID}
- 개념적 차이
  - reset은 커밋 내역을 삭제하는 반면 revert는 새로운 커밋을 생성함
  - revert는 Github를 이용해 협업할 때, 커밋 내역의 차이로 인한 충돌 방지 기능

<br>

#### Git brangch

- 브랜치(Branch)는 나뭇가지라는 뜻으로, 여러 갈래로 작업 공간을 나누어 독립적으로 작업할 수 있도록 도와주는 Git의 도구
- 장점
  - 독립 공간을 형성하기 때문엔 원본에 대해 안전함
  - 하나의 작업은 하나의 브랜치로 나누어 진행되므로 체계적인 개발이 가능함
  - Git은 브랜치를 만드는 속도가 굉장히 빠르고, 적은 용량을 소모함

- 조회
  - git branch #로컬 저장소의 브랜치 목록 확인
  - git branch -r #원격 저장소의 브랜치 목록 확인
- 생성
  - git branch {브랜치 이름} #새로운 브랜치 생성
  - git branch {브랜치 이름}{커밋 ID} #특정 커밋 기준으로 브랜치 생성
- 삭제
  - git branch -d{브랜치 이름} #병합된 브랜치만 삭제 가능
  - git branch -D{브랜치 이름} #강제 삭제
- git switch
  - 현재 브랜치에서 다른 브랜치로 이동하는 명령어
  - git switch {브랜치 이름} #다른 브랜치로 이동
  - git switch -c {브랜치 이름} # 브랜치를 새로 생성 및 이동
  - git switch -c {브랜치 이름}{커밋ID} #특정 커밋 기준으로 브랜치 생성 및 이동
  - switch하기 전에, 해당 브랜치의 변경 사항을 반드시 커밋 해야함을 주의 할 것!
    - 다른 브랜치에서 파일을 만들고 커밋 하지 않은 상태에서 switch를 하면 브랜치를 이동했음에도 불구하고 해당 파일이 그대로 남아있게 됨
- 다른 로컬에서 이미 존재하는 브랜치에서 작업하고 싶을때
  - git branch -r 로 브랜치 목록 확인
  - git checkout -t origin/브랜치명 (브랜치 경로?)
    - 이러면 이동과 동시에 같은 브랜치 만들어짐

<br>

#### Git merge

- git merge
  - 분기된 브랜치들을 하나로 합치는 명령어
  - master 브랜치가 상용이므로, 주로 master 브랜치에 병합
  - git merge {합칠 브랜치 이름}
    - 병합하기 전에 브랜치를 합치려고 하는, 즉 메인 브랜치로 switch해야함
    - 병합에는 세 종류가 존재
      1. Fast-Forward
        - 마치 빨리감기처럼 브랜치가 가리키는 커밋을 앞으로 이동시키는 방법
      2. 3-way Merge
        - 각 브랜치의 커밋 두개와 공통 조상 하나를 사용하여 병합하는 방법  
      3. Merge Conflict
        - 두 브랜치에서 같은 부분을 수정한 경우, Git이 어느 브랜치의 내용으로 작성해야 하는지 판단하지 못하여 충돌이 발생했을 떄 이를 해결하며 병합하는 방법
        - 보통 같은 파일의 같은 부분을 수정했을 때 자주 발생함

<br>

#### Git workflow

- Branch와 원격 저장소를 이용해 협업을 하는 두 가지 방법
  - 원격 저장소 소유권이 있는 경우 -> Shared repository model
  - 원격 저장소 소유권이 없는 경우 -> Fork& Pull model

- Shared repository model
  - master 브랜치에 직접 개발하는 것이 아니라, 기능별로 브랜치를 따로 만들어 개발
  - Pull request를 사용하여 팀원 간 변경 내용에 대한 소통 진행

- Fork & Pull model
  - 오픈소스 프로젝트와 같이, 자신의 소유가 아닌 원격 저장소인 경우
  - 원본 원격 저장소를 그대로 내 원격 저장소에 복제(이러한 행위를 Fork라고 함)
  - 그낭 완성 후 복제한 내 원격 저장소에 Push
  - 이후 Pull Request를 통해 원본 원격 저장소에 반영될 수 있도록 요청함