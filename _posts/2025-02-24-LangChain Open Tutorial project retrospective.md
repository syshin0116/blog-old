---
layout: post
title: "[LangChain Open Tutorial]Project retrospective"
date: 2025-02-27 23:54 +0900
categories:
  - Project
  - LangChain Open Tutorial
tags: 
math: true
---
## Background

I recently came across the news that **TeddyNote**, a YouTuber I follow, was recruiting contributors for the **LangChain open-source tutorial** on **Retrieval-Augmented Generation (RAG)**—a topic I was particularly interested in. This was an exciting opportunity, not just as a fan, but as a chance to **actively contribute to a topic I’m passionate about**. Since it was my first time participating in a large-scale open-source project and collaborating with various contributors, I was even more eager to take part.

The tutorial contribution process lasted about **seven weeks**, during which the project saw **over 2,000 commits**, reflecting its high level of activity. In the first week, all contributors focused on reviewing and translating existing tutorials. Afterward, I dedicated my time to creating **new tutorials**, taking responsibility for structuring content and implementing code.

GitBook: [🦜️🔗 The LangChain Open Tutorial for Everyone](https://langchain-opentutorial.gitbook.io/langchain-opentutorial)  
GitHub: [LangChain-OpenTutorial](https://github.com/LangChain-OpenTutorial/LangChain-OpenTutorial)

---

## Contributed Tutorials

### **LlamaParse Tutorial**

- **GitBook:** [LlamaParse GitBook](https://langchain-opentutorial.gitbook.io/langchain-opentutorial/06-documentloader/12-llamaparse)
- **GitHub**: [LlamaParse Tutorial Code](https://github.com/LangChain-OpenTutorial/LangChain-OpenTutorial/blob/main/06-DocumentLoader/13-LlamaParse.ipynb)
- **Google Colab**: [Run on Colab](https://colab.research.google.com/github/LangChain-OpenTutorial/LangChain-OpenTutorial/blob/main/06-DocumentLoader/13-LlamaParse.ipynb)

This was the **first tutorial I wrote**, and rather than creating new content, it was more about **reviewing and translating an existing tutorial**. While it was less exciting than other new projects, it was a **valuable hands-on experience** for learning how to write tutorials and understanding the workflow of a large-scale project.

The tutorial covered how to **efficiently parse documents** using **LlamaParse**, a tool provided by **LlamaIndex**. LlamaParse goes beyond simple document loading by supporting **various file formats such as PDF, Word, PowerPoint, and Excel**. It also offers **customizable outputs via natural language commands**, supports **image and table extraction**, and even provides **multilingual processing**.

Document processing plays a crucial role in **LLM-based applications**, and LlamaParse enhances **retrieval and utilization of documents** in **RAG (Retrieval-Augmented Generation)** systems. This tutorial systematically explored **basic document parsing to advanced parsing techniques utilizing multimodal models**.

### **Key Implementation Points**

- **Basic Document Parsing**
    
    - Load PDF files using LlamaParse and convert them into LangChain document objects
    - Unlike basic text extraction, LlamaParse preserves the **document structure**, producing cleaner results
- **Multimodal Model-Based Document Analysis**
    
    - Utilized models like OpenAI’s **GPT-4o** to **analyze images, tables, and graphs** within documents
    - Showcased how to process **both textual and visual elements** in documents
- **Custom Parsing Configuration**
    
    - Used **natural language commands** to tailor output formats to specific needs
    - Implemented features like **extracting only summaries** or **filtering specific sections**
- **Parameter Tuning and Advanced Features**
    
    - Adjusted **LlamaParse’s detailed settings** to optimize document parsing performance
    - Explored **OCR-based image text extraction**, **JSON output formatting**, and more

### **Lessons Learned & Areas for Improvement**

✔ **LLM-powered document processing will become even more powerful**  
Traditional document parsing mostly involved simple **text extraction**. However, LlamaParse considers the **position, context, and meaning of content**, enabling **LLMs to understand documents more comprehensively**.

✔ **Multimodal document processing is promising**  
The ability to analyze **tables, diagrams, and highlighted text** in PDFs and image-based documents was particularly impressive. Future developments in **multimodal AI** will likely move beyond simple text extraction to **leveraging visual elements** for deeper understanding.

✔ **Natural language-based parsing is highly useful**  
The ability to extract data **without complex coding, using natural language commands**, was powerful. However, **for complex output formats, additional post-processing is still required**.

---

### **Conversation Memory Management System Tutorial**

- **GitBook**: [ConversationMemoryManagementSystem GitBook](https://langchain-opentutorial.gitbook.io/langchain-opentutorial/19-cookbook/05-aimemorymanagementsystem/09-conversationmemorymanagementsystem)
- **GitHub**: [Conversation Memory Management System Tutorial Code](https://github.com/LangChain-OpenTutorial/LangChain-OpenTutorial/blob/main/19-Cookbook/07-Agent/15-CoT-basedSmartWebSearch.ipynb)
- **Google Colab**: [Run on Colab](https://colab.research.google.com/github/LangChain-OpenTutorial/LangChain-OpenTutorial/blob/main/19-Cookbook/07-Agent/15-CoT-basedSmartWebSearch.ipynb)

This tutorial covered **how to build an AI chatbot’s conversation memory management system using LangGraph**. The goal was to **help the chatbot maintain context over conversations and generate more natural responses** by **effectively storing, retrieving, and updating memory**.

Many chatbots traditionally generate **responses based solely on immediate input**, but by implementing **memory management, conversations can become more contextual and personalized**.

### **Key Implementation Points**

- **Configuration Class Utilization**
    
    - Set up **user_id, model selection, and runtime parameters** to control conversation flow
    - Ensured each conversation had its own context
- **Short-Term & Long-Term Memory Implementation**
    
    - `upsert_memory`: **Stores or updates user data**
    - `store_memory`: **Reflects new training data or tool call results into memory**
    - `call_model`: **Retrieves memory and calls LLM while maintaining context**
- **Automating Conversation Flow with StateGraph**
    
    - Automatically linked `call_model` and `store_memory` for **seamless memory updates**
    - Allowed dynamic and **context-aware conversations**
- **Using LangGraph Checkpoints**
    
    - Implemented **state-saving and rollback functionality** to restore previous conversation states

### **Lessons Learned & Areas for Improvement**

✔ **Memory significantly enhances chatbot realism**  
The **more refined the memory storage**, the more **natural and user-friendly** chatbot responses became.

✔ **Memory optimization is crucial**  
Storing **too much memory** can degrade **search performance and increase costs**, making **efficient memory management essential**.

✔ **LangGraph exceeded expectations**  
StateGraph allowed for **more flexible and intuitive** state management, making it a **great tool not just for chatbots but for workflow automation as well**.

---

### **CoT-Based Smart Web Search Tutorial**

- **GitHub**: [CoT-Based Smart Web Search Tutorial Code](https://github.com/LangChain-OpenTutorial/LangChain-OpenTutorial/blob/main/19-Cookbook/07-Agent/15-CoT-basedSmartWebSearch.ipynb)
- **Google Colab**: [Run on Colab](https://colab.research.google.com/github/LangChain-OpenTutorial/LangChain-OpenTutorial/blob/main/19-Cookbook/07-Agent/15-CoT-basedSmartWebSearch.ipynb)

This tutorial focused on building a **Chain-of-Thought (CoT)-based smart web search system**. Instead of simple keyword matching, it employed a **Plan-and-Execute QA system** to break complex queries into multiple steps.

By structuring the process into **search → extraction → inference → response generation**, the system could **retrieve and analyze information more effectively**.

### **Lessons Learned & Areas for Improvement**

✔ **Strategic search techniques improve results**  
Rather than simple keyword searches, **planning and executing search strategies** proved highly effective.

✔ **Asynchronous execution boosts efficiency**  
Running multiple search queries simultaneously significantly **improved speed**, but **additional filtering logic was needed to remove noise**.

✔ **LangGraph is highly useful**  
Using LangGraph to automate **search → extraction → response** flows was more powerful than expected.

---

## **Final Thoughts**

Beyond just learning about **LangChain and RAG**, I gained **invaluable experience collaborating on an open-source project**. Through **peer review sessions**, I learned different approaches from other contributors and expanded my technical insights.

More importantly, working on a **large-scale project helped me understand collaboration, documentation, and open-source contribution workflows**. It was a far more enriching experience than I had anticipated, and it has motivated me to continue contributing to open-source projects in the future.