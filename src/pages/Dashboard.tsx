import { Outlet } from "react-router-dom";
import DashboardSidebar from "@/components/DashboardSidebar";

const Dashboard = () => {
  return (
    <div className="flex min-h-screen w-full">
      <DashboardSidebar />
      <main className="flex-1 p-8 bg-background">
        <Outlet />
      </main>
    </div>
  );
};

export default Dashboard;
