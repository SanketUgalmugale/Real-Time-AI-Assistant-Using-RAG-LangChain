# Try to import ChatOllama from different locations
ChatOllama = None
Ollama = None

try:
    from langchain_ollama import ChatOllama
except ImportError:
    try:
        from langchain_community.chat_models import ChatOllama
    except ImportError:
        try:
            from langchain_community.llms import Ollama
            print("⚠️ Warning: Using deprecated Ollama. Please install langchain-ollama for better support.")
        except ImportError:
            raise ImportError("Please install langchain-ollama or langchain-community")

from langchain_community.tools import DuckDuckGoSearchRun
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough

# We specify the model we pulled in Step 1
if ChatOllama is not None:
    llm = ChatOllama(model="llama3:8b")
elif Ollama is not None:
    llm = Ollama(model="llama3:8b")
else:
    raise ImportError("Could not import ChatOllama or Ollama. Please install required packages.")

# This tool will run a web search
search = DuckDuckGoSearchRun()

# This is the prompt template, our instruction manual for the LLM
prompt = ChatPromptTemplate.from_template(
    """You are a helpful AI assistant. You must answer the user's question 
    based *only* on the following search results. If the search results 
    are empty or do not contain the answer, say 'I could not find 
    any information on that.'

    Search Results:
    {context}

    Question:
    {question}
    """
)

# This is our RAG chain
chain = (
    RunnablePassthrough.assign(
        # "context" is a new key we add to the dictionary.
        # Its value is the *output* of running the 'search' tool
        # with the original 'question' as input.
        context=lambda x: search.run(x["question"])
    )
    | prompt  # The dictionary (now with 'context' and 'question') is "piped" into the prompt
    | llm     # The formatted prompt is "piped" into the LLM
)

print("🤖 Hello! I'm a real-time AI assistant. What's new?")
while True:
    try:
        user_query = input("You: ")
        if user_query.lower() in ["exit", "quit"]:
            print("🤖 Goodbye!")
            break
        
        if not user_query.strip():
            continue
        
        print("🤖 Thinking...")
        
        # This one line runs the whole RAG process
        response = chain.invoke({"question": user_query})
        
        # Extract content from the response (handles both AIMessage and string responses)
        if hasattr(response, 'content'):
            response_content = response.content
        elif isinstance(response, str):
            response_content = response
        else:
            response_content = str(response)
        
        print(f"🤖: {response_content}")

    except KeyboardInterrupt:
        print("\n🤖 Goodbye!")
        break
    except Exception as e:
        print(f"❌ An error occurred: {e}")

