---
layout: post
title: Behavior Patterns
date: 2024-08-11 17:50 +0900
categories:
  - 스터디
  - Design Pattern
tags: 
math: true
---

## Iterator(반복자 패턴)


### Iterator이란?

- 컬렉션의 요소들의 기본 표현(리스트, 스택, 트리 등)을 노출하지 않고 하나씩 순회


![](https://i.imgur.com/nkBMQIh.png)


### 장점
- 단일 책임 원칙: 부피가 큰 순회 알고리즘들을 별도의 클래스들로 추출하여 클라이언트 코드와 컬렉션들을 정돈할 수 있다
-  개방/폐쇄 원칙: 새로운 유형의 컬렉션들과 반복자들을 구현할 수 있으며 이들을 아무것도 훼손하지 않은 체 기존의 코드에 전달할 수 있다



### 코드

```python
class Node:
    """
    이진 트리의 노드를 나타내는 클래스
    """

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    """
    이진 트리 클래스로, 노드를 추가하고 순회하는 기능을 제공
    """

    def __init__(self, root):
        self.root = root

    def __iter__(self):
        return InOrderIterator(self.root)


class InOrderIterator:
    """
    중위 순회를 위한 이터레이터
    """

    def __init__(self, root):
        self.stack = []
        self._push_left(root)

    def _push_left(self, node):
        while node:
            self.stack.append(node)
            node = node.left

    def __next__(self):
        if not self.stack:
            raise StopIteration
        node = self.stack.pop()
        result = node.value
        if node.right:
            self._push_left(node.right)
        return result


# 사용 예시
root = Node(10)
root.left = Node(5)
root.right = Node(15)
root.left.left = Node(2)
root.left.right = Node(7)
root.right.right = Node(20)

tree = BinaryTree(root)

print("이진 트리 중위 순회:")
for value in tree:
    print(value)

```