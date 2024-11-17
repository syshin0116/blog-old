---
layout: post
title: Modular RAG - Chat History
date: 2024-11-17 14:35 +0900
categories:
  - Project
  - Modular RAG
tags: 
math: true
---

## 효율적인 Chat History 저장과 확장 가능한 구조 설계

챗봇을 설계하다, 기본적인 채팅 기록 저장 방식에 대해 고민하게 되었다. 일반적으로 채팅 기록을 저장하는 방법은 **Chat Session**과 **Chat Messages**로 나눌 수 있다. 기본적인 저장 방식에 추가로 고려한 기능, 이를 구현하기 위한 구조, 그리고 일반적인 챗봇과 카카오톡 봇 모두에 적합한 설계를 정리해 보았다.


### 기본적인 Chat History 저장 방법
#### 1. Chat Session
• 채팅 세션 단위로 저장
• 각 세션은 시작 시간, 참여자, 그리고 채팅방에 대한 내용을 포함
• ex) 사용자와 봇 간의 대화는 하나의 세션으로 기록

#### 2. Chat Messages
• 각 메시지를 독립적으로 저장
• 메시지는 대화의 흐름을 기록하며, 발신자(사용자 또는 봇), 내용, 타임스탬프 등의 정보를 기록
• 세션 ID를 외래 키로 사용해, 각 메시지가 어떤 세션에 속해 있는지 명확히 연결

### 추가 기능

기본적인 저장 방식 외에도, 효율적이고 확장 가능한 구조를 위해 다음과 같은 기능을 추가하고 싶었다.

#### 1. 메타데이터 관리

• 각 세션에 메타데이터를 추가하여 요약, 중요 정보, 일정, 준비물 등을 저장할 수 있도록 설계
	• ex) 대화 중 중요한 일정이 언급되면 이를 자동으로 추출해 메타데이터에 추가

#### 2. 요약 기능

• 메시지가 많아질 경우, 이전 메시지를 요약해 세션에 저장하여 대화 기록을 간결하게 관리
• 요약은 세션의 메타데이터로 저장되며, 필요할 때 이를 참조

#### 3. 기억 기능

• 사용자가 특정 정보를 기억해 달라고 요청할 경우, 이를 메타데이터에 추가하여 후속 대화에서 활용할 수 있도록 기록
	• ex) “내가 22일에 회의가 있다고 했지?“라는 질문에 대답할 수 있도록 저장된 정보를 활용

## 구현을 위한 DB 테이블 구조

### Chat Session

```python
class ChatSession(Base):
    __tablename__ = "chat_sessions"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid4()))
    user_id = Column(String(36), ForeignKey("users.id", ondelete="CASCADE"), nullable=True)
    description = Column(JSON, nullable=True)  # 대화 세션에 대한 간단 정보
    metadata = Column(JSON, nullable=True)  # 일정, 준비물, 중요 정보 등 추가 정보
    start_time = Column(DateTime(timezone=True), server_default=func.now())
```

> metadata 필드에 다수의 일정과 관련 데이터를 저장할 수 있도록 설계

#### 사용 사례

#### 대화 내용

```
User: 우리 22일에 프로젝트 발표 있어.
Bot: 프로젝트 발표를 일정에 추가할게요. 장소는 어디인가요?
User: 회의실 1이야.
Bot: 알겠습니다. 준비물이나 역할을 추가하시겠어요?
User: 발표 자료는 내가 준비하고, 회의실 예약은 김팀장님이 맡아줘.
```

#### 메타데이터 저장 정보

```JSON
{
  "schedules": [
    {
      "id": "schedule1",
      "title": "프로젝트 발표",
      "date": "2024-11-22",
      "time": "10:00",
      "location": "회의실 1",
      "tasks": [
        {
          "name": "프레젠테이션 자료 준비",
          "type": "preparation",
          "assigned_to": "user1"
        },
        {
          "name": "회의실 예약",
          "type": "role",
          "assigned_to": "김팀장"
        }
      ]
    }
  ]
}
```

> 고려사항: 다수의 일정과 관련 데이터를 metadata로 충분히 관리할 수 있다. 다만, 데이터가 매우 많아지거나 일정/준비물 중심의 대규모 처리가 필요해지면 테이블 분리를 고려해야 한다. 
### Chat Messages

```python
class ChatMessage(Base):
    __tablename__ = "chat_messages"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid4()))
    session_id = Column(String(36), ForeignKey("chat_sessions.id", ondelete="CASCADE"), nullable=False)
    sender_type = Column(Enum(MessageSenderType), nullable=False)  # USER 또는 BOT
    sender = Column(Text, nullable=False)  # 발신자 이름 또는 ID
    content = Column(Text, nullable=False)  # 메시지 내용
    timestamp = Column(DateTime(timezone=True), server_default=func.now())
```


### Chat Summary

위 중요사항들과 같이 metadata에 간단하게 저장할 수 있지만, chat summary의 경우는 모든 챗에 적용할 수 있기에 테이블로 따로 구현하였다.

```python
class ChatSummary(Base):
    __tablename__ = "chat_summaries"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid4()))
    session_id = Column(String(36), ForeignKey("chat_sessions.id", ondelete="CASCADE"), nullable=False)
    start_time = Column(DateTime(timezone=True), nullable=False)  # 요약 시작 시간
    end_time = Column(DateTime(timezone=True), nullable=False)    # 요약 종료 시간
    content = Column(Text, nullable=False)  # 요약 내용
    created_at = Column(DateTime(timezone=True), server_default=func.now())  # 요약 생성 시간
```


#### 요약 함수 예시

```python
def summarize_chat(session_id, message_limit=100):
    # 세션에 연결된 메시지 가져오기
    messages = db.query(ChatMessage).filter(ChatMessage.session_id == session_id).order_by(ChatMessage.timestamp).all()
    
    if len(messages) >= message_limit:
        # 요약 대상 메시지 선택
        messages_to_summarize = messages[:message_limit]
        
        # 요약 내용 생성
        summary_content = " ".join([msg.content for msg in messages_to_summarize])
        summary_content = summarize_text(summary_content)  # 요약 알고리즘 적용

        # 요약 데이터 저장
        summary = ChatSummary(
            session_id=session_id,
            start_time=messages_to_summarize[0].timestamp,
            end_time=messages_to_summarize[-1].timestamp,
            content=summary_content,
        )
        db.add(summary)
        
        # 기존 메시지 삭제 또는 플래그 업데이트
        for msg in messages_to_summarize:
            db.delete(msg)  # 또는 msg.is_summarized = True
        db.commit()
```


#### 데이터 흐름 요약
1. **채팅 메시지 저장**: 새로운 메시지가 들어오면 ChatMessage에 저장.
2. **요약 조건 확인**:  메시지 수가 일정 개수를 초과하거나 시간이 경과하면 요약 생성
3. **요약 데이터 저장**: 별도 테이블(ChatSummary)에 저장하거나 ChatSession.metadata에 누적
4. **원본 메시지 관리**: 요약된 메시지는 삭제하거나 플래그로 처리해 데이터 크기 최소화

