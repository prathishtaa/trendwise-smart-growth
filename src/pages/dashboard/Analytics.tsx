import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { TrendingUp, TrendingDown } from "lucide-react";

const Analytics = () => {
  const trendingTopics = [
    { topic: "AI & Machine Learning", category: "Technology", growth: "+156%", trend: "up", engagement: "9.4/10" },
    { topic: "Sustainable Living", category: "Lifestyle", growth: "+89%", trend: "up", engagement: "8.8/10" },
    { topic: "Mental Health Awareness", category: "Healthcare", growth: "+67%", trend: "up", engagement: "8.5/10" },
    { topic: "Remote Work Solutions", category: "Technology", growth: "+45%", trend: "up", engagement: "8.2/10" },
    { topic: "Plant-Based Nutrition", category: "Cooking", growth: "+38%", trend: "up", engagement: "7.9/10" },
    { topic: "Traditional Media", category: "Entertainment", growth: "-12%", trend: "down", engagement: "6.2/10" },
  ];

  const categoryPerformance = [
    { category: "Technology", posts: 45, engagement: 8.9, reach: "12.3K" },
    { category: "Healthcare", posts: 28, engagement: 8.4, reach: "8.7K" },
    { category: "Cooking", posts: 22, engagement: 8.1, reach: "6.4K" },
    { category: "Politics", posts: 18, engagement: 7.5, reach: "5.1K" },
    { category: "Entertainment", posts: 14, engagement: 7.2, reach: "4.2K" },
  ];

  return (
    <div className="space-y-8">
      <div>
        <h1 className="text-4xl font-bold mb-2">Trend Analytics 📈</h1>
        <p className="text-muted-foreground text-lg">Real-time insights into what's trending</p>
      </div>

      {/* Trending Topics */}
      <Card className="border-none shadow-[var(--shadow-card)]">
        <CardHeader>
          <CardTitle>Top Trending Topics</CardTitle>
        </CardHeader>
        <CardContent>
          <div className="space-y-4">
            {trendingTopics.map((item, i) => (
              <div
                key={i}
                className="flex items-center justify-between p-4 bg-gradient-to-r from-muted to-transparent rounded-lg hover:shadow-[var(--shadow-glow)] transition-shadow"
              >
                <div className="flex items-center gap-4">
                  <div className="text-2xl font-bold text-muted-foreground">#{i + 1}</div>
                  <div>
                    <p className="font-semibold text-lg">{item.topic}</p>
                    <p className="text-sm text-muted-foreground">{item.category}</p>
                  </div>
                </div>
                <div className="flex items-center gap-6">
                  <div className="text-right">
                    <p className="font-medium text-primary">{item.engagement}</p>
                    <p className="text-xs text-muted-foreground">Engagement</p>
                  </div>
                  <div
                    className={`flex items-center gap-2 px-4 py-2 rounded-full font-semibold ${
                      item.trend === "up"
                        ? "bg-primary/10 text-primary"
                        : "bg-destructive/10 text-destructive"
                    }`}
                  >
                    {item.trend === "up" ? (
                      <TrendingUp className="w-4 h-4" />
                    ) : (
                      <TrendingDown className="w-4 h-4" />
                    )}
                    {item.growth}
                  </div>
                </div>
              </div>
            ))}
          </div>
        </CardContent>
      </Card>

      {/* Category Performance */}
      <Card className="border-none shadow-[var(--shadow-card)]">
        <CardHeader>
          <CardTitle>Performance by Category</CardTitle>
        </CardHeader>
        <CardContent>
          <div className="overflow-x-auto">
            <table className="w-full">
              <thead>
                <tr className="border-b border-border">
                  <th className="text-left py-3 px-4 font-semibold">Category</th>
                  <th className="text-left py-3 px-4 font-semibold">Posts</th>
                  <th className="text-left py-3 px-4 font-semibold">Avg. Engagement</th>
                  <th className="text-left py-3 px-4 font-semibold">Total Reach</th>
                </tr>
              </thead>
              <tbody>
                {categoryPerformance.map((item, i) => (
                  <tr key={i} className="border-b border-border hover:bg-muted/50 transition-colors">
                    <td className="py-4 px-4 font-medium">{item.category}</td>
                    <td className="py-4 px-4">{item.posts}</td>
                    <td className="py-4 px-4">
                      <span className="px-3 py-1 bg-primary/10 text-primary rounded-full text-sm font-medium">
                        {item.engagement}/10
                      </span>
                    </td>
                    <td className="py-4 px-4 font-medium text-secondary">{item.reach}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </CardContent>
      </Card>

      {/* Engagement Chart Placeholder */}
      <Card className="border-none shadow-[var(--shadow-card)]">
        <CardHeader>
          <CardTitle>Engagement Over Time</CardTitle>
        </CardHeader>
        <CardContent>
          <div className="h-64 bg-gradient-to-br from-primary/5 to-secondary/5 rounded-lg flex items-center justify-center">
            <div className="text-center text-muted-foreground">
              <TrendingUp className="w-16 h-16 mx-auto mb-4 opacity-50" />
              <p className="text-lg">Chart visualization coming soon</p>
              <p className="text-sm">Real-time engagement tracking</p>
            </div>
          </div>
        </CardContent>
      </Card>
    </div>
  );
};

export default Analytics;
