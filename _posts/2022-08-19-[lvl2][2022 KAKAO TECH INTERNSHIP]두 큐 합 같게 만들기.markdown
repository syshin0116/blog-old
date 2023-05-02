---
layout: post
title: "[lvl2][2022 KAKAO TECH INTERNSHIP]두 큐 합 같게 만들기"
date: 2022-08-19 10:35:29 +0900
categories: code-test
---

출처: [Programmers > 2022 KAKAO Tech Intership > 두 큐 합 같게 만들기](https://school.programmers.co.kr/learn/courses/30/lessons/118667)

# 두 큐 합 같게 만들기

## 문제 설명:

길이가 같은 두 개의 큐가 주어집니다. 하나의 큐를 골라 원소를 추출(pop)하고, 추출된 원소를 다른 큐에 집어넣는(insert) 작업을 통해 각 큐의 원소 합이 같도록 만들려고 합니다. 이때 필요한 작업의 최소 횟수를 구하고자 합니다. 한 번의 pop과 한 번의 insert를 합쳐서 작업을 1회 수행한 것으로 간주합니다.

큐는 먼저 집어넣은 원소가 먼저 나오는 구조입니다. 이 문제에서는 큐를 배열로 표현하며, 원소가 배열 앞쪽에 있을수록 먼저 집어넣은 원소임을 의미합니다. 즉, pop을 하면 배열의 첫 번째 원소가 추출되며, insert를 하면 배열의 끝에 원소가 추가됩니다. 예를 들어 큐 [1, 2, 3, 4]가 주어졌을 때, pop을 하면 맨 앞에 있는 원소 1이 추출되어 [2, 3, 4]가 되며, 이어서 5를 insert하면 [2, 3, 4, 5]가 됩니다.

다음은 두 큐를 나타내는 예시입니다.

	queue1 = [3, 2, 7, 2]
	queue2 = [4, 6, 5, 1]

두 큐에 담긴 모든 원소의 합은 30입니다. 따라서, 각 큐의 합을 15로 만들어야 합니다. 예를 들어, 다음과 같이 2가지 방법이 있습니다.

1. queue2의 4, 6, 5를 순서대로 추출하여 queue1에 추가한 뒤, queue1의 3, 2, 7, 2를 순서대로 추출하여 queue2에 추가합니다. 그 결과 queue1은 [4, 6, 5], queue2는 [1, 3, 2, 7, 2]가 되며, 각 큐의 원소 합은 15로 같습니다. 이 방법은 작업을 7번 수행합니다.
2. queue1에서 3을 추출하여 queue2에 추가합니다. 그리고 queue2에서 4를 추출하여 queue1에 추가합니다. 그 결과 queue1은 [2, 7, 2, 4], queue2는 [6, 5, 1, 3]가 되며, 각 큐의 원소 합은 15로 같습니다. 이 방법은 작업을 2번만 수행하며, 이보다 적은 횟수로 목표를 달성할 수 없습니다.

따라서 각 큐의 원소 합을 같게 만들기 위해 필요한 작업의 최소 횟수는 2입니다.

길이가 같은 두 개의 큐를 나타내는 정수 배열 queue1, queue2가 매개변수로 주어집니다. 각 큐의 원소 합을 같게 만들기 위해 필요한 작업의 최소 횟수를 return 하도록 solution 함수를 완성해주세요. 단, 어떤 방법으로도 각 큐의 원소 합을 같게 만들 수 없는 경우, -1을 return 해주세요.

## [제한사항]
* 1 ≤ queue1의 길이 = queue2의 길이 ≤ 300,000
* 1 ≤ queue1의 원소, queue2의 원소 ≤ 109
* 주의: 언어에 따라 합 계산 과정 중 산술 오버플로우 발생 가능성이 있으므로 long type 고려가 필요합니다.

## 입출력 예:

| queue1 	| queue2 	| result 	|
|---	|---	|---	|
| [3, 2, 7, 2] 	| [4, 6, 5, 1] 	| 2 	|
| [1, 2, 1, 2] 	| [1, 10, 1, 2] 	| 7 	|
| [1, 1] 	| [1, 5] 	| -1 	|

## 입출력 예 설명:
### 입출력 예 #1:

문제 예시와 같습니다.

### 입출력 예 #2:

두 큐에 담긴 모든 원소의 합은 20입니다. 따라서, 각 큐의 합을 10으로 만들어야 합니다. queue2에서 1, 10을 순서대로 추출하여 queue1에 추가하고, queue1에서 1, 2, 1, 2와 1(queue2으로부터 받은 원소)을 순서대로 추출하여 queue2에 추가합니다. 그 결과 queue1은 [10], queue2는 [1, 2, 1, 2, 1, 2, 1]가 되며, 각 큐의 원소 합은 10으로 같습니다. 이때 작업 횟수는 7회이며, 이보다 적은 횟수로 목표를 달성하는 방법은 없습니다. 따라서 7를 return 합니다.

### 입출력 예 #3:

어떤 방법을 쓰더라도 각 큐의 원소 합을 같게 만들 수 없습니다. 따라서 -1을 return 합니다.

<br>

<hr>

## 피드백: 
* deque를 활용할 생각은 빨리했으나, queue1+queue2로 합친 다음deque.rotate() 를 하며 sum(deque[slice]))로 비교하려고 했다
* 결국 pop을 사용하되, 두개의 리스트중 하나만 합이 전체합/2 를 충족시키게 했다
	* 한 리스트만 조건 충족을 확인하면 나머지 리스트가 조건을 충족못할수도 있지 않나?
		* => 없는것같다..
	* 만약 두 리스트의 합이 홀수인 경우 -1이 나와야 해서 if 문을 하나 더 추가해야하지않을까....?하고 추가해 보았다 (추가 안해도 통과하긴 한다)
	* ps) 원소 조건이 $$1 ≤ 원소 ≤ 10^9 
	$$이라 유리수도 포함해야하나,,,,,,싶었지만 머리아파서 그만둔다,,
	* 추가) 그냥 //를 / 로 바꿔주면 if 문 없이도 유리수까지 해결된다!


