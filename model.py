from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
load_dotenv()

model = init_chat_model(
    "openai//gpt-4o-mini",
    model_provider="openrouter"
)

result = model.invoke("What is a model in GenAI in one sentence?")

print(result.content)