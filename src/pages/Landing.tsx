import { Button } from "@/components/ui/button";
import { Card, CardContent } from "@/components/ui/card";
import { Brain, TrendingUp, Clock, Search, ArrowRight, Sparkles } from "lucide-react";
import { Link } from "react-router-dom";
import heroImage from "@/assets/hero-bg.jpg";

const Landing = () => {
  const scrollToFeatures = () => {
    document.getElementById("features")?.scrollIntoView({ behavior: "smooth" });
  };

  return (
    <div className="min-h-screen bg-background">
      {/* Hero Section */}
      <section 
        className="relative min-h-screen flex items-center justify-center overflow-hidden"
        style={{
          backgroundImage: `linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.6)), url(${heroImage})`,
          backgroundSize: 'cover',
          backgroundPosition: 'center',
        }}
      >
        <div className="container px-4 py-32 mx-auto text-center relative z-10">
          <h1 className="text-5xl md:text-7xl font-bold text-white mb-6 animate-fade-in">
            Stay Ahead. Create Smarter. <br />
            <span className="bg-gradient-to-r from-[hsl(162,73%,66%)] to-[hsl(262,52%,67%)] bg-clip-text text-transparent">
              Grow Faster. 🚀
            </span>
          </h1>
          <p className="text-xl md:text-2xl text-gray-200 mb-12 max-w-3xl mx-auto">
            TrendWise helps you craft viral-ready posts and predicts the best times to publish — all powered by AI.
          </p>
          <div className="flex flex-col sm:flex-row gap-4 justify-center">
            <Button asChild size="lg" variant="gradient" className="text-lg">
              <Link to="/dashboard">
                Try Dashboard <ArrowRight className="ml-2" />
              </Link>
            </Button>
            <Button size="lg" variant="outline" className="text-lg bg-white/10 text-white border-white/30 hover:bg-white/20" onClick={scrollToFeatures}>
              Learn More
            </Button>
          </div>
        </div>
      </section>

      {/* Features Section */}
      <section id="features" className="py-24 bg-gradient-to-b from-background to-[hsl(162,73%,96%)]">
        <div className="container px-4 mx-auto">
          <h2 className="text-4xl md:text-5xl font-bold text-center mb-16">
            Everything You Need to Go <span className="text-primary">Viral</span>
          </h2>
          <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-8">
            <Card className="border-none shadow-[var(--shadow-card)] hover:shadow-[var(--shadow-glow)] transition-shadow">
              <CardContent className="pt-6">
                <Brain className="w-12 h-12 text-primary mb-4" />
                <h3 className="text-xl font-semibold mb-2">AI-Powered Content Creation</h3>
                <p className="text-muted-foreground">Generate posts, blogs, or captions from trends.</p>
              </CardContent>
            </Card>
            <Card className="border-none shadow-[var(--shadow-card)] hover:shadow-[var(--shadow-glow)] transition-shadow">
              <CardContent className="pt-6">
                <TrendingUp className="w-12 h-12 text-secondary mb-4" />
                <h3 className="text-xl font-semibold mb-2">Trend Forecasting</h3>
                <p className="text-muted-foreground">See what's gaining traction before others.</p>
              </CardContent>
            </Card>
            <Card className="border-none shadow-[var(--shadow-card)] hover:shadow-[var(--shadow-glow)] transition-shadow">
              <CardContent className="pt-6">
                <Clock className="w-12 h-12 text-primary mb-4" />
                <h3 className="text-xl font-semibold mb-2">Best Posting Time Predictor</h3>
                <p className="text-muted-foreground">Know when your audience is most active.</p>
              </CardContent>
            </Card>
            <Card className="border-none shadow-[var(--shadow-card)] hover:shadow-[var(--shadow-glow)] transition-shadow">
              <CardContent className="pt-6">
                <Search className="w-12 h-12 text-secondary mb-4" />
                <h3 className="text-xl font-semibold mb-2">SEO Keyword Insights</h3>
                <p className="text-muted-foreground">Get smart keyword suggestions to boost reach.</p>
              </CardContent>
            </Card>
          </div>
        </div>
      </section>

      {/* Demo Section */}
      <section className="py-24 bg-background">
        <div className="container px-4 mx-auto">
          <div className="max-w-4xl mx-auto">
            <h2 className="text-4xl md:text-5xl font-bold text-center mb-8">
              See It In <span className="text-primary">Action</span>
            </h2>
            <Card className="border-2 border-primary/20 shadow-[var(--shadow-glow)]">
              <CardContent className="p-8">
                <div className="space-y-6">
                  <div>
                    <label className="text-sm font-medium mb-2 block">Try it yourself:</label>
                    <div className="flex gap-2">
                      <input 
                        type="text" 
                        placeholder="Summarize the latest tech trends in AI wearables..." 
                        className="flex-1 px-4 py-3 border border-input rounded-lg bg-background"
                        defaultValue="Summarize the latest tech trends in AI wearables"
                      />
                      <Button variant="gradient" size="lg">
                        <Sparkles className="mr-2" />
                        Generate
                      </Button>
                    </div>
                  </div>
                  <div className="bg-muted p-6 rounded-lg">
                    <p className="font-medium mb-3">Generated Post:</p>
                    <p className="text-muted-foreground mb-4">
                      "🚀 AI wearables are transforming health tech! From smartwatches tracking vitals to AR glasses enhancing daily life—2025 is the year of intelligent accessories. #AIWearables #TechTrends #Innovation"
                    </p>
                    <div className="flex items-center gap-4 text-sm">
                      <span className="text-primary font-medium">📈 Predicted Engagement: 8.5/10</span>
                      <span className="text-secondary font-medium">🕒 Best Time: 6-8 PM</span>
                    </div>
                  </div>
                </div>
              </CardContent>
            </Card>
          </div>
        </div>
      </section>

      {/* Testimonials */}
      <section className="py-24 bg-gradient-to-b from-background to-[hsl(262,52%,96%)]">
        <div className="container px-4 mx-auto">
          <h2 className="text-4xl md:text-5xl font-bold text-center mb-16">
            Loved by <span className="text-secondary">Creators</span>
          </h2>
          <div className="grid md:grid-cols-3 gap-8 max-w-6xl mx-auto">
            {[
              { name: "Sarah Chen", role: "Tech Influencer", quote: "TrendWise saved hours of planning — now every post performs better!" },
              { name: "Marcus Johnson", role: "Content Creator", quote: "The AI predictions are incredibly accurate. My engagement has doubled!" },
              { name: "Elena Rodriguez", role: "Digital Marketer", quote: "Finally, a tool that understands what content will actually trend. Game changer!" }
            ].map((testimonial, i) => (
              <Card key={i} className="border-none shadow-[var(--shadow-card)]">
                <CardContent className="pt-6">
                  <p className="text-muted-foreground mb-4 italic">"{testimonial.quote}"</p>
                  <div>
                    <p className="font-semibold">{testimonial.name}</p>
                    <p className="text-sm text-muted-foreground">{testimonial.role}</p>
                  </div>
                </CardContent>
              </Card>
            ))}
          </div>
        </div>
      </section>

      {/* Footer */}
      <footer className="py-12 bg-foreground text-background">
        <div className="container px-4 mx-auto">
          <div className="flex flex-col md:flex-row justify-between items-center gap-6">
            <div className="text-2xl font-bold">TrendWise</div>
            <div className="flex gap-8 text-sm">
              <Link to="/" className="hover:text-primary transition-colors">Home</Link>
              <a href="#features" className="hover:text-primary transition-colors">Features</a>
              <Link to="/dashboard" className="hover:text-primary transition-colors">Dashboard</Link>
              <a href="#" className="hover:text-primary transition-colors">Contact</a>
              <a href="#" className="hover:text-primary transition-colors">Privacy</a>
            </div>
          </div>
          <div className="text-center mt-8 text-sm opacity-70">
            © TrendWise 2025. All rights reserved.
          </div>
        </div>
      </footer>
    </div>
  );
};

export default Landing;
