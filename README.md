# 🤖 Real-Time Local RAG Assistant


A lightweight, terminal-based AI assistant that combines local LLM inference (using Ollama) with real-time web search (using DuckDuckGo). This project demonstrates how to build a Retrieval-Augmented Generation (RAG) pipeline using LangChain and LCEL.

# ✨ Features
Real-Time Knowledge: Unlike standard LLMs cut off from the internet, this bot fetches live data using DuckDuckGo.

Privacy-First: Runs the LLM (Llama 3) locally on your machine using Ollama.

Modern Architecture: Built using LangChain Expression Language (LCEL) for a clean, declarative pipeline.

Robust Error Handling: Includes fallback import logic to support various versions of LangChain libraries.

# 🛠️ Prerequisites
Before running the code, ensure you have the following installed:

Python 3.9+

Ollama: Download and install from ollama.com.

1. Set up the Model
This project uses llama3:8b by default. Open your terminal and run:

Bash

ollama pull llama3:8b
(Note: If you want to use a different model, simply update the model="llama3:8b" line in the Python script.)

# 📦 Installation
Clone the repository:

Bash 

git clone https://github.com/yourusername/local-rag-assistant.git
cd local-rag-assistant
Create a virtual environment (optional but recommended):

Bash

python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
Install dependencies:

Bash

* pip install langchain langchain-community langchain-ollama duckduckgo-search
🚀 Usage
Ensure Ollama is running: Usually, the Ollama app runs in the background. If not, start it with:

Bash

* ollama serve
* Run the assistant:

Bash

python main.py
Chat: Enter your questions in the terminal. Type exit or quit to stop.

Plaintext

🤖 Hello! I'm a real-time AI assistant. What's new?
You: What is the current stock price of Apple?
🤖 Thinking...
🤖: Based on the search results, the current stock price of Apple (AAPL) is $214.50...
🧠 How It Works
This project uses a RAG (Retrieval-Augmented Generation) pipeline:

Input: User asks a question (e.g., "Who won the game yesterday?").

Retrieval: The DuckDuckGoSearchRun tool searches the web for the query.

Context Injection: The search results are passed into a prompt template via RunnablePassthrough.

Generation: The prompt (containing the user's question + search results) is sent to the local Llama 3 model via Ollama.

Output: The LLM generates a factual answer based only on the provided search context.

# 📂 Code Structure
main.py: Contains the entire application logic.

Import Handling: Tries to import ChatOllama from multiple locations to ensure compatibility.

search: The DuckDuckGo tool instance.

prompt: Instructions telling the AI to use the search results.

chain: The LCEL pipeline connecting the search, prompt, and LLM.

while True: The main interactive loop.

🤝 Contributing
Contributions are welcome! If you'd like to add features like "Chat History" or a GUI, feel free to fork the repo and submit a pull request.
