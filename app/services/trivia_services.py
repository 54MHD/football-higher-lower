import random

from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.db import Question
from app.schema import (
    CountResponse,
    QuestionOut,
    RandomQuestionResponse,
    RandomQuestionsResponse,
    TriviaVerifyRequest,
    TriviaVerifyResponse,
)


class TriviaService:
    @staticmethod
    async def get_random_question(
        session: AsyncSession,
        exclude_ids: list[int] | None = None,
    ) -> RandomQuestionResponse:
        query = select(Question)
        if exclude_ids:
            query = query.where(~Question.id.in_(exclude_ids))
        query = query.order_by(func.random()).limit(1)
        result = await session.execute(query)
        question = result.scalar()

        if question is None:
            raise ValueError("No questions in the database")

        return RandomQuestionResponse(
            question=TriviaService._to_question_out(question)
        )

    @staticmethod
    async def get_random_questions(
        session: AsyncSession,
        limit: int = 20,
    ) -> RandomQuestionsResponse:
        query = select(Question).order_by(func.random()).limit(limit)
        result = await session.execute(query)
        questions = result.scalars().all()

        if not questions:
            raise ValueError("No questions in the database")

        return RandomQuestionsResponse(
            questions=[TriviaService._to_question_out(q) for q in questions]
        )

    @staticmethod
    async def get_question_count(session: AsyncSession) -> CountResponse:
        result = await session.execute(select(func.count()).select_from(Question))
        total = result.scalar_one()
        game_limit = 20
        return CountResponse(total_questions=min(total, game_limit))

    @staticmethod
    async def verify_answer(session: AsyncSession, payload: TriviaVerifyRequest) -> TriviaVerifyResponse:
        result = await session.execute(select(Question).where(Question.id == payload.question_id))
        question = result.scalar()

        if question is None:
            raise ValueError("Question not found")

        correct = payload.selected_answer.upper() == question.correct_answer

        return TriviaVerifyResponse(
            correct=correct,
            correct_answer=question.correct_answer,
            explanation=f"The correct answer is {question.correct_answer}."
        )

    @staticmethod
    def _to_question_out(question: Question) -> QuestionOut:
        return QuestionOut(
            id=question.id,
            question_text=question.question_text,
            option_a=question.option_a,
            option_b=question.option_b,
            option_c=question.option_c,
            option_d=question.option_d,
            difficulty=question.difficulty,
            category=question.category,
        )
