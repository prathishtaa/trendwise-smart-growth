import { Home, Sparkles, TrendingUp, Clock, Settings } from "lucide-react";
import { NavLink } from "react-router-dom";
import { cn } from "@/lib/utils";

const DashboardSidebar = () => {
  const navItems = [
    { icon: Home, label: "Home", path: "/dashboard" },
    { icon: Sparkles, label: "Content Generator", path: "/dashboard/generator" },
    { icon: TrendingUp, label: "Trend Analytics", path: "/dashboard/analytics" },
    { icon: Clock, label: "Posting Insights", path: "/dashboard/insights" },
    { icon: Settings, label: "Settings", path: "/dashboard/settings" },
  ];

  return (
    <aside className="w-64 bg-card border-r border-border min-h-screen p-4">
      <div className="mb-8">
        <h1 className="text-2xl font-bold bg-gradient-to-r from-primary to-secondary bg-clip-text text-transparent">
          TrendWise
        </h1>
      </div>
      <nav className="space-y-2">
        {navItems.map((item) => (
          <NavLink
            key={item.path}
            to={item.path}
            end={item.path === "/dashboard"}
            className={({ isActive }) =>
              cn(
                "flex items-center gap-3 px-4 py-3 rounded-lg transition-all",
                isActive
                  ? "bg-primary text-primary-foreground shadow-[var(--shadow-glow)]"
                  : "hover:bg-muted text-muted-foreground hover:text-foreground"
              )
            }
          >
            <item.icon className="w-5 h-5" />
            <span className="font-medium">{item.label}</span>
          </NavLink>
        ))}
      </nav>
    </aside>
  );
};

export default DashboardSidebar;
