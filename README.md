# 🚀 Day 4 - Tool Calling Agent

This project is part of the Generative & Agentic AI Bootcamp by Nunnari Academy.

## 📌 Objective
To understand how AI agents use tools by implementing a simple tool-calling system using Python.


## 🛠️ Tools Implemented

1. **web_search(query: str)**  
   - Simulates fetching latest information from the web.

2. **summarize(text: str)**  
   - Generates a short summary of the given text.

3. **notes(text: str)**  
   - Converts text into structured notes format with Title and Content.

## ⚙️ How It Works

- The agent receives a user query.
- Based on the query, it decides which tool to use.
- It executes the tool and prints the output.
- Supports multi-step tool calling (e.g., search + summarize).


## 🧠 Agent Logic

- If query contains **"latest" or "news"** → uses `web_search`
- If query contains **"summarize"** → uses `summarize`
- If query contains both → performs **tool chaining**
- If query contains **"notes"** → uses `notes`

---

## ▶️ How to Run

```bash
python day4_tool_calling.py
