import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Clock, Calendar, Users, Zap } from "lucide-react";

const Insights = () => {
  const bestTimes = [
    { day: "Monday", times: ["8:00 AM - 10:00 AM", "6:00 PM - 8:00 PM"], engagement: "8.7/10" },
    { day: "Tuesday", times: ["12:00 PM - 2:00 PM", "7:00 PM - 9:00 PM"], engagement: "8.9/10" },
    { day: "Wednesday", times: ["9:00 AM - 11:00 AM", "5:00 PM - 7:00 PM"], engagement: "9.1/10" },
    { day: "Thursday", times: ["1:00 PM - 3:00 PM", "6:00 PM - 8:00 PM"], engagement: "8.8/10" },
    { day: "Friday", times: ["10:00 AM - 12:00 PM", "4:00 PM - 6:00 PM"], engagement: "9.3/10" },
    { day: "Saturday", times: ["11:00 AM - 1:00 PM", "7:00 PM - 9:00 PM"], engagement: "8.4/10" },
    { day: "Sunday", times: ["2:00 PM - 4:00 PM", "8:00 PM - 10:00 PM"], engagement: "7.9/10" },
  ];

  const audienceInsights = [
    { metric: "Peak Activity Hours", value: "6:00 PM - 8:00 PM", icon: Clock, color: "primary" },
    { metric: "Most Active Day", value: "Friday", icon: Calendar, color: "secondary" },
    { metric: "Active Followers", value: "12.4K", icon: Users, color: "primary" },
    { metric: "Response Rate", value: "68%", icon: Zap, color: "secondary" },
  ];

  return (
    <div className="space-y-8">
      <div>
        <h1 className="text-4xl font-bold mb-2">Posting Insights 🕒</h1>
        <p className="text-muted-foreground text-lg">Optimize your posting schedule for maximum reach</p>
      </div>

      {/* Key Metrics */}
      <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-6">
        {audienceInsights.map((item, i) => (
          <Card key={i} className="border-none shadow-[var(--shadow-card)]">
            <CardContent className="pt-6">
              <div className="flex items-center justify-between mb-2">
                <item.icon className={`w-8 h-8 text-${item.color}`} />
                <span className={`text-2xl font-bold text-${item.color}`}>{item.value}</span>
              </div>
              <p className="text-sm text-muted-foreground">{item.metric}</p>
            </CardContent>
          </Card>
        ))}
      </div>

      {/* Best Posting Times */}
      <Card className="border-none shadow-[var(--shadow-card)]">
        <CardHeader>
          <CardTitle>Best Posting Times by Day</CardTitle>
        </CardHeader>
        <CardContent>
          <div className="space-y-4">
            {bestTimes.map((item, i) => (
              <div
                key={i}
                className="p-4 bg-gradient-to-r from-muted to-transparent rounded-lg hover:shadow-[var(--shadow-glow)] transition-shadow"
              >
                <div className="flex items-center justify-between mb-3">
                  <h3 className="font-semibold text-lg">{item.day}</h3>
                  <span className="px-3 py-1 bg-primary/10 text-primary rounded-full text-sm font-medium">
                    {item.engagement}
                  </span>
                </div>
                <div className="flex flex-wrap gap-2">
                  {item.times.map((time, j) => (
                    <div
                      key={j}
                      className="px-4 py-2 bg-secondary/10 text-secondary rounded-lg font-medium text-sm"
                    >
                      🕐 {time}
                    </div>
                  ))}
                </div>
              </div>
            ))}
          </div>
        </CardContent>
      </Card>

      {/* Recommendations */}
      <Card className="border-2 border-primary/20 shadow-[var(--shadow-glow)]">
        <CardHeader>
          <CardTitle className="flex items-center gap-2">
            <Zap className="w-6 h-6 text-primary" />
            AI Recommendations
          </CardTitle>
        </CardHeader>
        <CardContent className="space-y-4">
          <div className="p-4 bg-primary/5 rounded-lg border-l-4 border-primary">
            <h4 className="font-semibold mb-2">📈 Post between 6-8 PM for best reach</h4>
            <p className="text-sm text-muted-foreground">
              Your audience is most active during evening hours, especially on weekdays.
            </p>
          </div>
          <div className="p-4 bg-secondary/5 rounded-lg border-l-4 border-secondary">
            <h4 className="font-semibold mb-2">🎯 Focus on Friday content</h4>
            <p className="text-sm text-muted-foreground">
              Friday shows the highest engagement rates. Consider planning your key content for this day.
            </p>
          </div>
          <div className="p-4 bg-primary/5 rounded-lg border-l-4 border-primary">
            <h4 className="font-semibold mb-2">💡 Avoid Sunday late nights</h4>
            <p className="text-sm text-muted-foreground">
              Engagement drops significantly after 10 PM on Sundays. Schedule posts earlier in the day.
            </p>
          </div>
        </CardContent>
      </Card>
    </div>
  );
};

export default Insights;
