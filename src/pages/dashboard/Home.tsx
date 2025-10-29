import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { TrendingUp, Zap, Users, Target } from "lucide-react";
import { Button } from "@/components/ui/button";
import { Link } from "react-router-dom";

const DashboardHome = () => {
  return (
    <div className="space-y-8">
      <div>
        <h1 className="text-4xl font-bold mb-2">Welcome Back! 👋</h1>
        <p className="text-muted-foreground text-lg">Here's what's trending in your world</p>
      </div>

      {/* Stats Grid */}
      <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-6">
        <Card className="border-none shadow-[var(--shadow-card)]">
          <CardHeader className="flex flex-row items-center justify-between pb-2">
            <CardTitle className="text-sm font-medium text-muted-foreground">Total Posts</CardTitle>
            <Zap className="w-4 h-4 text-primary" />
          </CardHeader>
          <CardContent>
            <div className="text-3xl font-bold">127</div>
            <p className="text-xs text-muted-foreground mt-1">+12% from last month</p>
          </CardContent>
        </Card>

        <Card className="border-none shadow-[var(--shadow-card)]">
          <CardHeader className="flex flex-row items-center justify-between pb-2">
            <CardTitle className="text-sm font-medium text-muted-foreground">Engagement Rate</CardTitle>
            <TrendingUp className="w-4 h-4 text-secondary" />
          </CardHeader>
          <CardContent>
            <div className="text-3xl font-bold">8.4/10</div>
            <p className="text-xs text-muted-foreground mt-1">+0.8 from last week</p>
          </CardContent>
        </Card>

        <Card className="border-none shadow-[var(--shadow-card)]">
          <CardHeader className="flex flex-row items-center justify-between pb-2">
            <CardTitle className="text-sm font-medium text-muted-foreground">Active Trends</CardTitle>
            <Target className="w-4 h-4 text-primary" />
          </CardHeader>
          <CardContent>
            <div className="text-3xl font-bold">23</div>
            <p className="text-xs text-muted-foreground mt-1">Across 5 categories</p>
          </CardContent>
        </Card>

        <Card className="border-none shadow-[var(--shadow-card)]">
          <CardHeader className="flex flex-row items-center justify-between pb-2">
            <CardTitle className="text-sm font-medium text-muted-foreground">Reach</CardTitle>
            <Users className="w-4 h-4 text-secondary" />
          </CardHeader>
          <CardContent>
            <div className="text-3xl font-bold">45.2K</div>
            <p className="text-xs text-muted-foreground mt-1">+18% this month</p>
          </CardContent>
        </Card>
      </div>

      {/* Quick Actions */}
      <Card className="border-none shadow-[var(--shadow-card)]">
        <CardHeader>
          <CardTitle>Quick Actions</CardTitle>
        </CardHeader>
        <CardContent className="flex flex-wrap gap-4">
          <Button asChild variant="gradient">
            <Link to="/dashboard/generator">Generate New Post</Link>
          </Button>
          <Button asChild variant="outline">
            <Link to="/dashboard/analytics">View Trends</Link>
          </Button>
          <Button asChild variant="outline">
            <Link to="/dashboard/insights">Check Best Times</Link>
          </Button>
        </CardContent>
      </Card>

      {/* Trending Now */}
      <Card className="border-none shadow-[var(--shadow-card)]">
        <CardHeader>
          <CardTitle>Trending Now 🔥</CardTitle>
        </CardHeader>
        <CardContent>
          <div className="space-y-4">
            {[
              { topic: "AI Wearables", category: "Technology", engagement: "9.2/10", trend: "↑ 45%" },
              { topic: "Plant-Based Recipes", category: "Cooking", engagement: "8.7/10", trend: "↑ 32%" },
              { topic: "Remote Work Tools", category: "Technology", engagement: "8.5/10", trend: "↑ 28%" },
            ].map((item, i) => (
              <div key={i} className="flex items-center justify-between p-4 bg-muted rounded-lg">
                <div>
                  <p className="font-semibold">{item.topic}</p>
                  <p className="text-sm text-muted-foreground">{item.category}</p>
                </div>
                <div className="text-right">
                  <p className="font-medium text-primary">{item.engagement}</p>
                  <p className="text-sm text-secondary">{item.trend}</p>
                </div>
              </div>
            ))}
          </div>
        </CardContent>
      </Card>
    </div>
  );
};

export default DashboardHome;
