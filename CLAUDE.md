# CLAUDE.md

## Project Overview

**Korean Noir Film Scene Generator** ("누아르 영화 씬 메이커") — a Streamlit web application that uses Google's Gemini AI to generate Korean noir-style film dialogue and directing guidelines from user-provided scene descriptions.

The UI and all user-facing text are in Korean. This is an early-stage prototype with a single-file architecture.

## Tech Stack

- **Language:** Python 3.11+
- **Web Framework:** Streamlit
- **AI Backend:** Google Generative AI (Gemini 1.5 Flash)
- **Dependencies:** Managed via `requirements.txt`

## Repository Structure

```
my-movie-app/
├── app.py              # Main application (entry point)
├── requirements.txt    # Python dependencies
└── CLAUDE.md           # This file
```

## Getting Started

### Install dependencies

```bash
pip install -r requirements.txt
```

### Configure the API key

The app reads `GOOGLE_API_KEY` from Streamlit secrets. Create `.streamlit/secrets.toml`:

```toml
GOOGLE_API_KEY = "your-google-api-key-here"
```

### Run the application

```bash
streamlit run app.py
```

## Architecture

- **Single-file app** (`app.py`): All logic lives in one file — UI rendering, API configuration, and AI content generation.
- **Streamlit declarative UI**: Uses `st.title`, `st.text_area`, `st.button`, `st.spinner`, and `st.write` for the interface.
- **Google Generative AI**: Configured via `genai.configure()` with the API key from Streamlit secrets. Uses the `gemini-1.5-flash` model.

### Request Flow

1. User enters a scene description in the text area
2. User clicks "AI 분석 시작" (Start AI Analysis)
3. App appends a Korean noir prompt instruction to the user input
4. Gemini generates dialogue and directing guidelines
5. Response is rendered as markdown

## Code Conventions

- Comments and UI strings are in **Korean**
- No classes or complex abstractions — procedural style
- No custom error handling beyond checking for API key presence

## Development Notes

- **No test framework** is configured. There are no test files.
- **No linter/formatter** is configured (no flake8, black, isort, etc.).
- **No CI/CD pipeline** exists (no GitHub Actions or similar).
- **No `.gitignore`** is present — be careful not to commit `.streamlit/secrets.toml` or other sensitive files.
- The app has no environment variable fallback; it relies exclusively on `st.secrets`.

## Common Tasks

| Task | Command |
|------|---------|
| Install deps | `pip install -r requirements.txt` |
| Run app | `streamlit run app.py` |
| Add a dependency | Add to `requirements.txt`, then `pip install -r requirements.txt` |
