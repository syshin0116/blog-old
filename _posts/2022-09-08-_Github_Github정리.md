---
title: "[Github]Github 정리"
date: 2022-09-08 02:35:29 +0900
categories: [ETC, Github]
tags: [github]
---

# [Github]Github 정리

## Git이란?
*  2005년 리투스 토르발스에 의해 개발
*  **분산형 버전관리 시스템 - DVCS (Distributed Version Control System)**
	*  컴퓨터 파일의 변경사항을 추적, 기록하는 버전 관리 프로그램
*  _로컬에 한정됨_

## Github란?
* **Git을 사용하는 프로젝트를 지원하는 웹호스팅 서비스**
* 클라우드 서버를 사용해 로컬에서 버전관리한 소스코드를 업로드하여 공유 가능

#### 따라서 Git으로 로컬 저장소에서 관리한 작업물을 Github에 업로드 하는 형식으로 주로 사용하게 된다

<br>

## Github의 장점:
개인:

- 원하는 시점으로 복원 가능

- 작업한 내역을 타임라인 순으로 확인 가능

- 수정한 내용에 대한 문서화 용이

- 브랜치를 생성하고 병합하는것도 간편


팀:

- 여러 사람이 하나의 소스를 작업해도 충돌 방지/해결

- 누가 어떤 작업을 진행했는지 확인 가능

<br>
## 원리:

<p align="center">
<img width="900" alt="Screen Shot 2022-09-09 at 12 50 10 AM" src="https://t1.daumcdn.net/cfile/tistory/993CCF4B5F17C75211
">
</p>

