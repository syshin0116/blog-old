---
layout: post
title: "[lvl3][동적계획법(Dynamic Programming)]정수 삼각형"
date: 2023-05-01 10:31:29 +0900
categories: [Code-Test, Programmers]
tags: [lvl3, programmers, python]
---

출처: [Programmers > 코딩테스트 연습 > 연습문제 > 동적계획법(Dynamic Programming) > 정수 삼각형"](https://school.programmers.co.kr/learn/courses/30/lessons/43105)

## 문제 설명:

![img](https://user-images.githubusercontent.com/99532836/235447519-bf03dceb-2564-4962-91d2-18e74dc7b525.png)

위와 같은 삼각형의 꼭대기에서 바닥까지 이어지는 경로 중, 거쳐간 숫자의 합이 가장 큰 경우를 찾아보려고 합니다. 아래 칸으로 이동할 때는 대각선 방향으로 한 칸 오른쪽 또는 왼쪽으로만 이동 가능합니다. 예를 들어 3에서는 그 아래칸의 8 또는 1로만 이동이 가능합니다.

삼각형의 정보가 담긴 배열 triangle이 매개변수로 주어질 때, 거쳐간 숫자의 최댓값을 return 하도록 solution 함수를 완성하세요.

### 제한 사항
* 삼각형의 높이는 1 이상 500 이하입니다.
* 삼각형을 이루고 있는 숫자는 0 이상 9,999 이하의 정수입니다.

	
### 입출력 예

| triangle                                                | result |
|---------------------------------------------------------|--------|
| [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]] | 30     |


<br>

<hr>

## 피드백: 
* 재귀함수 생각하느라 너무 오래걸렷다..

<br>

## 코드 설명:
* 재귀함수 
	
## 코드:

```python
def solution(triangle):
    memo = {}
    answer = f(triangle, 0, 0, memo)
    return answer

def f(triangle, i, j, memo):
    if i == len(triangle)-1:
        return triangle[i][j]

    if (i,j) in memo:
        return memo[(i,j)]

    a = f(triangle, i+1, j, memo)
    b = f(triangle, i+1, j+1, memo)
    x = triangle[i][j] + max(a, b)

    memo[(i,j)] = x

    return x

```

## 우수답변자1 코드:

```python
solution = lambda t, l = []: max(l) if not t else solution(t[1:], [max(x,y)+z for x,y,z in zip([0]+l, l+[0], t[0])])

```

## 우수답변자2 코드:
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

## 우수답변자3 코드:
```python
def solution(triangle):

    height = len(triangle)

    while height > 1:
        for i in range(height - 1):
            triangle[height-2][i] += max([triangle[height-1][i], triangle[height-1][i+1]])
        height -= 1

    answer = triangle[0][0]
    return answer
```
