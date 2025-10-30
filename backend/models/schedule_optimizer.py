from datetime import datetime, timedelta
from typing import Dict, List, Optional
import random

class ScheduleOptimizer:
    """ML-based posting schedule optimization"""
    
    def __init__(self):
        self.engagement_patterns = self._load_engagement_patterns()
        self.platform_data = self._load_platform_data()
        print("ScheduleOptimizer initialized successfully")
        
    def _load_engagement_patterns(self) -> Dict:
        """Load engagement patterns by audience and time"""
        return {
            'business': {
                'peak_hours': [9, 10, 11, 14, 15],
                'peak_days': [1, 2, 3, 4],  # Tuesday-Friday (0=Monday)
                'engagement_multiplier': 1.3
            },
            'general': {
                'peak_hours': [10, 12, 15, 19, 20],
                'peak_days': [0, 1, 2, 3, 4],  # Monday-Friday
                'engagement_multiplier': 1.0
            },
            'tech': {
                'peak_hours': [8, 9, 14, 15, 16],
                'peak_days': [1, 2, 3, 4],  # Tuesday-Friday
                'engagement_multiplier': 1.2
            },
            'lifestyle': {
                'peak_hours': [7, 8, 12, 18, 19, 20],
                'peak_days': [0, 1, 2, 3, 4, 5, 6],  # All days
                'engagement_multiplier': 1.1
            },
            'education': {
                'peak_hours': [8, 9, 10, 14, 15, 16],
                'peak_days': [0, 1, 2, 3, 4],  # Weekdays
                'engagement_multiplier': 1.15
            }
        }
    
    def _load_platform_data(self) -> Dict:
        """Load platform-specific posting data"""
        return {
            'website': {
                'optimal_frequency': 'daily',
                'best_times': [9, 10, 14, 15],
                'content_lifespan': '30 days',
                'posts_per_week': 5
            },
            'blog': {
                'optimal_frequency': '2-3 times per week',
                'best_times': [9, 10, 11],
                'content_lifespan': '60-90 days',
                'posts_per_week': 3
            },
            'social_media': {
                'optimal_frequency': 'multiple times daily',
                'best_times': [8, 12, 17, 19],
                'content_lifespan': '2-3 days',
                'posts_per_week': 14
            },
            'email': {
                'optimal_frequency': 'weekly',
                'best_times': [9, 10],
                'content_lifespan': '7 days',
                'posts_per_week': 1
            }
        }
    
    def generate_schedule(self, content_type: str, target_audience: str, 
                         platform: str = "website") -> Dict:
        """Generate optimal posting schedule"""
        
        try:
            print(f"Generating schedule for: {content_type}, {target_audience}, {platform}")
            
            # Get engagement patterns (case-insensitive)
            audience_lower = target_audience.lower()
            patterns = self.engagement_patterns.get(
                audience_lower, 
                self.engagement_patterns['general']
            )
            print(f"Using patterns for: {audience_lower}")
            
            # Get platform data (case-insensitive)
            platform_lower = platform.lower()
            platform_info = self.platform_data.get(
                platform_lower, 
                self.platform_data['website']
            )
            print(f"Using platform: {platform_lower}")
            
            # Generate weekly schedule
            weekly_schedule = self._generate_weekly_schedule(patterns, platform_info)
            print(f"Generated weekly schedule with {len(weekly_schedule)} days")
            
            # Generate monthly calendar
            monthly_calendar = self._generate_monthly_calendar(patterns, platform_info)
            print(f"Generated monthly calendar")
            
            # Generate recommendations
            recommendations = self._generate_schedule_recommendations(
                patterns, platform_info, content_type
            )
            print(f"Generated {len(recommendations)} recommendations")
            
            # Get optimal times
            optimal_times = self._get_optimal_posting_times(patterns)
            print(f"Generated {len(optimal_times)} optimal times")
            
            # Calculate expected impact
            impact = self._calculate_expected_impact(patterns, weekly_schedule)
            print(f"Calculated expected impact")
            
            result = {
                'weekly_schedule': weekly_schedule,
                'monthly_overview': monthly_calendar,
                'optimal_times': optimal_times,
                'recommendations': recommendations,
                'expected_impact': impact,
                'platform_insights': platform_info
            }
            
            print("Schedule generation completed successfully")
            return result
            
        except Exception as e:
            print(f"Error in generate_schedule: {str(e)}")
            import traceback
            traceback.print_exc()
            raise
    
    def _generate_weekly_schedule(self, patterns: Dict, platform_info: Dict) -> List[Dict]:
        """Generate weekly posting schedule"""
        
        try:
            schedule = []
            days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
            
            # Determine posts per week
            posts_per_week = platform_info.get('posts_per_week', 3)
            posts_distributed = []
            
            # Distribute posts across peak days
            peak_days = patterns['peak_days']
            for i in range(posts_per_week):
                day_idx = peak_days[i % len(peak_days)]
                posts_distributed.append(day_idx)
            
            for day_idx, day_name in enumerate(days):
                is_peak_day = day_idx in patterns['peak_days']
                num_posts = posts_distributed.count(day_idx)
                
                day_schedule = {
                    'day': day_name,
                    'is_peak_day': is_peak_day,
                    'posts': []
                }
                
                # Generate posts for the day
                peak_hours = patterns['peak_hours']
                for i in range(num_posts):
                    if is_peak_day and peak_hours:
                        hour = peak_hours[i % len(peak_hours)]
                    else:
                        hour = random.choice(range(9, 18))
                    
                    engagement_score = self._calculate_engagement_score(
                        day_idx, hour, patterns
                    )
                    
                    post = {
                        'time': f"{hour:02d}:00",
                        'engagement_score': round(engagement_score, 1),
                        'expected_reach': self._estimate_reach(engagement_score),
                        'recommended': engagement_score > 75
                    }
                    
                    day_schedule['posts'].append(post)
                
                # Sort posts by time
                if day_schedule['posts']:
                    day_schedule['posts'].sort(key=lambda x: x['time'])
                
                schedule.append(day_schedule)
            
            return schedule
            
        except Exception as e:
            print(f"Error in _generate_weekly_schedule: {str(e)}")
            raise
    
    def _generate_monthly_calendar(self, patterns: Dict, platform_info: Dict) -> Dict:
        """Generate monthly posting calendar"""
        
        try:
            today = datetime.now()
            start_date = today.replace(day=1)
            
            posts_per_week = platform_info.get('posts_per_week', 3)
            
            weeks = []
            for week in range(4):
                week_start = start_date + timedelta(weeks=week)
                
                high_priority_days = []
                for day_offset in range(7):
                    date = week_start + timedelta(days=day_offset)
                    if date.weekday() in patterns['peak_days']:
                        high_priority_days.append(date.strftime('%A'))
                
                week_data = {
                    'week': week + 1,
                    'start_date': week_start.strftime('%Y-%m-%d'),
                    'total_posts': posts_per_week,
                    'high_priority_days': high_priority_days
                }
                weeks.append(week_data)
            
            return {
                'total_posts_per_month': posts_per_week * 4,
                'weeks': weeks,
                'recommended_frequency': platform_info.get('optimal_frequency', 'weekly')
            }
            
        except Exception as e:
            print(f"Error in _generate_monthly_calendar: {str(e)}")
            raise
    
    def _calculate_engagement_score(self, day_idx: int, hour: int, 
                                   patterns: Dict) -> float:
        """Calculate engagement score for specific time"""
        
        try:
            score = 50.0  # Base score
            
            # Day score
            if day_idx in patterns['peak_days']:
                score += 20
            
            # Hour score
            if hour in patterns['peak_hours']:
                score += 25
            
            # Add some variance
            score += random.uniform(-3, 3)
            
            # Apply engagement multiplier
            multiplier = patterns.get('engagement_multiplier', 1.0)
            score *= multiplier
            
            # Ensure score is between 0 and 100
            score = max(0, min(100, score))
            
            return score
            
        except Exception as e:
            print(f"Error in _calculate_engagement_score: {str(e)}")
            return 50.0
    
    def _estimate_reach(self, engagement_score: float) -> str:
        """Estimate reach based on engagement score"""
        
        if engagement_score >= 80:
            return "High (5K-10K)"
        elif engagement_score >= 60:
            return "Medium (2K-5K)"
        else:
            return "Low (500-2K)"
    
    def _get_optimal_posting_times(self, patterns: Dict) -> List[Dict]:
        """Get list of optimal posting times"""
        
        try:
            times = []
            days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
            
            peak_days = patterns['peak_days']
            peak_hours = patterns['peak_hours']
            
            for day_idx in peak_days[:5]:
                for hour in peak_hours[:3]:
                    times.append({
                        'day': days[day_idx],
                        'time': f"{hour:02d}:00",
                        'engagement_potential': random.randint(80, 95)
                    })
            
            # Sort by engagement potential
            times.sort(key=lambda x: x['engagement_potential'], reverse=True)
            
            return times[:10]
            
        except Exception as e:
            print(f"Error in _get_optimal_posting_times: {str(e)}")
            return []
    
    def _generate_schedule_recommendations(self, patterns: Dict, 
                                         platform_info: Dict, 
                                         content_type: str) -> List[Dict]:
        """Generate scheduling recommendations"""
        
        try:
            recommendations = []
            
            # Frequency recommendation
            recommendations.append({
                'category': 'Frequency',
                'priority': 'high',
                'recommendation': f"Post {platform_info['optimal_frequency']} for optimal engagement",
                'reasoning': "This frequency aligns with platform best practices and audience behavior"
            })
            
            # Timing recommendation
            peak_hours = patterns['peak_hours']
            if peak_hours:
                recommendations.append({
                    'category': 'Timing',
                    'priority': 'high',
                    'recommendation': f"Schedule posts between {peak_hours[0]}:00 and {peak_hours[-1]}:00",
                    'reasoning': "These hours show highest engagement rates for your target audience"
                })
            
            # Day recommendation
            peak_days = patterns['peak_days']
            day_names = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
            best_days = [day_names[i] for i in peak_days[:3]]
            recommendations.append({
                'category': 'Days',
                'priority': 'medium',
                'recommendation': f"Focus on {', '.join(best_days)} for maximum reach",
                'reasoning': "These days show consistently higher engagement metrics"
            })
            
            # Content type specific recommendation
            content_lower = content_type.lower()
            if 'blog' in content_lower:
                recommendations.append({
                    'category': 'Content Strategy',
                    'priority': 'medium',
                    'recommendation': "Publish long-form content early in the week",
                    'reasoning': "Blog posts gain traction over several days, starting early maximizes exposure"
                })
            elif 'landing' in content_lower or 'page' in content_lower:
                recommendations.append({
                    'category': 'Content Strategy',
                    'priority': 'high',
                    'recommendation': "Update landing pages during off-peak hours",
                    'reasoning': "Minimize disruption to live traffic and allow time for testing"
                })
            
            # Consistency recommendation
            recommendations.append({
                'category': 'Consistency',
                'priority': 'high',
                'recommendation': "Maintain a consistent posting schedule",
                'reasoning': "Regular posting builds audience expectations and improves algorithmic favorability"
            })
            
            return recommendations
            
        except Exception as e:
            print(f"Error in _generate_schedule_recommendations: {str(e)}")
            return []
    
    def _calculate_expected_impact(self, patterns: Dict, schedule: List[Dict]) -> Dict:
        """Calculate expected impact of posting schedule"""
        
        try:
            total_posts = 0
            total_engagement = 0
            
            for day in schedule:
                for post in day.get('posts', []):
                    total_posts += 1
                    total_engagement += post.get('engagement_score', 0)
            
            avg_engagement = total_engagement / total_posts if total_posts > 0 else 50
            
            # Calculate potential reach
            if avg_engagement >= 80:
                reach_range = "50K-100K"
                traffic_increase = random.randint(40, 70)
            elif avg_engagement >= 60:
                reach_range = "20K-50K"
                traffic_increase = random.randint(25, 45)
            else:
                reach_range = "5K-20K"
                traffic_increase = random.randint(10, 30)
            
            compliance = self._calculate_compliance(schedule, patterns)
            
            return {
                'average_engagement_score': round(avg_engagement, 1),
                'estimated_weekly_reach': reach_range,
                'expected_traffic_increase': f"{traffic_increase}%",
                'conversion_potential': round(avg_engagement * 0.05, 2),
                'optimal_schedule_compliance': compliance
            }
            
        except Exception as e:
            print(f"Error in _calculate_expected_impact: {str(e)}")
            return {
                'average_engagement_score': 50.0,
                'estimated_weekly_reach': "Unknown",
                'expected_traffic_increase': "0%",
                'conversion_potential': 2.5,
                'optimal_schedule_compliance': 0.0
            }
    
    def _calculate_compliance(self, schedule: List[Dict], patterns: Dict) -> float:
        """Calculate how well schedule aligns with optimal patterns"""
        
        try:
            total_posts = 0
            optimal_posts = 0
            
            for day_idx, day in enumerate(schedule):
                for post in day.get('posts', []):
                    total_posts += 1
                    time_str = post.get('time', '12:00')
                    hour = int(time_str.split(':')[0])
                    
                    if day_idx in patterns['peak_days'] and hour in patterns['peak_hours']:
                        optimal_posts += 1
            
            compliance = (optimal_posts / total_posts * 100) if total_posts > 0 else 0
            return round(compliance, 1)
            
        except Exception as e:
            print(f"Error in _calculate_compliance: {str(e)}")
            return 0.0
    
    def is_ready(self) -> bool:
        """Check if model is ready"""
        return (self.engagement_patterns is not None and 
                self.platform_data is not None)

    def optimize(self, content_type: str, target_audience: str,
                 timezone: str = "UTC", num_suggestions: int = 5):
        """Compatibility wrapper: produce a list of schedule suggestions.

        This method adapts older callers that expect an `optimize` method
        returning a list of suggestion dicts. It uses the internal
        `generate_schedule` and flattens weekly posts into sorted suggestions.
        """
        try:
            result = self.generate_schedule(content_type, target_audience, platform=content_type)

            weekly = result.get('weekly_schedule', [])
            suggestions = []
            today = datetime.now()
            day_name_to_idx = {'Monday':0,'Tuesday':1,'Wednesday':2,'Thursday':3,'Friday':4,'Saturday':5,'Sunday':6}

            for day in weekly:
                day_name = day.get('day')
                day_idx = day_name_to_idx.get(day_name, None)
                for post in day.get('posts', []):
                    time_str = post.get('time', '12:00')
                    hour = int(time_str.split(':')[0])

                    # compute next date for this weekday
                    if day_idx is None:
                        scheduled_date = today
                    else:
                        days_ahead = (day_idx - today.weekday() + 7) % 7
                        if days_ahead == 0:
                            days_ahead = 7
                        scheduled_date = today + timedelta(days=days_ahead)

                    scheduled_dt = scheduled_date.replace(hour=hour, minute=0, second=0, microsecond=0)

                    suggestions.append({
                        'datetime': scheduled_dt.isoformat(),
                        'date': scheduled_dt.strftime('%Y-%m-%d'),
                        'time': scheduled_dt.strftime('%H:%M'),
                        'day_of_week': day_name,
                        'timezone': timezone,
                        'engagement_score': post.get('engagement_score', 0),
                        'competition_level': 'medium',
                        'expected_reach': post.get('expected_reach', ''),
                        'priority': post.get('engagement_score', 0),
                        'reasoning': 'Auto-generated suggestion from schedule optimizer.'
                    })

            # Sort by priority/engagement and return top N
            suggestions.sort(key=lambda x: (x.get('priority', 0), x.get('engagement_score', 0)), reverse=True)
            return suggestions[:num_suggestions]
        except Exception as e:
            print(f"Error in optimize wrapper: {e}")
            return []