# Football Games - Project Update

## Overview
Your football project has been upgraded with a new **Football Trivia Game**! Now users can choose between two games:
1. **Higher or Lower** - Compare player statistics
2. **Football Trivia** - Answer multiple-choice questions

## New Features Added

### 1. Football Trivia Game
A new interactive trivia game where users answer football-related questions with multiple choices (A, B, C, D).

**Features:**
- Random questions from database
- Multiple difficulty levels (easy, medium, hard)
- Category-based questions
- Score tracking
- Streak counter (resets on wrong answer)
- Immediate feedback with correct answer display
- Beautiful UI with Tailwind CSS

### 2. Updated Database Schema
Added a new `Question` table to store trivia questions:
```python
class Question(Base):
    id: Integer (primary key)
    question_text: String(500)
    option_a: String(200)
    option_b: String(200)
    option_c: String(200)
    option_d: String(200)
    correct_answer: String(1)  # 'A', 'B', 'C', or 'D'
    difficulty: String(20)      # 'easy', 'medium', 'hard'
    category: String(50)        # e.g., 'Premier League', 'World Cup'
```

### 3. New API Endpoints
```
GET /trivia                      - Serves the trivia game page
GET /api/trivia/question         - Get a random question
POST /api/trivia/verify          - Verify the user's answer
```

### 4. Game Selection Menu
The homepage (`index.html`) has been completely redesigned to show both games as cards:
- **Higher or Lower** card with emerald theme
- **Football Trivia** card with amber theme
- Tech stack information section
- Navigation to either game

## File Structure

```
New/Modified Files:
├── app/
│   ├── db.py                           (MODIFIED - added Question model)
│   ├── schema.py                       (MODIFIED - added trivia schemas)
│   ├── app.py                          (MODIFIED - added trivia endpoints)
│   ├── db_init_trivia.py              (NEW - database seeding script)
│   └── services/
│       └── trivia_services.py         (NEW - trivia game logic)
├── trivia.html                         (NEW - trivia game UI)
└── index.html                          (MODIFIED - game selection menu)
```

## Setup Instructions

### 1. Initialize Trivia Questions Database
Run the database seeding script to populate sample questions:

```bash
# From the project root directory
python -m app.db_init_trivia
```

This will add 20 sample questions covering:
- World Cup
- Premier League
- Champions League
- Player Awards
- Football Rules
- Stadiums

### 2. Start the Server
```bash
python main.py
```

The application will be available at `http://localhost:8000`

### 3. Access the Games
- **Home**: `http://localhost:8000/` - Game selection menu
- **Higher or Lower**: `http://localhost:8000/game` - Player comparison game
- **Football Trivia**: `http://localhost:8000/trivia` - Trivia quiz game

## API Schema

### Trivia Request/Response Models

**GetQuestion Response:**
```json
{
  "question": {
    "id": 1,
    "question_text": "Which country won the FIFA World Cup 2022?",
    "option_a": "France",
    "option_b": "Argentina",
    "option_c": "Brazil",
    "option_d": "Germany",
    "difficulty": "medium",
    "category": "World Cup"
  }
}
```

**VerifyAnswer Request:**
```json
{
  "question_id": 1,
  "selected_answer": "B"
}
```

**VerifyAnswer Response:**
```json
{
  "correct": true,
  "correct_answer": "B",
  "explanation": "The correct answer is B."
}
```

## Game Mechanics

### Higher or Lower
- User is shown two random players
- User guesses who has the higher statistic
- Correct answer: score increases and streak continues
- Wrong answer: streak resets to 0

### Football Trivia
- User is shown a question with 4 options
- User selects an answer
- Correct answer: score increases and streak continues
- Wrong answer: streak resets to 0, correct answer is highlighted
- Difficulty levels help users understand question complexity

## Scoring System
Both games track:
- **Score**: Cumulative points (increases by 1 per correct answer)
- **Streak**: Consecutive correct answers (resets to 0 on wrong answer)

## Adding More Questions
To add more trivia questions, edit `app/db_init_trivia.py`:

1. Add new entries to the `SAMPLE_QUESTIONS` list
2. Run the seeding script again (it checks for duplicates)

Example:
```python
{
    "question_text": "Your question here?",
    "option_a": "Answer 1",
    "option_b": "Answer 2",
    "option_c": "Answer 3",
    "option_d": "Answer 4",
    "correct_answer": "A",  # or B, C, D
    "difficulty": "easy",    # or "medium", "hard"
    "category": "Your Category",
}
```

## Technologies Used
- **Backend**: FastAPI with async/await
- **Database**: SQLite with SQLAlchemy ORM
- **Frontend**: HTML5, Tailwind CSS, Vanilla JavaScript
- **API Communication**: Fetch API with JSON

## Future Enhancements
Possible improvements:
- User authentication and leaderboards
- More questions database with admin panel
- Time limits for questions
- Different game modes (timed, survival, etc.)
- Question filtering by difficulty or category
- User statistics and analytics
- Mobile app version

## Troubleshooting

**"No questions in the database" error:**
- Run the database seeding script: `python -m app.db_init_trivia`

**API endpoints not found:**
- Make sure the server is running
- Check that you're using the correct URLs

**Styling issues:**
- Tailwind CSS is loaded from CDN, ensure internet connection
- Clear browser cache if styles don't update

## Notes
- The project uses SQLite, so data persists in `test.db`
- Both games are fully async and can handle multiple concurrent players
- No user authentication is required - it's open play
- All game data is stored in the database for potential future analytics
