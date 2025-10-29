import { useState } from "react";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Sparkles, Copy, ThumbsUp } from "lucide-react";
import { toast } from "sonner";

const Generator = () => {
  const [selectedCategory, setSelectedCategory] = useState<string>("");
  const [prompt, setPrompt] = useState("");
  const [generatedContent, setGeneratedContent] = useState<any>(null);
  const [isGenerating, setIsGenerating] = useState(false);

  const categories = [
    { id: "tech", label: "Technology", icon: "💻" },
    { id: "health", label: "Healthcare", icon: "🏥" },
    { id: "politics", label: "Politics", icon: "🗳️" },
    { id: "cooking", label: "Cooking", icon: "🍳" },
    { id: "entertainment", label: "Entertainment", icon: "🎬" },
    { id: "custom", label: "Custom Query", icon: "✨" },
  ];

  const handleGenerate = () => {
    if (!prompt.trim() && selectedCategory !== "custom") {
      toast.error("Please enter a topic or select a category");
      return;
    }

    setIsGenerating(true);
    
    // Simulate AI generation
    setTimeout(() => {
      const mockContent = {
        post: `🚀 ${prompt || `Latest trends in ${selectedCategory}`} are reshaping the industry! Here's what you need to know:\n\n✨ Innovation is at an all-time high\n📈 Growth opportunities are everywhere\n💡 Smart strategies make all the difference\n\n#${selectedCategory || 'Trending'} #Innovation #GrowthMindset #2025Trends`,
        hashtags: ["#Innovation", "#Trending", `#${selectedCategory || 'AI'}`, "#GrowthMindset"],
        engagement: (Math.random() * 2 + 7).toFixed(1),
        bestTime: ["6:00 PM - 8:00 PM", "12:00 PM - 2:00 PM"],
        keywords: ["innovation", "growth", "strategy", "trends"],
      };
      
      setGeneratedContent(mockContent);
      setIsGenerating(false);
      toast.success("Content generated successfully!");
    }, 1500);
  };

  const copyToClipboard = () => {
    if (generatedContent) {
      navigator.clipboard.writeText(generatedContent.post);
      toast.success("Copied to clipboard!");
    }
  };

  return (
    <div className="space-y-8">
      <div>
        <h1 className="text-4xl font-bold mb-2">Content Generator 💡</h1>
        <p className="text-muted-foreground text-lg">Create smart, trend-optimized posts</p>
      </div>

      {/* Category Selection */}
      <Card className="border-none shadow-[var(--shadow-card)]">
        <CardHeader>
          <CardTitle>Select Category</CardTitle>
        </CardHeader>
        <CardContent>
          <div className="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-6 gap-4">
            {categories.map((category) => (
              <button
                key={category.id}
                onClick={() => setSelectedCategory(category.id)}
                className={`p-4 rounded-lg border-2 transition-all hover:scale-105 ${
                  selectedCategory === category.id
                    ? "border-primary bg-primary/10 shadow-[var(--shadow-glow)]"
                    : "border-border hover:border-primary/50"
                }`}
              >
                <div className="text-3xl mb-2">{category.icon}</div>
                <div className="text-sm font-medium">{category.label}</div>
              </button>
            ))}
          </div>
        </CardContent>
      </Card>

      {/* Input Section */}
      <Card className="border-none shadow-[var(--shadow-card)]">
        <CardHeader>
          <CardTitle>Content Topic</CardTitle>
        </CardHeader>
        <CardContent className="space-y-4">
          <textarea
            placeholder="Enter your content idea or topic... (e.g., 'AI wearables trends', 'healthy meal prep tips')"
            value={prompt}
            onChange={(e) => setPrompt(e.target.value)}
            className="w-full min-h-32 p-4 border border-input rounded-lg bg-background resize-none"
          />
          <Button 
            onClick={handleGenerate} 
            variant="gradient" 
            size="lg" 
            className="w-full md:w-auto"
            disabled={isGenerating}
          >
            <Sparkles className="mr-2" />
            {isGenerating ? "Generating..." : "Generate Content"}
          </Button>
        </CardContent>
      </Card>

      {/* Output Section */}
      {generatedContent && (
        <Card className="border-2 border-primary/20 shadow-[var(--shadow-glow)]">
          <CardHeader>
            <CardTitle className="flex items-center justify-between">
              <span>Generated Content</span>
              <Button variant="outline" size="sm" onClick={copyToClipboard}>
                <Copy className="w-4 h-4 mr-2" />
                Copy
              </Button>
            </CardTitle>
          </CardHeader>
          <CardContent className="space-y-6">
            <div>
              <h3 className="font-semibold mb-3 text-lg">Social Media Post:</h3>
              <div className="bg-muted p-6 rounded-lg whitespace-pre-wrap">
                {generatedContent.post}
              </div>
            </div>

            <div className="grid md:grid-cols-2 gap-6">
              <div>
                <h3 className="font-semibold mb-3 flex items-center gap-2">
                  <ThumbsUp className="w-5 h-5 text-primary" />
                  Predicted Engagement
                </h3>
                <div className="bg-gradient-to-r from-primary/10 to-secondary/10 p-4 rounded-lg">
                  <div className="text-3xl font-bold text-primary">
                    {generatedContent.engagement}/10
                  </div>
                  <p className="text-sm text-muted-foreground mt-1">
                    Expected high engagement
                  </p>
                </div>
              </div>

              <div>
                <h3 className="font-semibold mb-3">Best Posting Times 🕒</h3>
                <div className="space-y-2">
                  {generatedContent.bestTime.map((time: string, i: number) => (
                    <div key={i} className="bg-secondary/10 p-3 rounded-lg text-secondary font-medium">
                      {time}
                    </div>
                  ))}
                </div>
              </div>
            </div>

            <div>
              <h3 className="font-semibold mb-3">Recommended Keywords</h3>
              <div className="flex flex-wrap gap-2">
                {generatedContent.keywords.map((keyword: string, i: number) => (
                  <span
                    key={i}
                    className="px-3 py-1 bg-primary/10 text-primary rounded-full text-sm font-medium"
                  >
                    {keyword}
                  </span>
                ))}
              </div>
            </div>
          </CardContent>
        </Card>
      )}
    </div>
  );
};

export default Generator;
