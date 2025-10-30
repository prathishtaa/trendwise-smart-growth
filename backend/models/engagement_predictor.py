import numpy as np
import re
from typing import List, Dict
from textblob import TextBlob
import math

class EngagementPredictor:
    def __init__(self):
        self.weights = {
            'keyword_density': 0.25,
            'readability': 0.20,
            'content_length': 0.15,
            'keyword_placement': 0.20,
            'semantic_relevance': 0.20
        }
        
    def predict(self, content: str, keywords: List[str], 
                platform: str = "website") -> Dict:
        """Predict engagement metrics for content"""
        
        # Calculate individual scores
        keyword_score = self._calculate_keyword_score(content, keywords)
        readability_score = self._calculate_readability(content)
        length_score = self._calculate_length_score(content)
        placement_score = self._calculate_placement_score(content, keywords)
        semantic_score = self._calculate_semantic_score(content, keywords)
        
        # Calculate weighted SEO score
        seo_score = (
            keyword_score * self.weights['keyword_density'] +
            readability_score * self.weights['readability'] +
            length_score * self.weights['content_length'] +
            placement_score * self.weights['keyword_placement'] +
            semantic_score * self.weights['semantic_relevance']
        )
        
        # Predict ranking (1-100, where 1 is best)
        predicted_ranking = self._predict_ranking(seo_score)
        
        # Estimate traffic
        estimated_traffic = self._estimate_traffic(seo_score, predicted_ranking)
        
        # Calculate engagement metrics
        engagement_rate = self._calculate_engagement_rate(
            seo_score, readability_score, platform
        )
        
        # Calculate click-through rate
        ctr = self._calculate_ctr(seo_score, predicted_ranking)
        
        # Calculate bounce rate
        bounce_rate = self._calculate_bounce_rate(readability_score, length_score)
        
        return {
            'seo_score': round(seo_score, 2),
            'predicted_ranking': predicted_ranking,
            'estimated_traffic': estimated_traffic,
            'readability_score': round(readability_score, 2),
            'engagement_metrics': {
                'engagement_rate': round(engagement_rate, 2),
                'click_through_rate': round(ctr, 2),
                'bounce_rate': round(bounce_rate, 2),
                'avg_time_on_page': self._estimate_time_on_page(len(content.split()))
            },
            'keyword_metrics': {
                'keyword_density': round(keyword_score, 2),
                'keyword_placement': round(placement_score, 2),
                'semantic_relevance': round(semantic_score, 2)
            },
            'content_metrics': {
                'word_count': len(content.split()),
                'sentence_count': len(re.split(r'[.!?]+', content)),
                'paragraph_count': len(content.split('\n\n'))
            },
            'improvement_suggestions': self._generate_suggestions(
                seo_score, readability_score, keyword_score, length_score
            )
        }
    
    def _calculate_keyword_score(self, content: str, keywords: List[str]) -> float:
        """Calculate keyword density and distribution score"""
        content_lower = content.lower()
        words = content_lower.split()
        total_words = len(words)
        
        if total_words == 0:
            return 0
        
        keyword_count = 0
        for keyword in keywords[:5]:  # Focus on top 5 keywords
            keyword_count += content_lower.count(keyword.lower())
        
        # Optimal density is 1-3%
        density = (keyword_count / total_words) * 100
        
        if 1 <= density <= 3:
            score = 100
        elif density < 1:
            score = density * 100
        else:
            score = max(0, 100 - (density - 3) * 20)
        
        return score
    
    def _calculate_readability(self, content: str) -> float:
        """Calculate readability score (Flesch Reading Ease)"""
        sentences = len(re.split(r'[.!?]+', content))
        words = len(content.split())
        
        if sentences == 0 or words == 0:
            return 50
        
        # Count syllables (approximation)
        syllables = sum([self._count_syllables(word) for word in content.split()])
        
        # Flesch Reading Ease formula
        if sentences > 0 and words > 0:
            score = 206.835 - 1.015 * (words / sentences) - 84.6 * (syllables / words)
            # Normalize to 0-100
            score = max(0, min(100, score))
        else:
            score = 50
        
        return score
    
    def _count_syllables(self, word: str) -> int:
        """Count syllables in a word (approximation)"""
        word = word.lower()
        vowels = "aeiouy"
        syllable_count = 0
        previous_was_vowel = False
        
        for char in word:
            is_vowel = char in vowels
            if is_vowel and not previous_was_vowel:
                syllable_count += 1
            previous_was_vowel = is_vowel
        
        # Adjust for silent 'e'
        if word.endswith('e'):
            syllable_count -= 1
        
        # Minimum one syllable
        return max(1, syllable_count)
    
    def _calculate_length_score(self, content: str) -> float:
        """Calculate optimal content length score"""
        word_count = len(content.split())
        
        # Optimal length: 1500-2500 words for blogs
        if 1500 <= word_count <= 2500:
            score = 100
        elif word_count < 1500:
            score = (word_count / 1500) * 100
        else:
            score = max(50, 100 - (word_count - 2500) / 50)
        
        return score
    
    def _calculate_placement_score(self, content: str, keywords: List[str]) -> float:
        """Calculate score based on keyword placement in important areas"""
        score = 0
        content_lower = content.lower()
        
        # Check title (first line)
        first_line = content.split('\n')[0].lower() if content else ""
        if any(kw.lower() in first_line for kw in keywords[:3]):
            score += 40
        
        # Check first paragraph (first 200 chars)
        first_para = content[:200].lower()
        if any(kw.lower() in first_para for kw in keywords[:3]):
            score += 30
        
        # Check headings (lines starting with #)
        headings = [line for line in content.split('\n') if line.startswith('#')]
        heading_text = ' '.join(headings).lower()
        if any(kw.lower() in heading_text for kw in keywords[:5]):
            score += 30
        
        return min(100, score)
    
    def _calculate_semantic_score(self, content: str, keywords: List[str]) -> float:
        """Calculate semantic relevance using simple text analysis"""
        try:
            blob = TextBlob(content)
            sentiment = blob.sentiment.polarity
            
            # Check for keyword variations and related terms
            content_lower = content.lower()
            variation_count = 0
            
            for keyword in keywords:
                # Check for exact match
                if keyword.lower() in content_lower:
                    variation_count += 2
                # Check for partial match
                keyword_words = keyword.lower().split()
                if any(word in content_lower for word in keyword_words):
                    variation_count += 1
            
            # Score based on variation usage
            score = min(100, (variation_count / len(keywords)) * 50 + 50)
            
            return score
        except:
            return 75  # Default score if analysis fails
    
    def _predict_ranking(self, seo_score: float) -> int:
        """Predict search ranking based on SEO score"""
        # Higher SEO score = better ranking (lower number)
        if seo_score >= 90:
            return np.random.randint(1, 5)
        elif seo_score >= 80:
            return np.random.randint(5, 15)
        elif seo_score >= 70:
            return np.random.randint(15, 30)
        elif seo_score >= 60:
            return np.random.randint(30, 50)
        else:
            return np.random.randint(50, 100)
    
    def _estimate_traffic(self, seo_score: float, ranking: int) -> int:
        """Estimate monthly traffic based on SEO score and ranking"""
        base_traffic = 10000
        
        # Traffic decreases exponentially with ranking
        ranking_factor = math.exp(-0.1 * ranking)
        
        # SEO score multiplier
        seo_factor = seo_score / 100
        
        estimated = int(base_traffic * ranking_factor * seo_factor)
        
        return max(100, estimated)
    
    def _calculate_engagement_rate(self, seo_score: float, 
                                   readability: float, platform: str) -> float:
        """Calculate engagement rate percentage"""
        base_rate = 2.5  # 2.5% base engagement
        
        quality_factor = (seo_score + readability) / 200
        
        platform_multipliers = {
            'website': 1.0,
            'social_media': 1.5,
            'email': 1.2
        }
        
        multiplier = platform_multipliers.get(platform, 1.0)
        
        return base_rate * quality_factor * multiplier
    
    def _calculate_ctr(self, seo_score: float, ranking: int) -> float:
        """Calculate click-through rate"""
        # CTR is heavily influenced by ranking
        if ranking <= 3:
            base_ctr = 30
        elif ranking <= 10:
            base_ctr = 10
        elif ranking <= 20:
            base_ctr = 3
        else:
            base_ctr = 1
        
        # Adjust by SEO score
        ctr = base_ctr * (seo_score / 100)
        
        return min(35, ctr)
    
    def _calculate_bounce_rate(self, readability: float, length_score: float) -> float:
        """Calculate bounce rate (lower is better)"""
        # Good readability and length = lower bounce rate
        quality = (readability + length_score) / 2
        
        # Inverse relationship
        bounce_rate = 100 - quality
        
        # Typical bounce rates: 40-60%
        bounce_rate = 40 + (bounce_rate * 0.2)
        
        return min(90, max(25, bounce_rate))
    
    def _estimate_time_on_page(self, word_count: int) -> str:
        """Estimate average time on page"""
        # Average reading speed: 200-250 words per minute
        minutes = word_count / 225
        
        if minutes < 1:
            return f"{int(minutes * 60)}s"
        else:
            return f"{minutes:.1f}m"
    
    def _generate_suggestions(self, seo_score: float, readability: float,
                             keyword_score: float, length_score: float) -> List[str]:
        """Generate improvement suggestions"""
        suggestions = []
        
        if seo_score < 70:
            suggestions.append("Overall SEO score needs improvement. Focus on keyword optimization and content quality.")
        
        if readability < 60:
            suggestions.append("Improve readability by using shorter sentences and simpler words.")
        
        if keyword_score < 50:
            suggestions.append("Increase keyword density to 1-3% for better SEO performance.")
        elif keyword_score > 80:
            suggestions.append("Reduce keyword density to avoid over-optimization.")
        
        if length_score < 70:
            suggestions.append("Content length is not optimal. Aim for 1500-2500 words for better ranking.")
        
        if not suggestions:
            suggestions.append("Content is well-optimized! Consider adding more internal links and updating regularly.")
        
        return suggestions