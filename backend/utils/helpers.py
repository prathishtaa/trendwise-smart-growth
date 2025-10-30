# utils/helpers.py
import re
from typing import List, Dict
import json
from datetime import datetime

def clean_text(text: str) -> str:
    """Clean and normalize text"""
    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text)
    # Remove special characters but keep basic punctuation
    text = re.sub(r'[^\w\s\.\,\!\?\-\(\)]', '', text)
    return text.strip()

def extract_keywords_from_text(text: str, num_keywords: int = 10) -> List[str]:
    """Extract potential keywords from text"""
    # Simple extraction based on word frequency
    words = re.findall(r'\b[a-zA-Z]{4,}\b', text.lower())
    
    # Count frequency
    word_freq = {}
    for word in words:
        word_freq[word] = word_freq.get(word, 0) + 1
    
    # Sort by frequency
    sorted_words = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
    
    return [word for word, freq in sorted_words[:num_keywords]]

def calculate_content_metrics(content: str) -> Dict:
    """Calculate basic content metrics"""
    words = content.split()
    sentences = re.split(r'[.!?]+', content)
    paragraphs = content.split('\n\n')
    
    return {
        'word_count': len(words),
        'sentence_count': len([s for s in sentences if s.strip()]),
        'paragraph_count': len([p for p in paragraphs if p.strip()]),
        'avg_words_per_sentence': len(words) / max(len(sentences), 1),
        'avg_sentence_per_paragraph': len(sentences) / max(len(paragraphs), 1)
    }

def format_schedule_datetime(dt: datetime) -> Dict:
    """Format datetime for schedule response"""
    return {
        'iso': dt.isoformat(),
        'date': dt.strftime('%Y-%m-%d'),
        'time': dt.strftime('%H:%M'),
        'day': dt.strftime('%A'),
        'readable': dt.strftime('%B %d, %Y at %I:%M %p')
    }

def calculate_keyword_difficulty(search_volume: int, competition: float) -> str:
    """Calculate keyword difficulty level"""
    score = (search_volume / 10000) * competition
    
    if score < 5:
        return "easy"
    elif score < 15:
        return "medium"
    elif score < 30:
        return "hard"
    else:
        return "very_hard"

def generate_meta_description(content: str, max_length: int = 160) -> str:
    """Generate SEO meta description from content"""
    # Get first paragraph or first few sentences
    sentences = re.split(r'[.!?]+', content)
    
    description = ""
    for sentence in sentences:
        if len(description) + len(sentence) < max_length - 3:
            description += sentence.strip() + ". "
        else:
            break
    
    if len(description) > max_length:
        description = description[:max_length-3] + "..."
    
    return description.strip()

def validate_content_type(content_type: str) -> bool:
    """Validate content type"""
    valid_types = ['blog', 'landing_page', 'app_description', 'social_media', 'email']
    return content_type.lower() in valid_types

def calculate_seo_improvements(current_score: float, target_score: float = 90) -> List[str]:
    """Calculate what improvements are needed to reach target SEO score"""
    improvements = []
    gap = target_score - current_score
    
    if gap <= 0:
        return ["Your content is already well-optimized!"]
    
    if gap > 40:
        improvements.append("Major optimization needed - focus on keyword integration")
        improvements.append("Improve content structure with clear headings")
        improvements.append("Enhance readability and content length")
    elif gap > 20:
        improvements.append("Add more relevant keywords naturally")
        improvements.append("Improve meta descriptions and title tags")
        improvements.append("Increase content depth and quality")
    elif gap > 10:
        improvements.append("Fine-tune keyword placement")
        improvements.append("Add internal and external links")
        improvements.append("Optimize images with alt text")
    else:
        improvements.append("Add schema markup")
        improvements.append("Improve page load speed")
        improvements.append("Enhance mobile responsiveness")
    
    return improvements

def format_api_response(success: bool, data: any = None, 
                       error: str = None, metadata: Dict = None) -> Dict:
    """Standardize API response format"""
    response = {
        'success': success,
        'timestamp': datetime.now().isoformat()
    }
    
    if data is not None:
        response['data'] = data
    
    if error:
        response['error'] = error
    
    if metadata:
        response['metadata'] = metadata
    
    return response

def parse_content_type_from_url(url: str) -> str:
    """Determine content type from URL pattern"""
    url_lower = url.lower()
    
    if '/blog/' in url_lower or '/post/' in url_lower:
        return 'blog'
    elif '/landing' in url_lower or '/lp/' in url_lower:
        return 'landing_page'
    elif '/app/' in url_lower or 'store' in url_lower:
        return 'app_description'
    else:
        return 'general'

class ContentValidator:
    """Validate content quality and requirements"""
    
    @staticmethod
    def validate_min_length(content: str, min_words: int = 300) -> tuple[bool, str]:
        """Check if content meets minimum length"""
        word_count = len(content.split())
        
        if word_count < min_words:
            return False, f"Content too short: {word_count} words (minimum: {min_words})"
        return True, "Length OK"
    
    @staticmethod
    def validate_keyword_presence(content: str, keywords: List[str]) -> tuple[bool, str]:
        """Check if keywords are present"""
        content_lower = content.lower()
        missing_keywords = [kw for kw in keywords if kw.lower() not in content_lower]
        
        if len(missing_keywords) > len(keywords) / 2:
            return False, f"Many keywords missing: {', '.join(missing_keywords[:3])}"
        return True, "Keywords present"
    
    @staticmethod
    def validate_structure(content: str) -> tuple[bool, str]:
        """Check if content has proper structure"""
        has_title = content.strip().startswith('#')
        has_paragraphs = '\n\n' in content
        has_headings = '##' in content or '###' in content
        
        if not (has_title or has_paragraphs or has_headings):
            return False, "Content lacks proper structure (title, headings, paragraphs)"
        return True, "Structure OK"

def export_to_json(data: Dict, filename: str) -> bool:
    """Export data to JSON file"""
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        return True
    except Exception as e:
        print(f"Error exporting to JSON: {e}")
        return False

def import_from_json(filename: str) -> Dict:
    """Import data from JSON file"""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error importing from JSON: {e}")
        return {}

# Rate limiting helper
class RateLimiter:
    def __init__(self):
        self.requests = {}
    
    def is_allowed(self, key: str, max_requests: int = 100, 
                   window_seconds: int = 3600) -> bool:
        """Check if request is allowed based on rate limit"""
        now = datetime.now()
        
        if key not in self.requests:
            self.requests[key] = []
        
        # Remove old requests outside the window
        self.requests[key] = [
            req_time for req_time in self.requests[key]
            if (now - req_time).total_seconds() < window_seconds
        ]
        
        # Check if limit exceeded
        if len(self.requests[key]) >= max_requests:
            return False
        
        # Add current request
        self.requests[key].append(now)
        return True