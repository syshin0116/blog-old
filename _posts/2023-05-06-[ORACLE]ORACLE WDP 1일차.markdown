---
title: "[ORACLE-WDP]1일차- 리눅스 환경, 오라클 설치"
date: 2023-05-06 20:00:00 +0900
categories: [Database,ORACLE-WDP]
tags: [oracle, wdp, database]     # TAG names should always be lowercase
---


<!--#### 공유url: http://naver.me/xoKMlnp5
#### 암호: -->

<!--강사님 정보:

- 경력: 전북은행 새마을금고 DB, DW/DM-->

# VM Virtual Machine
- Download url : https://www.virtualbox.org/wiki/Downloads
- 네트워크 설정
    - network > 수동어댑터 설정 > ipv4 주소: 10.0.2.2 > ncpa.cpl > 이더넷 > ipv4 > 속성에서 바뀐것 확인
- machine > 새로 만들기 > 
    - 이름: ORACLE_LINUX
    - 위치: E drive vmFile
    - skip unattended installation
    - iso: USB다운로드 파일

    
![image](https://user-images.githubusercontent.com/99532836/236602113-5a39c54e-63d0-4acf-b2a1-a864d341a6b4.png)
![image](https://user-images.githubusercontent.com/99532836/236602132-4ef07410-1b0f-46b0-b3bc-10b4883a293f.png)
    - virtual hard disk : 200GB

![image](https://user-images.githubusercontent.com/99532836/236602190-f82c231b-50e0-4d3d-a246-2784b6c8e2cd.png)
![vmware_network설정](https://user-images.githubusercontent.com/99532836/236591187-7a1ab528-5e7c-4654-8ce0-036611c56282.png)
![vmware_network설정2](https://user-images.githubusercontent.com/99532836/236591188-acce325b-c7a5-4944-936d-a2129041324c.png)



- 키보드 설정
    - 입력 > 키보드 > 키보드 설정 > 호스트 키 조합: Application 

![key설정](https://user-images.githubusercontent.com/99532836/236591177-345fb000-7eae-4ddf-b4b8-7919fe51de02.png)

## Installation Summary
![language support](https://user-images.githubusercontent.com/99532836/236591179-76f81ba6-4998-49ac-80b2-ce6a5b844f2b.png)

### Software Selection
CLI를 이용한 가장 기본적인 환경 설정
- Minimal install > Standard
![software_selection](https://user-images.githubusercontent.com/99532836/236591180-3760ecf2-ab47-4744-aae1-27a168f85a30.png)

### Installation Destination

![image](https://user-images.githubusercontent.com/99532836/236602886-77c58c25-4962-4896-8ded-29b53fd45f49.png)
![](https://velog.velcdn.com/images/syshin0116/post/4dfafeb3-53ea-4039-8434-2eecddbfbc5d/image.png)

#### Manual Partitioning
- /home, / 삭제
- swap > Desired Capacity: 16 GiB
- / 추가 > 
    - Mount Point: /
    - Desired Capacity: max
    
![화면 캡처 2023-05-06 100037](https://user-images.githubusercontent.com/99532836/236591181-3b89c40a-b84c-4ff5-b39b-338a8dd26fd6.png)
![화면 캡처 2023-05-06 100145](https://user-images.githubusercontent.com/99532836/236591183-24f0037e-6894-4218-8ea9-03cd41f2e3c1.png)
### Network & Host
![화면 캡처 2023-05-06 100704](https://user-images.githubusercontent.com/99532836/236591184-a7b1650b-e717-40c0-9f60-0a0bdd14e828.png)
- S3 > configure > ipv4 settings > Hostname: HORA19C
- S8 > configure > ipv4 settings > manual > 
    - address: 10.0.2.15
    - net mask: 24
    - gateway: 10.0.2.1
    - DNS server: 168.126.63.1

![image](https://user-images.githubusercontent.com/99532836/236603410-31eed586-fccf-4bd1-a17e-ca0828af9403.png)


### Root password
- id: root
- password: oracle


## 부팅 이후 설정
boot > ```ifconfig```
s3: 동적 할당받은 ip
s8: 
- ```/etc/sysconfig/network-scripts``` 에 vi로 s3, s8확인
- ```vi ifcfg-emp0s8``` > ONBOOT = yes 로 수정
- reboot
- ```ifconfig``` > s8 바뀐것 확인
- ```ping 168.126.63.1``` > 확인
- 윈도우 cmd: ```ping 10.0.2.15``` > 확인

## FeedBack
- 처음 설치 해봤을땐 문제 없었으나, 본 블로그에 정리한 대로 다시 해보니 네트워크 오류(핑 실패)가 발생했다
- /etc/sysconfig/network-scripts/ifcfg-emp0s3 에서 vi로 ip address, DNS server, gateway를 지워주고 껐다 키니 정상 작동됐다
- emp0s3 은 ip를 동적할당 받기 때문에 위와 같은 해결이 가능했다

## FileZilla, Xming, Putty 설치
- 네이버 드라이브 > SW > 1.기타 프로그램에 설치 파일 있음 
- XMing
    - Create a desktop icon for Xming



# Oracle 19c 설치
### 1.  putty HOST 설정
- Host ip address: 10.0.2.15
- id: root
- password: oracle

### 2. Linux 설정 추가
```sh
vi /etc/hosts
```
- 10.0.2.15 HORA19C HORA19C 추가


![화면 캡처 2023-05-06 112918](https://user-images.githubusercontent.com/99532836/236594224-421a671e-2643-4554-beed-3b6c9fcc3930.png)

```shell
vi /etc/selinux/config
```
- #SELINUX=enforcing 주석처리
SELINUX=permissive 추가


![화면 캡처 2023-05-06 113039](https://user-images.githubusercontent.com/99532836/236594226-abb54b9b-8a64-4cef-99f8-4da21508d20d.png)

### 3. Linux 패키지 추가 설치
```shell
yum search preinstall
yum install make perl xorg-x11-xauth xterm libGL libEGL nmap
```

### 4. oracle 계정 그룹 변경
```shell
cd /home
ls
```
- /home/oracle 디렉토리 생성된것 확인

![화면 캡처 2023-05-06 114700](https://user-images.githubusercontent.com/99532836/236594638-cb2f3262-9958-42bc-a40c-8f910a018451.png)

- oracle 계정의 그룹을 oinstall에서 dba 그룹으로 변경 , 패스워드 변경
- 패스워드는 oracle 을 두번 입력한다.
```shell
usermod -g dba -G dba oracle
passwd oracle
```

![화면 캡처 2023-05-06 114718](https://user-images.githubusercontent.com/99532836/236594640-0fd5733b-2a53-4bb3-98b3-be17484d3011.png)

### 5. 오라클 홈디렉토리 생성 및 권한/소속그룹 변경
```shell
mkdir -p /app/oracle/product/19.3/db_1
chmod 775 -R /app
chown -R oracle:dba /app
```
- mkdir -p : 한꺼번에 여러 directory 생성

### 6. Linux 불필요한 서비스 종료

```shell
systemctl stop bluetooth.service
systemctl disable bluetooth.service
systemctl stop firewalld
systemctl disable firewalld
systemctl stop chronyd
systemctl disable chronyd
systemctl stop ntpdate
systemctl disable ntpdate
systemctl stop avahi-daemon
systemctl disable avahi-daemon
systemctl stop libvirtd
systemctl disable libvirtd.service
systemctl stop cups
systemctl disable cups.service
```


### 7. Oracle 계정의 .bash_profile 설정
- oracle 계정으로 전환
- ctrl + D : 로그아웃, quit, exit
- oracle/oracle로 다시 로그인

```shell
$ cd /home/oracle/
$ vi .bash_profile
export ORACLE_HOSTNAME=HORA19C
export ORACLE_UNQNAME=ORA19C
export ORACLE_SID=ORA19C
export ORACLE_BASE=/app/oracle
export ORACLE_HOME=$ORACLE_BASE/product/19.3/db_1
export DATA_DIR=/app/oracle/oradata
export TNS_ADMIN=$ORACLE_HOME/network/admin
export PATH=$ORACLE_HOME/bin:$PATH:/bin:/usr/bin:/usr/sbin
export LD_LIBRARY_PATH=$ORACLE_HOME/lib:/lib:/usr/lib
export CLASSPATH=$ORACLE_HOME/jlib:$ORACLE_HOME/rdbms/jlib
export NLS_LANG=AMERICAN_AMERICA.AL32UTF8
export PS1='[$PWD]\\$ '
#export NLS_LANG=KOREAN_KOREA.AL32UTF8
#alias sqlplus='rlwrap sqlplus'
#alias ss='sqlplus / as sysdba'
```
```
. .bash_profile
```
앞에 프롬프트가 /home/oracle 로 변경되는것 확인

### 8. FileZilla
    - Hostname: 10.0.2.15
    - 사용자명: oracle
    - 비밀번호: oracle
    - 포트: 22
    
![화면 캡처 2023-05-06 120339](https://user-images.githubusercontent.com/99532836/236599500-302b1265-a1fb-4ccb-bf97-34d6e754f283.png)
![화면 캡처 2023-05-06 120524](https://user-images.githubusercontent.com/99532836/236599501-3ae8aa7a-8352-4cb8-b210-1c250054fa9f.png)
![화면 캡처 2023-05-06 120635](https://user-images.githubusercontent.com/99532836/236599502-cc904786-8cb4-4f67-a76d-25da8cd07563.png)


### 10. 리눅스 시작 > 오라클 설치 파일 압축 풀기 (oracle 계정
```shell
cd $ORACLE_HOME
unzip LINUX.X64_193000_db_home.zip
```
- XMing 실행 (우측 하단 프로그램 XMING 뜨는 것 확인)(중요!)


### 12. 오라클 설치 (XMing이 실행되고 있는 상태여야함)

#### 12.1 Putty 설정

![화면 캡처 2023-05-06 121808](https://user-images.githubusercontent.com/99532836/236599503-8795498a-d3ed-43f5-a743-a1c53d05bc26.png)

- OS 인증 에러 방지를 위해 $CV_ASSUME_DISTID 환경 변수 설정

```
cd $ORACLE_HOME
export CV_ASSUME_DISTID=OEL7
echo $CV_ASSUME_DISTID
```
- 오라클 runInstall 실행
```
cd $ORACLE_HOME
ls runInstaller
./runInstaller
```
./runinstaller
한글깨짐 현상 시
```
export LANG=C
export LC_ALL=C
```


#### 12.2 오라클 설치화면

![화면 캡처 2023-05-06 132426](https://user-images.githubusercontent.com/99532836/236599818-ca34282c-aad4-4084-9377-46fdbb0625fa.png)
![화면 캡처 2023-05-06 132441](https://user-images.githubusercontent.com/99532836/236599820-675e8408-77be-4a76-859e-4797dec1d58d.png)
![화면 캡처 2023-05-06 132452](https://user-images.githubusercontent.com/99532836/236599826-45d23444-dfe1-4635-9ba1-79fb25bd170f.png)
![화면 캡처 2023-05-06 132504](https://user-images.githubusercontent.com/99532836/236599828-ab5eaae8-b6a1-4d20-ab35-6a9a806d2469.png)
![화면 캡처 2023-05-06 132517](https://user-images.githubusercontent.com/99532836/236599829-1147dee5-b5da-4172-837d-7198968b75fd.png)
![화면 캡처 2023-05-06 132529](https://user-images.githubusercontent.com/99532836/236599830-b2143546-2771-4b93-aada-712d1249d938.png)
![화면 캡처 2023-05-06 132541](https://user-images.githubusercontent.com/99532836/236599835-066c54ea-cc1f-4a51-afd2-c1574f0bd664.png)
![화면 캡처 2023-05-06 132551](https://user-images.githubusercontent.com/99532836/236599840-a0e9f71a-bbfb-4af6-a776-c03dd6a729d5.png)
![화면 캡처 2023-05-06 132604](https://user-images.githubusercontent.com/99532836/236599842-6535740b-c295-4747-9a50-d82ceac38f79.png)
![화면 캡처 2023-05-06 132615](https://user-images.githubusercontent.com/99532836/236599843-c9b77477-75c2-462b-b7f8-f131ba7bd767.png)
![화면 캡처 2023-05-06 132626](https://user-images.githubusercontent.com/99532836/236599848-fad2a102-48ba-4a89-9bc5-874416965d49.png)
![화면 캡처 2023-05-06 132637](https://user-images.githubusercontent.com/99532836/236599852-a76d2aaa-98af-4b92-9222-41ae65389f8f.png)
![화면 캡처 2023-05-06 132647](https://user-images.githubusercontent.com/99532836/236599855-b954e90c-729c-4a4c-8371-ebccdb564fc2.png)
![화면 캡처 2023-05-06 132658](https://user-images.githubusercontent.com/99532836/236599860-aedbb01c-418c-47a5-96f0-938b3099e36e.png)
![화면 캡처 2023-05-06 132715](https://user-images.githubusercontent.com/99532836/236599870-dafc5d39-8fb7-4cc7-a54c-ad4a5d1d6477.png)
![화면 캡처 2023-05-06 132731](https://user-images.githubusercontent.com/99532836/236599873-46dcfd41-e614-42c6-8e6d-a4cd340f5562.png)
![화면 캡처 2023-05-06 132745](https://user-images.githubusercontent.com/99532836/236599877-b47a6a55-9686-4443-b4c7-96f27865ab0b.png)




https://HORA19C:5500/em

https://10.0.2.15:5500/em

```sh
cd /app/oracle/product/19.3/db_1/OPatch
ls -l opatch
./opatch lspatches
netstat -plnt | grep tns
netstat -a | grep ssh
lsnrctl status
```
![백업](https://user-images.githubusercontent.com/99532836/236601663-1f76bb0e-a82e-459a-8b4f-03c6f0469738.png)

백업 방법: 

```sh
su -
poweroff
```

VM VirtualBox
![백업](https://user-images.githubusercontent.com/99532836/236601685-6f1b6395-4947-459e-9f97-a10d529b6286.png)


# Oracle
## Oracle 접속/종료
### putty 10.0.2.2 접속
### 리스너 구동, 성공적 구동 확인:

```sh
$ lsnrctl start
```
### 8.sqlplus 접속:

#### 1. OS 인증방식으로 접속
```shell
sqlplus / as sysdba
sqlplus sys/oracle as sysdba
sqlplus oracle/oracle as sysdba
```
#### 2. EZ CONNECT 방법
- (OS 인증방식으로 들어가서 startup을 해 놔야 가능)
```shell
sqlplus 아이디/비밀번호@IP 주소:포트번호/sid
sqlplus sys/oracle@10.0.2.2:1521/ora19c as sysdba
sqlplus sys/oracle@10.0.2.15:1521/ora19c as sysdba
sqlplus hr/hr@10.0.2.2:1521/ora19c
```

#### 3. oracle client 방법
- tnsnames.ora 에 호스트명, IP, PORT, 서비스 이름등 접속 정보가 저장되어있다.
호스트명(ALIAS)은 대소문자를 구분 하지 않는다.
- (OS 인증방식으로 들어가서 startup을 해 놔야 가능)
```shell
sqlplus 아이디/비밀번호@호스트명(ALIAS)
sqlplus sys/oracle@ora19c as sysdba
sqlplus hr/hr@ora19c
```


### 11. 오라클의 인스턴스명과 상태를 확인한다.
```sql
SQL > select instance_name, status from v$instance;
```
### 12. 리스터 종료, 정상종료 확인
```shell
 lsnrctl stop
```
### 13. 오라클 종료
```shell
SQL > shutdwon immediate
```

### 14. sqlplus 종료
1. exit
2. quit
3. ctrl+d (리눅스에서만 가능)


## sqlDeveloper
- 접속 [+] 모양
![image](https://user-images.githubusercontent.com/99532836/236611426-a9d320d4-947e-4116-b182-7f5145be0617.png)

### SQL 단축키
![image](https://user-images.githubusercontent.com/99532836/236612088-d3c7c450-94c2-4adf-bcdf-84393bbd0ee5.png)
