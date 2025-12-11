# Quick Start Guide - Football Games Project

## 🚀 Getting Started

### 1. Initialize the Trivia Database
First, populate the trivia questions database:

```bash
cd /home/admin123/Desktop/software_project/project_football/project
python -m app.db_init_trivia
```

**Expected Output:**
```
Successfully seeded 20 questions!
```

### 2. Start the Server
```bash
python main.py
```

**Expected Output:**
```
INFO:     Started server process [PID]
INFO:     Waiting for application startup.
INFO:     Application startup complete
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
```

### 3. Open Your Browser
Visit: **http://localhost:8000**

## 📊 Game Selection Screen

You'll see two game options:

### 🎲 Higher or Lower
- Compare player statistics
- Guess who has the higher value
- Build streaks for points
- **Play**: Click the green "Play now" button

### 🧠 Football Trivia
- Answer multiple-choice questions
- Track your score and streak
- Different difficulty levels
- **Play**: Click the amber "Play now" button

## 🎮 How to Play

### Higher or Lower
1. You'll see two player cards
2. Each card shows a player's name and photo
3. The stat value is hidden (shown as "?")
4. Click the player you think has the higher value
5. The values reveal and your guess is verified
6. ✓ Correct: Score increases, next question
7. ✗ Wrong: Streak resets, next question

### Football Trivia
1. Read the question carefully
2. You'll see 4 answer options (A, B, C, D)
3. Click your answer choice
4. The system shows if you're correct
5. ✓ Correct: Score increases, streak continues
6. ✗ Wrong: Correct answer is highlighted
7. New question loads automatically

## 📈 Scoring

Both games track:
- **Score**: Total points (1 point per correct answer)
- **Streak**: Consecutive correct answers (resets on wrong answer)

## 🔄 Resetting Games

- Click **"New game"** button to restart with score = 0
- Click **"Back to menu"** to return to game selection
- Click the logo to return to home page

## 🛠️ Adding More Trivia Questions

Edit `app/db_init_trivia.py` and add entries to `SAMPLE_QUESTIONS`:

```python
{
    "question_text": "Your question?",
    "option_a": "Choice 1",
    "option_b": "Choice 2",
    "option_c": "Choice 3",
    "option_d": "Choice 4",
    "correct_answer": "B",        # Correct answer (A, B, C, or D)
    "difficulty": "medium",       # easy, medium, or hard
    "category": "Premier League",  # Any category name
}
```

Then re-run:
```bash
python -m app.db_init_trivia
```

## 📁 Project Structure

```
project/
├── app/
│   ├── db.py                    (Database models: Player, Question)
│   ├── schema.py                (Pydantic schemas for API)
│   ├── app.py                   (FastAPI routes)
│   ├── db_init_trivia.py       (Question seeding script)
│   ├── services/
│   │   ├── game_services.py     (Higher or Lower logic)
│   │   └── trivia_services.py   (Trivia game logic)
│   └── db/
│       └── players_source.csv   (Player data)
├── index.html                   (Game selection page)
├── game.html                    (Higher or Lower game)
├── trivia.html                  (Football Trivia game)
├── main.py                      (Server entry point)
└── TRIVIA_GAME_UPDATE.md       (Full documentation)
```

## 🐛 Troubleshooting

| Problem | Solution |
|---------|----------|
| "No questions in the database" | Run `python -m app.db_init_trivia` |
| Page won't load | Check if server is running on http://localhost:8000 |
| Buttons not working | Clear browser cache or try a different browser |
| Styling looks broken | Ensure you have internet (Tailwind CSS via CDN) |
| Questions keep repeating | The database has all questions, restarting server may help |

## 📚 Available Trivia Categories

The sample database includes questions from:
- ⚽ World Cup
- 🏆 Premier League
- 🏅 Champions League
- 🎖️ Player Awards
- 📋 Football Rules
- 🏟️ Stadiums
- 👥 Player History

## 🌐 API Endpoints

### Higher or Lower
- `GET /game` - Game page
- `GET /api/player/random` - Get 2 random players
- `POST /api/game/verify` - Verify guess

### Football Trivia
- `GET /trivia` - Trivia game page
- `GET /api/trivia/question` - Get random question
- `POST /api/trivia/verify` - Verify answer

### General
- `GET /` - Home page (game selection)
- `GET /health` - Health check

## 🎯 Next Steps

1. ✅ Start the server
2. ✅ Initialize the trivia database
3. ✅ Try both games
4. ✅ Add your own questions
5. ✅ Customize the styling if desired
6. ✅ Share with friends!

Enjoy! 🎮⚽
