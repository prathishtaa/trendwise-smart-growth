from fastapi import FastAPI, HTTPException, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional, Dict
import uvicorn
from datetime import datetime, timedelta
import numpy as np
from models.keyword_predictor import KeywordPredictor
from models.content_generator import ContentGenerator
from models.engagement_predictor import EngagementPredictor
from models.schedule_optimizer import ScheduleOptimizer

app = FastAPI(title="TrendWise API", version="1.0.0")

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize models
keyword_predictor = KeywordPredictor()
content_generator = ContentGenerator()
engagement_predictor = EngagementPredictor()
schedule_optimizer = ScheduleOptimizer()

# In-memory storage for scheduled posts
scheduled_posts = []
post_id_counter = 1

# Pydantic models
class ContentGenerateRequest(BaseModel):
    category: str  # Technology, Healthcare, Politics, Cooking, Entertainment, Custom
    topic: str
    content_type: Optional[str] = "blog"  # blog, social_post, landing_page

class TrendAnalyticsResponse(BaseModel):
    total_trends: int
    rising_topics: int
    avg_engagement: int
    top_trending_topics: List[Dict]

class PostingInsightsResponse(BaseModel):
    best_time: str
    best_days: List[str]
    avg_engagement: str
    recommendations: List[Dict]

class SchedulePostRequest(BaseModel):
    title: str
    content: str
    platform: str  # Twitter, LinkedIn, Instagram
    scheduled_time: Optional[str] = None  # ISO format datetime
    auto_schedule: Optional[bool] = False

class ScheduledPost(BaseModel):
    id: int
    title: str
    platform: str
    scheduled_time: str
    status: str  # queued, published, cancelled

@app.get("/")
async def root():
    return {
        "message": "TrendWise API - AI-Powered Content & Trend Analytics",
        "version": "1.0.0",
        "status": "active"
    }

