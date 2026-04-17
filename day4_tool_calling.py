# ==========================================
# DAY 4 - TOOL CALLING (FINAL WORKING CODE)
# ==========================================

print("✅ Script Running...\n")


# ==========================================
# 🔷 TOOLS
# ==========================================

def web_search(query):
    return f"[Web Result] Latest info about '{query}': AI and OpenAI are trending."

def summarize(text):
    return f"[Summary] {text[:60]}..."

def notes(text):
    return f"""
Title: Notes
Content: {text}
"""


# ==========================================
# 🔷 AGENT FUNCTION
# ==========================================

def agent(query):
    print("\n🧠 Query:", query)

    q = query.lower()

    # 🔹 Case 1: Web search
    if "latest" in q or "news" in q:
        print("🔧 Tool Used: web_search")
        result = web_search(query)
        print("📤 Output:", result)

        # 🔹 Bonus: If also needs summarize
        if "summarize" in q:
            print("🔧 Tool Used: summarize")
            result = summarize(result)
            print("📤 Final Output:", result)

    # 🔹 Case 2: Only summarize
    elif "summarize" in q:
        print("🔧 Tool Used: summarize")

        if ":" in query:
            text = query.split(":", 1)[1]
        else:
            text = query

        result = summarize(text)
        print("📤 Output:", result)

    # 🔹 Case 3: Notes
    elif "notes" in q:
        print("🔧 Tool Used: notes")
        result = notes(query)
        print("📤 Output:", result)

    # 🔹 Default
    else:
        print("❌ No tool used")


# ==========================================
# 🔷 RUN TEST CASES
# ==========================================

if __name__ == "__main__":

    agent("What is the latest news on OpenAI?")

    agent("Summarize this: AI is growing fast in many industries like healthcare and finance.")

    agent("Find the latest news on AI agents and summarize it")