출처: [https://ux.stories.pe.kr/182 [UX 공작소:티스토리]](https://ux.stories.pe.kr/182)

복잡함으로 대충 보고 밑에글을 읽은 후에 다시 보며 이해하는걸 추천

<br>

## 명령어 정리:

| code                                	     | description                                                                                                    	| tips                                                                                                                                                                                                                                                                                                                                            	|
|----------------------------------------	|----------------------------------------------------------------------------------------------------------------	|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------	|
| git init                     	| 현재 directory를 Git 저장소로 변환                                                                             	| git 저장소 초기화                                                                                                                                                                                                                                                                                                                                    	|
| git add                        	| directory상의 변경 내용을 스테이징 영역에 추가                                                                 	| git add [파일/디렉토리 경로]  : 변경 내용의 일부만 스테이징 영역에 넘기고 싶을 때 디렉토리의 경로를 인자  git add .  : 현재 directory 모든 변경 내역 (상위 디렉토리의 변경 내용은 포함하지 않음)  git add -A  : 작업 directory상 모든 변경 내역  git add -p  : 각 변경 사항을 터미널에서 직접 눈으로 확인하면서 스테이징 영역으로 넘기거나 또는 제외 	|
| git commit                     	| directory의 변경/추가를 저장소에 기록 인덱스(staging area)에 등록되어 있는 파일 상태를 기록                    	| git commit -m "[커밋 메세지]"                                                                                                                                                                                                                                                                                                                        	|
| git push [저장소명] [브랜치명] 	| 로컬 저장소의 변경사항을 github에 반영                                                                         	| -u 옵션을 사용하면 최초 한 번만 저장소명과 브랜치명을 입력하고 이후에 생략 가능                                                                                                                                                                                                                                                                      	|
| git clone [저장소 경로]        	| 저장소 복제                                                                                                    	| 저장소를 clone 하면 ‘origin’ 이라는 리모트 저장소가 자동으로 등록 git clone -b [저장소 경로] : 특정 브랜치 clone                                                                                                                                                                                                                                     	|
| git fetch                      	| 원격저장소로 부터 변경된 내용을 가지고 온 후 병합 x                                                            	| 변경된 내역을 가지고 온 후 검토 후에 merge 할 수 있어서 충돌 방지                                                                                                                                                                                                                                                                                    	|
| git pull                       	| 원격저장소로 부터 변경된 내용을 가지고 온 후 병합(merge)                                                       	| pull = fetch + merge 와 같은 의미!                                                                                                                                                                                                                                                                                                                   	|
| git branch [브랜치명]          	| 브랜치를 생성                                                                                                  	|                                                                                                                                                                                                                                                                                                                                                      	|
| git checkout [브랜치명]        	| 브랜치 [브랜치명] 으로 이동                                                                                    	| b 옵션을 사용하면 브랜치 생성과 체크아웃 동시에                                                                                                                                                                                                                                                                                                      	|
| git merge [브랜치명]           	| 브랜치를 병합 (병합 할 브랜치에서 기록한 모든 commit이 master의 commit으로 기록)                               	| 같은 이름의 파일 안에 수정한 부분이 겹칠 때 충돌(conflit)이 발생                                                                                                                                                                                                                                                                                     	|
| git rebase                     	| 브랜치를 병합 (작업 중 남겼던 commit 중 불필요한 것들을 생략시키고 필요한 commit만 남겨서 master 병합이 가능) 	| -i : interactive 옵션: 중간에 낀 커밋 메세지를 수정 가능                                                                                                                                                                                                                                                                                             	|

## Git 사용 tip

### 새 Repository 생성시:

#### 1. Login,  Create New Repository
<br>
<p align="center">


<img width="700" alt="image" src="https://user-images.githubusercontent.com/99532836/189163644-de0128ce-2302-4751-849b-6bab6f6755d3.png">

</p>

README.md 파일:

* Repository 하단에 나타나는 글
* 주로 프로젝트 소개글이나 사용법 등 Repository에 포함된 내용에 대한 정보 기재
* 다른 확장자도 사용 가능하나 기본적으로 마크다운(Markdown, .md)사용
	* [마크다운 사용법](https://gist.github.com/ihoneymon/652be052a0727ad59601) 
	* [뱃지 예시 github](https://github.com/Ileriayo/markdown-badges)

.gitignore 파일:

* 업로드를 원하지 않는 Backup File이나 Log File , 혹은 컴파일 된 파일들을 Git에서 제외시킬수 있는 설정 File
* 최상위 Directory에 존재해야함
* .gitignore 파일 Push시 적용
* .gitignore 문법


```
# : comments

# no .a files
*.a

# but do track lib.a, even though you're ignoring .a files above
!lib.a

# only ignore the TODO file in the current directory, not subdir/TODO
/TODO

# ignore all files in the build/ directory
build/

# ignore doc/notes.txt, but not doc/server/arch.txt
doc/*.txt

# ignore all .pdf files in the doc/ directory
doc/**/*.pdf
``` 

#### 2. 로컬 directory와 repository 연동
* cmd 또는 terminal에서 repository와 연동하고 싶은 directory로 이동부터 해야한다
	* cd [directory 주소]


<br>
<p align="center">
<img width="900" alt="Screen Shot 2022-09-09 at 12 50 10 AM" src="https://user-images.githubusercontent.com/99532836/189167753-88a267a5-5243-4d97-a108-f7983e551fb7.png">
</p>
[참고로 위 화면은 repository생성시 addReadme 설정을 하지 않았을때 뜸]

설명:

```
git init 								# 현재 directory를 Git 저장소로 변환 (.git 이라는 git관련정보를 담을 파일 생성)
git add README.md 							# README.md파일을 추가
git commit -m "first commit" 						# "first commit" 커밋 메세지를 담아 커밋
git branch -M main 							# main브랜치 생성 (예전엔 default 브랜치명으로 master을 썼지만 main으로 바뀌는 추세)
git remote add origin [repository 주소] 					# 원격저장소 추가
git push -u origin main	 						# github에 반영
```

<br>

### Repository 를 Local Directory로 다운시:

<p align="center">
<img width="900" alt="Screen Shot 2022-09-09 at 12 50 10 AM" src="https://t1.daumcdn.net/cfile/tistory/9913EE3C5F17C75214">
</p>
출처: [https://ux.stories.pe.kr/182 [UX 공작소:티스토리]](https://ux.stories.pe.kr/182)

### git clone과 download zip의 차이점:

* Download ZIP : 그냥 순수하게 파일들만 압축해서 다운로드
* Clone 주소복사 : 순수파일들 + 커밋 히스토리 정보 다운로드 + remote add 가 된 상태로 로컬저장소(Local Repository)를 만들어 줌

따라서 평소엔 git clone을 추천한다. 다만, 주의할 점은

**git 저장소 안에 다른 git 저장소가 있을 시 커밋시 오류가 뜬다**

따라서 git 저장소 안에 다른 repository를 포함하고 싶다면 download zip 추천한다. 이미 clone을 해버린 경우, .git을 포함한 git관련 파일들을 삭제하면 해결된다.

### 팀 프로젝트 협업시:

이상적인 팀 프로젝트를 시작하는 방법:
1. 팀 리더가 환경설정, 대략적인 구성이 정해진 프로젝트 파일을 깃허브에 올린다.
2. 팀원이 git clone 명령어를 사용해 클론해간다.
3. 필요한 경우 브랜치를 만들어 각 브랜치에서 작업을 하고 메인 브랜치로 merge한다.
