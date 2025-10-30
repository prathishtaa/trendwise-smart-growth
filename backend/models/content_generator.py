import random
from typing import List
import re

class ContentGenerator:
    def __init__(self):
        self.templates = {
            "blog": self._get_blog_templates(),
            "landing_page": self._get_landing_templates(),
            "app_description": self._get_app_templates()
        }
        
    def generate(self, topic: str, content_type: str, keywords: List[str],
                 target_audience: str = "general", tone: str = "professional",
                 length: int = 500, category: str = "general") -> str:
        """Generate SEO-optimized content"""
        
        template = random.choice(self.templates.get(content_type, self.templates["blog"]))
        
        # Generate content based on type (pass category for more relevant output)
        if content_type == "blog":
            content = self._generate_blog(topic, keywords, template, tone, length, category)
        elif content_type == "landing_page":
            content = self._generate_landing_page(topic, keywords, template, tone, category)
        else:
            content = self._generate_app_description(topic, keywords, template, tone, category)
        
        return content
    
    def _generate_blog(self, topic: str, keywords: List[str], template: dict,
                       tone: str, length: int, category: str = "general") -> str:
        """Generate blog post"""
        
    # Title (make sure title contains category/topic)
    title = f"# {template['title_prefix']} {topic.title()} - {category.title()}: {template['title_suffix']}\n\n"
        
        # Introduction
    intro = f"## Introduction\n\n"
    intro += f"{template['intro_hook'].format(topic=topic, keyword=keywords[0])} "
    intro += f"In this comprehensive guide focused on {category} and {topic}, we'll explore everything you need to know about {topic}, "
    intro += f"including {', '.join(keywords[:3])}, and more.\n\n"
        
        # Main sections
        sections = []
        section_templates = [
            {
                "title": f"Understanding {topic.title()} and {keywords[0].title()}",
                "content": f"{keywords[0].title()} plays a crucial role in {topic}. "
                          f"By leveraging {keywords[1]} and {keywords[2]}, organizations in the {category} sector can "
                          f"achieve measurable improvements in their {topic} strategy. "
                          f"Industry case studies often report substantial gains when these approaches are applied."
            },
            {
                "title": f"Key Benefits of {topic.title()} for {category.title()}",
                "content": f"The advantages of focusing on {topic} for {category} organizations are numerous:\n\n"
                          f"- **Improved {keywords[0]}**: Strengthen domain-specific capabilities\n"
                          f"- **Advanced {keywords[1]}**: Streamline operations and insights\n"
                          f"- **Relevant {keywords[2]}**: Enhance user-facing value\n"
                          f"- **Sustainable Growth**: Build long-term success within {category}\n\n"
                          f"These benefits typically translate into better KPIs and market positioning."
            },
            {
                "title": "Best Practices and Strategies",
                "content": f"To maximize the impact of {topic} in {category}, consider these proven strategies:\n\n"
                          f"1. **Prioritize {keywords[0]}**: Establish a clear roadmap tailored to {category}\n"
                          f"2. **Integrate {keywords[1]}**: Use tools that map to your workflows\n"
                          f"3. **Monitor {keywords[2]}**: Create dashboards for ongoing optimization\n"
                          f"4. **Stay Updated**: Track sector-specific trends and regulations\n\n"
                          f"Applying these strategies in the context of {category} will produce better outcomes."
            },
            {
                "title": "Common Challenges and Solutions",
                "content": f"While working with {topic}, you may encounter challenges related to "
                          f"{keywords[0]} and {keywords[1]}. Here's how to overcome them:\n\n"
                          f"**Challenge**: Managing {keywords[0]} effectively\n"
                          f"**Solution**: Implement automated tools and processes\n\n"
                          f"**Challenge**: Optimizing {keywords[1]}\n"
                          f"**Solution**: Use data-driven decision making and A/B testing\n\n"
                          f"These solutions have been validated by industry leaders."
            },
            {
                "title": "Future Trends and Innovations",
                "content": f"The landscape of {topic} is constantly evolving. Emerging trends include:\n\n"
                          f"- AI-powered {keywords[0]} optimization\n"
                          f"- Advanced {keywords[1]} analytics\n"
                          f"- Integrated {keywords[2]} platforms\n"
                          f"- Real-time performance tracking\n\n"
                          f"Staying ahead of these trends will be crucial for maintaining competitive advantage."
            }
        ]
        
        # Use first 3 sections but ensure they reference topic/category dynamically
        for i, section in enumerate(section_templates[:3]):
            sections.append(f"## {section['title']}\n\n{section['content']}\n\n")
        
        # Conclusion
    conclusion = f"## Conclusion\n\n"
    conclusion += f"Mastering {topic} in the {category} space requires understanding {keywords[0]}, implementing effective "
    conclusion += f"{keywords[1]} strategies, and continuously optimizing {keywords[2]}. "
        conclusion += f"By following the best practices outlined in this guide, you can achieve "
        conclusion += f"significant improvements in your results and stay ahead of the competition.\n\n"
        conclusion += f"Ready to take your {topic} strategy to the next level? Start implementing these "
        conclusion += f"techniques today and watch your metrics improve.\n\n"
        
        # CTA
        cta = f"**Want to learn more about {keywords[0]} and {keywords[1]}?** "
        cta += f"Subscribe to our newsletter for weekly insights and expert tips.\n"
        
        content = title + intro + ''.join(sections) + conclusion + cta

        # Respect the requested length: if length is larger than output, add examples/expand sections
        if length and len(content.split()) < length:
            content = self._expand_content_by_length(content, topic, keywords, category, length)

        return content
    
    def _generate_landing_page(self, topic: str, keywords: List[str], 
                                template: dict, tone: str, category: str = "general") -> str:
        """Generate landing page content"""
        
        content = f"# {template['headline'].format(topic=topic.title())}\n\n"
        
        content += f"## {template['subheadline'].format(keyword=keywords[0])}\n\n"
        
        content += f"### Why Choose Our {topic.title()} Solution?\n\n"
        content += f"Transform your business with cutting-edge {keywords[0]} technology. "
        content += f"Our platform combines {keywords[1]} with {keywords[2]} to deliver "
        content += f"unmatched results.\n\n"
        
        content += f"#### Key Features:\n\n"
        content += f"✓ **Advanced {keywords[0]}** - Industry-leading capabilities\n"
        content += f"✓ **Seamless {keywords[1]}** - Easy integration\n"
        content += f"✓ **Powerful {keywords[2]}** - Drive real results\n"
        content += f"✓ **24/7 Support** - We're here when you need us\n\n"
        
        content += f"### Proven Results\n\n"
        content += f"- 95% customer satisfaction rate\n"
        content += f"- 3x average ROI improvement\n"
        content += f"- Used by 10,000+ businesses worldwide\n\n"
        
    content += f"### Get Started Today\n\n"
    content += f"Join thousands of successful {category} organizations using our {topic} solution. "
    content += f"Start your free trial now - no credit card required!\n\n"
        
        content += f"**[Start Free Trial]** | **[Watch Demo]** | **[Contact Sales]**\n"
        
        return content
    
    def _generate_app_description(self, topic: str, keywords: List[str],
                                   template: dict, tone: str, category: str = "general") -> str:
        """Generate app description"""
        
        content = f"# {topic.title()} - {template['tagline'].format(keyword=keywords[0])}\n\n"
        
        content += f"## Transform Your {keywords[0]} Experience\n\n"
        
        content += f"{topic.title()} is the ultimate solution for {keywords[0]}, {keywords[1]}, "
        content += f"and {keywords[2]}. Designed for both beginners and professionals, our app "
        content += f"delivers powerful features in an intuitive interface.\n\n"
        
        content += f"### ⭐ Top Features:\n\n"
        content += f"• **Smart {keywords[0]}** - AI-powered optimization\n"
        content += f"• **Real-time {keywords[1]}** - Stay updated instantly\n"
        content += f"• **Advanced {keywords[2]}** - Professional-grade tools\n"
        content += f"• **Cross-platform Sync** - Access anywhere, anytime\n"
        content += f"• **Offline Mode** - Work without internet\n"
        content += f"• **Secure & Private** - Your data is protected\n\n"
        
        content += f"### 💡 Why Users Love Us:\n\n"
        content += f'"Best {topic} app I\'ve used!" - 5 stars\n'
        content += f'"Game-changer for {keywords[0]}" - 5 stars\n'
        content += f'"Simple yet powerful" - 5 stars\n\n'
        
        content += f"### 🚀 Get Started in Minutes:\n\n"
        content += f"1. Download and install\n"
        content += f"2. Create your free account\n"
        content += f"3. Start optimizing your {keywords[0]}\n\n"
        
        content += f"Download now and join millions of satisfied users!\n"
        
        return content

    def _expand_content_by_length(self, content: str, topic: str, keywords: List[str], category: str, length: int) -> str:
        """Naive expansion: append examples, tips and mini-case studies until length reached."""
        extra_paragraphs = [
            f"Example: A {category} company implemented {keywords[0]} and saw clear gains in user engagement and retention.",
            f"Tip: When working on {topic}, focus on measurable KPIs (CTR, conversion rate) and iterate quickly.",
            f"Mini case study: Company X used {keywords[1]} to improve their workflow, leading to a 25% improvement in time-to-value.",
            f"How-to: Start by auditing current processes, prioritize quick wins, and scale successful experiments across teams.",
        ]

        idx = 0
        while len(content.split()) < length and idx < 50:
            content += "\n\n" + extra_paragraphs[idx % len(extra_paragraphs)]
            idx += 1

        return content
    
    def _get_blog_templates(self):
        return [
            {
                "title_prefix": "The Ultimate Guide to",
                "title_suffix": "in 2025",
                "intro_hook": "Are you looking to master {keyword}?"
            },
            {
                "title_prefix": "How to Optimize",
                "title_suffix": "for Maximum Results",
                "intro_hook": "Want to improve your {keyword} performance?"
            },
            {
                "title_prefix": "10 Proven Strategies for",
                "title_suffix": "Success",
                "intro_hook": "Discover the secrets to {keyword} excellence."
            }
        ]
    
    def _get_landing_templates(self):
        return [
            {
                "headline": "Transform Your Business with {topic}",
                "subheadline": "Unlock the Power of {keyword}"
            },
            {
                "headline": "The #1 {topic} Solution for Modern Businesses",
                "subheadline": "Boost Your {keyword} by 10x"
            }
        ]
    
    def _get_app_templates(self):
        return [
            {
                "tagline": "Your Personal {keyword} Assistant"
            },
            {
                "tagline": "Revolutionize Your {keyword}"
            }
        ]