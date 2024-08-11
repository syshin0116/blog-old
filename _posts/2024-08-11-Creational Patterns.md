---
layout: post
title: Creational Patterns
date: 2024-08-11 15:51 +0900
categories:
  - 스터디
  - Design Pattern
tags: 
math: true
---

## Abstract Factory

![](https://i.imgur.com/MFN6ace.png)

### Abstract Factory란?
- 패턴은 관련이 있거나 의존적인 객체들의 가족을 생성하기 위한 인터페이스를 제공하는 생성 패턴
- 패턴은 구체적인 클래스에 의존하지 않고 객체의 가족을 생성하기 용이
- 서로 관련된 객체들을 하나의 주제나 개념으로 묶어 생성


![](https://i.imgur.com/CRw1AX6.png)


### 장점
- 관련 제품군 생성: 관련 제품(또는 객체)들을 하나의 가족으로 캡슐화하여, 가족 내 제품들이 서로 잘 협력할 수 있도록 함

- 제품 호환성 보장: 팩토리를 통해 제품을 생성함으로써 생성된 객체들이 서로 호환될 수 있도록 보장

- 제품 가족 전환의 용이성: 런타임 시 팩토리 객체를 변경함으로써 제품 가족을 쉽게 교체할 수 있어, 클라이언트 코드를 수정하지 않고도 전체 제품 세트를 교체에 용이


### Abstract Factory vs Factory Method

- Factory Method: 조건에 따른 생성을 팩토리 클래스로 위임하여, 팩토리 클래스에서 객체를 생성하는 패턴
- Abstract Factory: 서로 관련이 있는 개체들을 통째로 묶어서 팩토리 클래스로 만들고, 이들 팩토리를 조건에 따라 생성하도록 다시 팩토리를 만들어서 객체를 생성하는 패턴


### 코드
```python
from __future__ import annotations
from abc import ABC, abstractmethod


class AbstractFactory(ABC):
    """
    The Abstract Factory interface declares a set of methods that return
    different abstract products. These products are called a family and are
    related by a high-level theme or concept. Products of one family are usually
    able to collaborate among themselves. A family of products may have several
    variants, but the products of one variant are incompatible with products of
    another.
    """

    @abstractmethod
    def create_iphone(self) -> AbstractProductIphone:
        pass

    @abstractmethod
    def create_galaxy(self) -> AbstractProductGalaxy:
        pass


class AppleFactory(AbstractFactory):

    def create_iphone(self) -> AbstractProductIphone:
        return Iphone15Pro()

    def create_galaxy(self) -> AbstractProductGalaxy:
        raise NotImplementedError("AppleFactory does not create Galaxy products.")


class SamsungFactory(AbstractFactory):
    def create_galaxy(self) -> AbstractProductGalaxy:
        return GalaxyS24()

    def create_iphone(self) -> AbstractProductIphone:
        raise NotImplementedError("SamsungFactory does not create iPhone products.")


class AbstractProductIphone(ABC):

    @abstractmethod
    def applepay(self) -> str:
        pass


class AbstractProductGalaxy(ABC):

    @abstractmethod
    def samsungpay(self) -> str:
        pass


class Iphone15Pro(AbstractProductIphone):
    def applepay(self) -> str:
        return "애플페이"


class GalaxyS24(AbstractProductGalaxy):
    def samsungpay(self) -> str:
        return "삼성페이"


def client_code(factory: AbstractFactory) -> None:
    """
    The client code works with factories and products only through abstract
    types: AbstractFactory and AbstractProduct. This lets you pass any factory
    or product subclass to the client code without breaking it.
    """
    try:
        product_a = factory.create_iphone()
        print(f"{product_a.applepay()}")
    except NotImplementedError as e:
        print(e)

    try:
        product_b = factory.create_galaxy()
        print(f"{product_b.samsungpay()}")
    except NotImplementedError as e:
        print(e)


if __name__ == "__main__":
    client_code(AppleFactory())
    client_code(SamsungFactory())

```





## Singleton

![](https://i.imgur.com/vjX1HWH.png)


### Singleton이란?
- 전역 변수를 사용하지 않고 객체를 하나만 생성
- 생성된 객체를 어디에서든지 참조할 수 있도록 하는 패턴




### 장점
- 단 한개의 인스턴스를 보장
- 어디에서든 참조 가능


#### 메타클래스란?
- 메타클래스(metaclass)는 클래스의 행동을 정의하는 데 사용되는 클래스
- 파이썬에서 클래스는 객체로 간주되며, 메타클래스는 이러한 클래스의 생성 및 초기화를 제어할 수 있는 특수한 클래스
- 기본적으로 클래스는 type이라는 메타클래스로 생성되며, type은 클래스를 생성하는 데 사용되는 내장 메타클래스이다


### 코드
#### 1. 메타클래스 사용  Singleton 구현
```python
### 메타데이터 사용 방법
class SingletonMeta(type):
    """
    The Singleton class can be implemented in different ways in Python. Some
    possible methods include: base class, decorator, metaclass. We will use the
    metaclass because it is best suited for this purpose.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):
    def some_business_logic(self):
        """
        Finally, any singleton should define some business logic, which can be
        executed on its instance.
        """

        # ...


if __name__ == "__main__":
    # The client code.

    s1 = Singleton()
    s2 = Singleton()

    if id(s1) == id(s2):
        print("Singleton works, both variables contain the same instance.")
    else:
        print("Singleton failed, variables contain different instances.")

```

#### 2. 클래스 사용 Singleton 구현

```python

class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def some_logic(self):
        pass

```


#### 3. Decorator 사용 Singleton 구현


```python
def singleton(cls):
    instances = {}

    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance


@singleton
class Singleton:
    def some_logic(self):
        pass


# 사용 예
s1 = Singleton()
s2 = Singleton()

if id(s1) == id(s2):
    print("Singleton works, both variables contain the same instance.")
else:
    print("Singleton failed, variables contain different instances.")

```



