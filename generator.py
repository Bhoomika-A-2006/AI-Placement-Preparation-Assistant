import os

from dotenv import load_dotenv
from langchain_openrouter import ChatOpenRouter

from prompts import interview_prompt, parser

load_dotenv()


def get_llm():

    api_key = os.getenv("OPENROUTER_API_KEY")

    if not api_key:
        raise ValueError("OpenRouter API key not found.")

    model_name = os.getenv(
        "MODEL_NAME",
        "openai/gpt-4o-mini"
    )

    llm = ChatOpenRouter(
        model=model_name,
        api_key=api_key,
        base_url="https://openrouter.ai/api/v1",
        temperature=0.3
    )

    return llm


def generate_interview(
    job_role,
    experience_level,
    difficulty,
    num_questions
):

    llm = get_llm()

    chain = interview_prompt | llm | parser

    response = chain.invoke({

        "job_role": job_role,
        "experience_level": experience_level,
        "difficulty": difficulty,
        "num_questions": num_questions

    })

    return response