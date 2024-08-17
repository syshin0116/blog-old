---
layout: post
title: Podly Github Readme
date: 2024-08-16 10:31 +0900
categories:
  - Project
  - Podly
tags: 
math: true
---
### Podly 프로젝트에서 Git 서브모듈 활용하기

Podly 프로젝트에서는 다양한 컴포넌트를 효과적으로 관리하기 위해 Git 서브모듈을 활용하고 있음. 이 글에서는 서브모듈이 어떻게 사용되는지, 레포지토리가 어떻게 구성되어 있는지, 그리고 로컬 환경에서의 구조를 간략히 설명함

#### 1. 서브모듈의 사용 목적

Podly 프로젝트는 여러 독립적인 컴포넌트로 구성되어 있으며, 각 컴포넌트는 별도의 Git 레포지토리로 관리됨. 이를 하나의 메인 레포지토리에서 관리하기 위해 서브모듈을 도입했음. 서브모듈을 통해 각 컴포넌트를 독립적으로 개발, 버전 관리할 수 있으며, 메인 레포지토리에서 이들을 통합하여 관리할 수 있음

#### 2. 레포지토리 구성

Podly 메인 레포지토리는 다음과 같은 구조로 구성되어 있음


```
podly/ 
├── .gitmodules  # 서브모듈 정보가 담긴 파일 
├── backend/     # 백엔드 서브모듈 디렉토리 
├── frontend/    # 프론트엔드 서브모듈 디렉토리 
└── README.md    # 프로젝트 설명 파일
```


- **.gitmodules**: 서브모듈의 경로와 원격 레포지토리 URL이 정의되어 있음
- **backend/**: 백엔드 관련 코드가 포함된 서브모듈 디렉토리
- **frontend/**: 프론트엔드 관련 코드가 포함된 서브모듈 디렉토리

#### 3. 로컬 환경에서의 구조

로컬에서 Podly 레포지토리를 클론할 때, 서브모듈도 함께 클론하여 사용함. 로컬 환경에서의 파일 구조는 다음과 같음


```
podly/ 
├── .git/            # Git 관련 디렉토리 
├── backend/         # 백엔드 서브모듈 (서브모듈의 Git 히스토리 포함) 
├── frontend/        # 프론트엔드 서브모듈 (서브모듈의 Git 히스토리 포함) 
├── .gitmodules      # 서브모듈 정보 파일 
└── README.md        # 메인 프로젝트 설명 파일
```
로컬에서는 각 서브모듈이 독립된 Git 프로젝트처럼 관리되며, `git submodule update --remote` 명령어를 통해 최신 상태로 업데이트할 수 있음. 이를 통해 메인 레포지토리에서 각 서브모듈의 상태를 최신으로 유지하고, 필요에 따라 커밋하여 메인 레포지토리에 반영할 수 있음

#### 4. 서브모듈 관리 방법

Podly 프로젝트를 클론하거나 서브모듈을 업데이트하려면 다음 명령어를 사용함

1. **최초 클론**
    
    
    `git clone --recurse-submodules https://github.com/GovTech-GenAI/podly.git`
    
2. **메인 레포지토리 및 서브모듈 업데이트**
    
    
    `git pull origin main git submodule update --remote`
    

이 명령어들을 통해 메인 레포지토리와 서브모듈을 최신 상태로 유지할 수 있음. 서브모듈을 효과적으로 사용하면, 대규모 프로젝트에서도 각 컴포넌트를 독립적으로 관리하면서도 일관된 버전 관리를 할 수 있음



## Podly Main README.md

# Podly  
This repository contains Git submodules for managing various components of the project.  

## Cloning the Repository  

To clone this repository along with all its submodules, run the following command:  
```bash 
git clone --recurse-submodules https://github.com/GovTech-GenAI/podly.git
```

This command will clone the main repository and automatically initialize and update all the submodules.


## Updating the Repository and Submodules

If the repository is already cloned and you want to update both the main repository and its submodules to their latest versions, follow these steps:

1. **Update the main repository**:

```bash
git pull origin main
```

	This command fetches the latest changes in the main repository.
    
2. **Update the submodules**:
    
```bash
git submodule update --remote
```

    This command updates all submodules to their latest commits from their respective remote repositories.