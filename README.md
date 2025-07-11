# 🤖 Inquiro – Agentic AI Assistant

Inquiro is a modular **Agentic AI chatbot** built with [LangGraph](https://github.com/langchain-ai/langgraph), [Groq LLMs](https://console.groq.com/), and [Streamlit](https://streamlit.io/). It supports basic chat, web-augmented conversations, and real-time **AI news summarization**, offering a dynamic interface for both users and developers to explore the capabilities of LLM-driven agents.

---

## 🚀 Features

- 🧠 **Basic Chatbot** – Chat with Groq LLMs in an interactive UI.
- 🌐 **Web-Augmented Chatbot** – Retrieve live search results via [Tavily](https://www.tavily.com/).
- 📰 **AI News Explorer** – Fetch and summarize trending AI news into clean, readable markdown.
- 📊 **Graph-Based Design** – Flexible LangGraph architecture for easy feature expansion.
- 🔐 **Secure API Key Input** – API keys handled safely via Streamlit sidebar inputs.

---

## 📸 Demo Video


[streamlit-app-2025-07-12-01-07-22.webm](https://github.com/user-attachments/assets/a81f0653-2c0a-4388-8f00-b4b85882d5c5)

---

## 🛠️ Tech Stack

| Tool / Library        | Purpose                              |
|-----------------------|--------------------------------------|
| LangChain + LangGraph | Orchestrating LLM logic via graphs  |
| Groq LLMs             | Lightning-fast chat responses        |
| Tavily                | Real-time web search API             |
| Streamlit             | UI interface                        |
| FAISS                 | (Planned) for vector search/memory   |

---
## 📂 Project Structure:

Agentic-Chatbot/
├── app.py
├── requirements.txt
├── AINews/                     
├── src/
│   └── langgraphagenticai/
│       ├── main.py             
│       ├── ui/
│       │   ├── streamlitui/
│       │   │   ├── loadui.py            
│       │   │   └── display_results.py   
│       │   └── uiconfigfile.py          
│       ├── LLMS/
│       │   └── groqllm.py               
│       ├── graph/
│       │   └── graphbuilder.py         
│       ├── nodes/
│       │   ├── basicchatbotnode.py      
│       │   ├── chatbotwithweb.py        
│       │   └── ainewsnode.py            
│       └── state/
│           └── State.py                 

---
## 👤 Author
### Pranav Vashisth
📧 Email: pvashisth0711@gmail.com
🔗 LinkedIn: linkedin.com/in/pranav-vashisth

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/pvashisth-07/Agentic-Chatbot.git
cd Agentic-Chatbot

