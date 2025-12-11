from typing import List, Literal

from pydantic import BaseModel, Field


class PlayerOut(BaseModel):
    id: int
    name: str
    image_url: str
    stat_value: int


class RandomPlayersResponse(BaseModel):
    players: List[PlayerOut]


class VerifyRequest(BaseModel):
    player_left_id: int = Field(..., ge=1)
    player_right_id: int = Field(..., ge=1)
    guess: Literal["left", "right"]


class VerifyResponse(BaseModel):
    correct: bool
    left_value: int
    right_value: int


class QuestionOut(BaseModel):
    id: int
    question_text: str
    option_a: str
    option_b: str
    option_c: str
    option_d: str
    difficulty: str
    category: str


class RandomQuestionResponse(BaseModel):
    question: QuestionOut

class RandomQuestionsResponse(BaseModel):
    questions: List[QuestionOut]


class TriviaVerifyRequest(BaseModel):
    question_id: int = Field(..., ge=1)
    selected_answer: str = Field(..., min_length=1, max_length=1)


class TriviaVerifyResponse(BaseModel):
    correct: bool
    correct_answer: str
    explanation: str


class HealthResponse(BaseModel):
    status: str


class CountResponse(BaseModel):
    total_questions: int
