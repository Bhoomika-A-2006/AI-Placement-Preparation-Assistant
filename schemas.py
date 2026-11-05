
from pydantic import BaseModel, Field
from typing import List, Literal


# ==================================================
# INTERVIEW QUESTION SCHEMA
# ==================================================

class InterviewQuestion(BaseModel):

    question: str = Field(
        ...,
        min_length=10,
        description=(
            "Practical, interview-oriented technical question "
            "specific to the selected job role."
        )
    )

    question_type: Literal[
        "Scenario-based",
        "Coding",
        "Debugging",
        "Conceptual",
        "Comparison",
        "Problem-solving"
    ] = Field(
        description="Category of the interview question."
    )

    difficulty: Literal[
        "Easy",
        "Medium",
        "Hard"
    ] = Field(
        description="Difficulty level of the question."
    )

    model_answer: str = Field(
        ...,
        min_length=20,
        description=(
            "Detailed, technically accurate, interview-ready "
            "answer with reasoning and implementation details."
        )
    )

    explanation: str = Field(
        ...,
        min_length=10,
        description=(
            "Simple conversational explanation using relatable "
            "examples, practical situations and why the concept "
            "is useful."
        )
    )

    practical_example: str = Field(
        ...,
        min_length=5,
        description=(
            "A small real-world or code example illustrating "
            "the concept."
        )
    )

    keywords: List[str] = Field(
        ...,
        min_length=3,
        max_length=8,
        description=(
            "Three to eight important technical keywords "
            "related to the question."
        )
    )

    follow_up: str = Field(
        ...,
        min_length=10,
        description=(
            "One challenging follow-up question that tests "
            "deeper technical understanding."
        )
    )


# ==================================================
# COMPLETE INTERVIEW RESPONSE SCHEMA
# ==================================================

class InterviewResponse(BaseModel):

    job_role: str = Field(
        ...,
        description="Selected technical job role."
    )

    experience_level: str = Field(
        ...,
        description="Candidate's selected experience level."
    )

    questions: List[InterviewQuestion] = Field(
        ...,
        min_length=1,
        description=(
            "List of generated technical interview questions."
        )
    )
