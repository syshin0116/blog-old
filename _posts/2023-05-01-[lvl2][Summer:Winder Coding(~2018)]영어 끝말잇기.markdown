---
layout: post
title: "[lvl2][Summer/Winder Coding(~2018)]영어 끝말잇기"
date: 2023-05-01 10:31:29 +0900
categories: code-test
---

출처: [Programmers > 코딩테스트 연습 > 연습문제 > Summer/Winder Coding(~2018) > 영어 끝말잇기](https://school.programmers.co.kr/learn/courses/30/lessons/12981)

## 문제 설명:

1부터 n까지 번호가 붙어있는 n명의 사람이 영어 끝말잇기를 하고 있습니다. 영어 끝말잇기는 다음과 같은 규칙으로 진행됩니다.

1. 1번부터 번호 순서대로 한 사람씩 차례대로 단어를 말합니다.
1. 마지막 사람이 단어를 말한 다음에는 다시 1번부터 시작합니다.
1. 앞사람이 말한 단어의 마지막 문자로 시작하는 단어를 말해야 합니다.
1. 이전에 등장했던 단어는 사용할 수 없습니다.
1. 한 글자인 단어는 인정되지 않습니다.

다음은 3명이 끝말잇기를 하는 상황을 나타냅니다.

tank → kick → know → wheel → land → dream → mother → robot → tank

위 끝말잇기는 다음과 같이 진행됩니다.

* 1번 사람이 자신의 첫 번째 차례에 tank를 말합니다.
* 2번 사람이 자신의 첫 번째 차례에 kick을 말합니다.
* 3번 사람이 자신의 첫 번째 차례에 know를 말합니다.
* 1번 사람이 자신의 두 번째 차례에 wheel을 말합니다.
* (계속 진행)
끝말잇기를 계속 진행해 나가다 보면, 3번 사람이 자신의 세 번째 차례에 말한 tank 라는 단어는 이전에 등장했던 단어이므로 탈락하게 됩니다.

사람의 수 n과 사람들이 순서대로 말한 단어 words 가 매개변수로 주어질 때, 가장 먼저 탈락하는 사람의 번호와 그 사람이 자신의 몇 번째 차례에 탈락하는지를 구해서 return 하도록 solution 함수를 완성해주세요.

### 제한 사항
* 끝말잇기에 참여하는 사람의 수 n은 2 이상 10 이하의 자연수입니다.
* words는 끝말잇기에 사용한 단어들이 순서대로 들어있는 배열이며, 길이는 n 이상 100 이하입니다.
* 단어의 길이는 2 이상 50 이하입니다.
* 모든 단어는 알파벳 소문자로만 이루어져 있습니다.
* 끝말잇기에 사용되는 단어의 뜻(의미)은 신경 쓰지 않으셔도 됩니다.
* 정답은 [ 번호, 차례 ] 형태로 return 해주세요.
* 만약 주어진 단어들로 탈락자가 생기지 않는다면, [0, 0]을 return 해주세요.

	
### 입출력 예

| n | words                                                                                                                                                              | result |
|---|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|
| 3 | ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]                                                                                      | [3,3]  |
| 5 | ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"] | [0,0]  |
| 2 | ["hello", "one", "even", "never", "now", "world", "draw"]                                                                                                          | [1,3]  |

### 입출력 예 설명
#### 입출력 예 #1
3명의 사람이 끝말잇기에 참여하고 있습니다.

* 1번 사람 : tank, wheel, mother
* 2번 사람 : kick, land, robot
* 3번 사람 : know, dream, tank

와 같은 순서로 말을 하게 되며, 3번 사람이 자신의 세 번째 차례에 말한 tank라는 단어가 1번 사람이 자신의 첫 번째 차례에 말한 tank와 같으므로 3번 사람이 자신의 세 번째 차례로 말을 할 때 처음 탈락자가 나오게 됩니다.

#### 입출력 예 #2
5명의 사람이 끝말잇기에 참여하고 있습니다.

* 1번 사람 : hello, recognize, gather
* 2번 사람 : observe, encourage, refer
* 3번 사람 : effect, ensure, reference
* 4번 사람 : take, establish, estimate
* 5번 사람 : either, hang, executive


와 같은 순서로 말을 하게 되며, 이 경우는 주어진 단어로만으로는 탈락자가 발생하지 않습니다. 따라서 [0, 0]을 return하면 됩니다.

#### 입출력 예 #3
2명의 사람이 끝말잇기에 참여하고 있습니다.

* 1번 사람 : hello, even, now, draw
* 2번 사람 : one, never, world

와 같은 순서로 말을 하게 되며, 1번 사람이 자신의 세 번째 차례에 'r'로 시작하는 단어 대신, n으로 시작하는 now를 말했기 때문에 이때 처음 탈락자가 나오게 됩니다.
<br>

<hr>

## 피드백: 
* 처음엔 foreach가 아닌 for문으로 작성해서 가독성이 떨어졌었는데, 사용된 단어들을 리스트에 담음으로서 foreach문까지 사용할 수 있어서 가독성이 향상되었다 

<br>

## 코드 설명:
* foreach, enumerate, if ~ and 문 사용
* foreach문이 실행될때마다 단어를 리스트에 저장하고 해당 리스트를 사용해 중복과 끝말잇기 룰(마지막 단어의 끝과 다음 단어의 첫 문자가 같아야함)을 확인했다
* %, //를 활용해 순번과 사람을 구했다
	
## 코드:

```python
def solution(n, words):
    p = [words[0][0]]
    for i, w in enumerate(words):
        if w not in p and p[-1][-1] == w[0]:
            p.append(w)
        else:
            return [i % n + 1, (i//n)+1]
    return [0, 0]
```

## 우수답변자1 코드:

```python
def solution(n, words):
    for p in range(1, len(words)):
        if words[p][0] != words[p-1][-1] or words[p] in words[:p]: return [(p%n)+1, (p//n)+1]
    else:
        return [0,0]
```

## 우수답변자2 코드:
```python
def solution(n, words):
    answer = []
    turn = 0
    wordList = [words[0]]
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    for idx in range(1, len(words)):
        if words[idx-1][-1] != words[idx][0]:
            turn = idx
            break
        if words[idx] in wordList:
            turn = idx
            break
        wordList.append(words[idx])
    answer = [turn%n +1, turn//n + 1]
    if turn == 0:
        answer = [0, 0]
    return answer
```

## 우수답변자3 코드:
```python
import math
def solution(n, words):
    answer = []
    Pnum =0
    arr =[]
    i=0
    count = 1
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')
    arr.append(words[0])
    while(1):
        if len(arr)!=len(words):
            if words[i][-1]==words[i+1][0] and words[i+1] not in arr:
                arr.append(words[i+1])
                Pnum= (Pnum+1)%n
                i=(i+1)%(len(words)-1)
                count+=1
            else :
                count=(count+1)/n
                Pnum= (Pnum+1)%n
                break
        else :
            count=(count+1)/n
            Pnum= (Pnum+1)%n
            return [0,0]
    answer = [Pnum+1,math.ceil(count)]
    return answer```