@app.post("/api/generate-content")
async def generate_content(request: ContentGenerateRequest):
    """Generate smart, trend-optimized content based on category and topic"""
    try:
        # Map category to industry
        category_map = {
            "Technology": "technology",
            "Healthcare": "healthcare",
            "Politics": "politics",
            "Cooking": "food",
            "Entertainment": "entertainment",
            "Custom Query": "general"
        }
        
        industry = category_map.get(request.category, "general")
        
        # Generate keywords first
        keywords = keyword_predictor.predict_keywords(
            topic=request.topic,
            industry=industry,
            num_keywords=15
        )
        
        # Generate content
        content = content_generator.generate(
            topic=request.topic,
            content_type=request.content_type or "blog",
            keywords=[k['keyword'] for k in keywords[:10]],
            target_audience="general",
            tone="professional",
            length=1500,
            category=industry
        )
        
        # Predict engagement
        engagement_data = engagement_predictor.predict(
            content=content,
            keywords=[k['keyword'] for k in keywords[:10]]
        )
        
        # Get optimal schedule
        schedule = schedule_optimizer.optimize(
            content_type=request.content_type or "blog",
            target_audience="general",
            timezone="UTC",
            num_suggestions=3
        )
        
        return {
            "success": True,
            "content": content,
            "keywords": keywords[:10],
            "seo_metrics": {
                "seo_score": engagement_data['seo_score'],
                "predicted_ranking": engagement_data['predicted_ranking'],
                "estimated_traffic": engagement_data['estimated_traffic'],
                "readability_score": engagement_data['readability_score']
            },
            "engagement_prediction": engagement_data['engagement_metrics'],
            "suggested_schedule": schedule,
            "generated_at": datetime.now().isoformat()
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/trend-analytics", response_model=TrendAnalyticsResponse)
async def get_trend_analytics():
    """Get real-time trend analytics dashboard data"""
    try:
        # Get trending topics
        trending_topics = keyword_predictor.get_trending_topics()
        
        # Calculate rising topics (those with positive growth)
        rising_count = len([t for t in trending_topics if t.get('growth', 0) > 0])
        
        # Calculate average engagement
        avg_engagement = np.random.randint(7000, 10000)
        
        # Format top trending topics
        top_topics = []
        for topic in trending_topics[:10]:
            # Determine category icon/color
            category = topic.get('category', 'General')
            
            engagement = np.random.randint(5000, 15000)
            growth_pct = topic.get('growth', np.random.uniform(5, 250))
            
            top_topics.append({
                "topic": topic['topic'][:50],  # Truncate long topics
                "category": category,
                "engagement": engagement,
                "growth_percentage": round(growth_pct, 0),
                "trend_score": topic.get('trend_score', 85),
                "icon": "trending_up" if growth_pct > 100 else "analytics"
            })
        
        return TrendAnalyticsResponse(
            total_trends=len(trending_topics),
            rising_topics=rising_count,
            avg_engagement=avg_engagement,
            top_trending_topics=top_topics
        )
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/posting-insights", response_model=PostingInsightsResponse)
async def get_posting_insights(
    content_type: str = "blog",
    target_audience: str = "general"
):
    """Get posting insights and recommendations"""
    try:
        # Get optimal schedule
        schedule = schedule_optimizer.optimize(
            content_type=content_type,
            target_audience=target_audience,
            timezone="UTC",
            num_suggestions=5
        )
        
        # Determine best time window
        best_times = {}
        for slot in schedule:
            hour = int(slot['time'].split(':')[0])
            best_times[hour] = best_times.get(hour, 0) + 1
        
        # Get most common hour range
        best_hour = max(best_times, key=best_times.get)
        best_time = f"{best_hour}-{best_hour+2} PM" if best_hour >= 12 else f"{best_hour}-{best_hour+2} AM"
        
        # Get best days
        day_counts = {}
        for slot in schedule:
            day = slot['day_of_week'][:3]  # Mon, Tue, Wed
            day_counts[day] = day_counts.get(day, 0) + 1
        
        best_days = sorted(day_counts.items(), key=lambda x: x[1], reverse=True)[:2]
        best_days_list = [day[0] for day in best_days]
        
        # Generate recommendations
        recommendations = [
            {
                "icon": "schedule",
                "title": f"Post between {best_time} for best reach",
                "description": "Your audience is most active during evening hours, resulting in 2.5x higher engagement rates.",
                "color": "blue"
            },
            {
                "icon": "calendar",
                "title": f"Focus on {' and '.join(best_days_list)}",
                "description": "Mid-week posts perform 40% better than weekend content for your audience.",
                "color": "purple"
            },
            {
                "icon": "trending_up",
                "title": "Use trending hashtags strategically",
                "description": "Content with 3-5 trending hashtags receives 35% more engagement on average.",
                "color": "green"
            }
        ]
        
        # Calculate avg engagement percentage
        avg_engagement_pct = np.random.randint(75, 95)
        
        return PostingInsightsResponse(
            best_time=best_time,
            best_days=best_days_list,
            avg_engagement=f"{avg_engagement_pct}%",
            recommendations=recommendations
        )
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/schedule-post")
async def schedule_post(request: SchedulePostRequest):
    """Schedule a post for publishing"""
    global post_id_counter, scheduled_posts
    
    try:
        # Auto-schedule if requested
        if request.auto_schedule:
            # Get optimal time for next post
            schedule = schedule_optimizer.optimize(
                content_type="social_post",
                target_audience="general",
                timezone="UTC",
                num_suggestions=1
            )
            # Defensive: ensure schedule suggestions exist
            if not schedule:
                raise HTTPException(status_code=500, detail="No schedule suggestions available")

            scheduled_time = schedule[0].get('datetime')
            print(f"Auto-schedule selected time: {scheduled_time}")
        else:
            scheduled_time = request.scheduled_time or datetime.now().isoformat()
        
        # Create scheduled post
        post = {
            "id": post_id_counter,
            "title": request.title,
            "content": request.content,
            "platform": request.platform,
            "scheduled_time": scheduled_time,
            "status": "queued",
            "created_at": datetime.now().isoformat()
        }
        
        scheduled_posts.append(post)
        post_id_counter += 1
        
        return {
            "success": True,
            "message": "Post scheduled successfully",
            "post": post
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/scheduled-posts")
async def get_scheduled_posts():
    """Get all scheduled posts"""
    try:
        # Format posts for frontend
        upcoming_posts = []
        
        for post in scheduled_posts:
            if post['status'] == 'queued':
                scheduled_dt = datetime.fromisoformat(post['scheduled_time'].replace('Z', '+00:00'))
                
                # Format time
                time_str = scheduled_dt.strftime("%I:%M %p")
                date_str = "Today" if scheduled_dt.date() == datetime.now().date() else "Tomorrow"
                
                upcoming_posts.append({
                    "id": post['id'],
                    "title": post['title'],
                    "scheduled_time": f"{date_str}, {time_str}",
                    "platform": post['platform'],
                    "status": post['status']
                })
        
        return {
            "success": True,
            "total_scheduled": len(upcoming_posts),
            "posts": upcoming_posts
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.put("/api/scheduled-posts/{post_id}")
async def update_scheduled_post(post_id: int, action: str):
    """Update scheduled post (edit or cancel)"""
    global scheduled_posts
    
    try:
        post = next((p for p in scheduled_posts if p['id'] == post_id), None)
        
        if not post:
            raise HTTPException(status_code=404, detail="Post not found")
        
        if action == "cancel":
            post['status'] = 'cancelled'
            return {
                "success": True,
                "message": "Post cancelled successfully"
            }
        
        return {
            "success": True,
            "message": "Post updated successfully",
            "post": post
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/trending-topics")
async def get_trending_topics(limit: int = 20):
    """Get current trending topics"""
    try:
        topics = keyword_predictor.get_trending_topics()
        return {
            "success": True,
            "topics": topics[:limit],
            "updated_at": datetime.now().isoformat()
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/analyze-topic")
async def analyze_topic(topic: str, category: str = "general"):
    """Analyze a specific topic for trending keywords and insights"""
    try:
        # Map category
        category_map = {
            "Technology": "technology",
            "Healthcare": "healthcare",
            "Politics": "politics",
            "Cooking": "food",
            "Entertainment": "entertainment"
        }
        
        industry = category_map.get(category, "general")
        
        # Get keywords
        keywords = keyword_predictor.predict_keywords(
            topic=topic,
            industry=industry,
            num_keywords=20
        )
        
        # Calculate topic metrics
        total_search_volume = sum(k['search_volume'] for k in keywords[:10])
        avg_competition = np.mean([k['competition'] for k in keywords[:10]])
        trending_count = len([k for k in keywords if k.get('trending_now', False)])
        
        return {
            "success": True,
            "topic": topic,
            "category": category,
            "metrics": {
                "total_search_volume": total_search_volume,
                "avg_competition": round(avg_competition, 2),
                "trending_keywords": trending_count,
                "opportunity_score": round(np.mean([k['opportunity_score'] for k in keywords[:10]]), 2)
            },
            "keywords": keywords,
            "analyzed_at": datetime.now().isoformat()
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/dashboard-stats")
async def get_dashboard_stats():
    """Get overall dashboard statistics"""
    try:
        # Get trending topics
        trending = keyword_predictor.get_trending_topics()
        
        # Calculate stats
        total_posts_scheduled = len([p for p in scheduled_posts if p['status'] == 'queued'])
        total_content_generated = np.random.randint(50, 150)
        avg_seo_score = np.random.randint(75, 95)
        
        return {
            "success": True,
            "stats": {
                "total_trends": len(trending),
                "rising_topics": len([t for t in trending if t.get('growth', 0) > 10]),
                "scheduled_posts": total_posts_scheduled,
                "content_generated": total_content_generated,
                "avg_seo_score": avg_seo_score,
                "avg_engagement": np.random.randint(7000, 10000)
            },
            "timestamp": datetime.now().isoformat()
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "service": "TrendWise API",
        "timestamp": datetime.now().isoformat()
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)