<br>

## 코드설명:

*  deque의 popleft()함수 활용
*   한개의 리스트를 기준으로 전체 리스트의 합의 반과 같을떄까지 popleft()해준다
*   두개의 리스트중 한개라도 원소가 남아있지 않다면 -1 리턴

## 코드:

```python
from collections import deque

def solution(queue1, queue2):
    target_sum = (sum(queue1) + sum(queue2)) / 2

    ## 두 리스트의 합이 홀수인 경우 -1
    ##if target_sum.is_integer() == False:
    ##    return -1
    left_sum = sum(queue1)
    queue1 = deque(queue1)
    queue2 = deque(queue2)

    answer = 0
    while queue1 and queue2:
        if left_sum < target_sum:
            tmp = queue2.popleft()
            left_sum += tmp
            queue1.append(tmp)
            answer += 1
        elif left_sum > target_sum:
            left_sum -= queue1.popleft()
            answer += 1
        else:
            return answer

    else:
        return -1

```

## 우수답변자 코드:

```python

from collections import deque

def solution(queue1, queue2):
    answer = 0
    total = (sum(queue1) + sum(queue2))

    if total % 2 != 0:
        return -1

    total //= 2

    q1, q2 = deque(queue1), deque(queue2)
    q1_sum, q2_sum = sum(queue1), sum(queue2)

    while answer <= 600000: # 두개의 큐 최대 길이만큼 탐색
        if q1_sum == q2_sum:
            return answer
        elif q1_sum < q2_sum:
            q2_front = q2.popleft()
            q2_sum -= q2_front
            q1_sum += q2_front
            q1.append(q2_front)
        else:
            q1_front = q1.popleft()
            q1_sum -= q1_front
            q2_sum += q1_front
            q2.append(q1_front)

        answer += 1

    return -1
```

## 우수답변자2 코드:
```python
from collections import deque
def solution(queue1, queue2):
    queue1_sum = sum(queue1)
    queue2_sum = sum(queue2)
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    for i in range(4 * len(queue1) + 1):
        if queue1_sum > queue2_sum:
            x = queue1.popleft()
            queue1_sum -= x
            queue2_sum += x
            queue2.append(x)
        elif queue1_sum < queue2_sum:
            x = queue2.popleft()
            queue2_sum -= x
            queue1_sum += x
            queue1.append(x)
        else:
            return i
    return -1
```

## 우수답변자3 코드:
```python
from collections import deque

def solution(queue1, queue2):
    answer = 0
    count = len(queue1) + len(queue2) + 2

    queue1_sum = sum(queue1)
    queue2_sum = sum(queue2)

    q1 = deque(queue1)
    q2 = deque(queue2)

    temp = True

    while True:
        if count < 0 or not q1 or not q2:
            temp = False
            break

        if queue1_sum == queue2_sum:
            break

        elif queue1_sum > queue2_sum:
            data = q1.popleft()
            q2.append(data)

            queue1_sum -= data
            queue2_sum += data

        else:
            data = q2.popleft()
            q1.append(data)

            queue1_sum += data
            queue2_sum -= data
        answer += 1
        count -= 1

    if temp == False:
        answer = -1

    return answer
```

