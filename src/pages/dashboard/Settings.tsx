import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Bell, User, Lock, Palette } from "lucide-react";

const Settings = () => {
  return (
    <div className="space-y-8">
      <div>
        <h1 className="text-4xl font-bold mb-2">Settings ⚙️</h1>
        <p className="text-muted-foreground text-lg">Manage your preferences and account</p>
      </div>

      <div className="grid lg:grid-cols-2 gap-6">
        <Card className="border-none shadow-[var(--shadow-card)]">
          <CardHeader>
            <CardTitle className="flex items-center gap-2">
              <User className="w-5 h-5" />
              Profile Settings
            </CardTitle>
          </CardHeader>
          <CardContent className="space-y-4">
            <div>
              <label className="text-sm font-medium mb-2 block">Display Name</label>
              <input
                type="text"
                defaultValue="Content Creator"
                className="w-full px-4 py-2 border border-input rounded-lg bg-background"
              />
            </div>
            <div>
              <label className="text-sm font-medium mb-2 block">Email</label>
              <input
                type="email"
                defaultValue="creator@trendwise.com"
                className="w-full px-4 py-2 border border-input rounded-lg bg-background"
              />
            </div>
            <Button variant="default">Save Changes</Button>
          </CardContent>
        </Card>

        <Card className="border-none shadow-[var(--shadow-card)]">
          <CardHeader>
            <CardTitle className="flex items-center gap-2">
              <Bell className="w-5 h-5" />
              Notifications
            </CardTitle>
          </CardHeader>
          <CardContent className="space-y-4">
            <div className="flex items-center justify-between">
              <div>
                <p className="font-medium">Trend Alerts</p>
                <p className="text-sm text-muted-foreground">Get notified about new trends</p>
              </div>
              <input type="checkbox" defaultChecked className="w-5 h-5" />
            </div>
            <div className="flex items-center justify-between">
              <div>
                <p className="font-medium">Performance Updates</p>
                <p className="text-sm text-muted-foreground">Weekly engagement reports</p>
              </div>
              <input type="checkbox" defaultChecked className="w-5 h-5" />
            </div>
            <div className="flex items-center justify-between">
              <div>
                <p className="font-medium">Best Time Reminders</p>
                <p className="text-sm text-muted-foreground">Posting time suggestions</p>
              </div>
              <input type="checkbox" className="w-5 h-5" />
            </div>
          </CardContent>
        </Card>

        <Card className="border-none shadow-[var(--shadow-card)]">
          <CardHeader>
            <CardTitle className="flex items-center gap-2">
              <Lock className="w-5 h-5" />
              Privacy & Security
            </CardTitle>
          </CardHeader>
          <CardContent className="space-y-4">
            <Button variant="outline" className="w-full justify-start">
              Change Password
            </Button>
            <Button variant="outline" className="w-full justify-start">
              Two-Factor Authentication
            </Button>
            <Button variant="outline" className="w-full justify-start">
              Connected Accounts
            </Button>
          </CardContent>
        </Card>

        <Card className="border-none shadow-[var(--shadow-card)]">
          <CardHeader>
            <CardTitle className="flex items-center gap-2">
              <Palette className="w-5 h-5" />
              Appearance
            </CardTitle>
          </CardHeader>
          <CardContent className="space-y-4">
            <div>
              <label className="text-sm font-medium mb-2 block">Theme</label>
              <select className="w-full px-4 py-2 border border-input rounded-lg bg-background">
                <option>Light</option>
                <option>Dark</option>
                <option>System</option>
              </select>
            </div>
            <div>
              <label className="text-sm font-medium mb-2 block">Language</label>
              <select className="w-full px-4 py-2 border border-input rounded-lg bg-background">
                <option>English</option>
                <option>Spanish</option>
                <option>French</option>
              </select>
            </div>
          </CardContent>
        </Card>
      </div>
    </div>
  );
};

export default Settings;
