# TrendWise Backend

AI-powered content generation and trend analytics API.

## Quick Start
```bash
# 1. Setup
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python -m textblob.download_corpora

# 2. Run
uvicorn main:app --reload

# 3. Open
http://localhost:8000/docs
```

## API Endpoints

- `POST /api/generate-content` - Generate AI content
- `GET /api/trend-analytics` - Get trend analytics
- `GET /api/posting-insights` - Get posting insights
- `POST /api/schedule-post` - Schedule a post
- `GET /api/scheduled-posts` - List scheduled posts
- `GET /api/trending-topics` - Get trending topics

## Features

✅ Real-time trending keywords (Google, Reddit, News)
✅ AI content generation
✅ SEO score prediction
✅ Smart scheduling
✅ No database required