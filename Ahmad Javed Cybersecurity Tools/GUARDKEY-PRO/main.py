#!/usr/bin/env python3
"""
GUARDKEY PRO - Password Strength Analyzer
Created by AJ
"""

import tkinter as tk
from tkinter import ttk
import os
import time
from colorama import init, Fore, Style

init(autoreset=True)
from src.gui_interface import PasswordAnalyzerGUI

class SplashScreen:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("GUARDKEY PRO")
        self.root.overrideredirect(True)
        sw = self.root.winfo_screenwidth()
        sh = self.root.winfo_screenheight()
        w, h = 700, 500
        x = (sw - w)//2
        y = (sh - h)//2
        self.root.geometry(f'{w}x{h}+{x}+{y}')
        self.root.configure(bg='#1a1a2e')
        self.canvas = tk.Canvas(self.root, width=w, height=h, bg='#1a1a2e', highlightthickness=0)
        self.canvas.pack()
        self.colors = {'primary':'#00d4ff','secondary':'#7b2cbf','accent':'#ff006e',
                       'success':'#06d6a0','warning':'#ffd166','text':'#ffffff'}
        self.pulse = 0
        self.angle = 0
        self._after_id = None
        self.animate()          # start animation, but do not enter mainloop yet

    def show(self):
        """Start the splash screen main loop and close after 3 seconds."""
        self.root.after(3000, self.fade_out)
        self.root.mainloop()

    def draw_gradient(self):
        w, h = 700, 500
        for i in range(h):
            r = int(26 + 20*i/h)
            g = int(26 + 30*i/h)
            b = int(46 + 40*i/h)
            self.canvas.create_line(0,i,w,i, fill=f'#{r:02x}{g:02x}{b:02x}')

    def draw_shield(self, x, y, size=100):
        s = size + 10*self.pulse
        pts = [x, y-s//2, x+s//2, y-s//4, x+s//2, y+s//4, x, y+s//2, x-s//2, y+s//4, x-s//2, y-s//4]
        self.canvas.create_polygon(pts, fill='#2a2a4a', outline=self.colors['primary'], width=3)
        self.canvas.create_rectangle(x-20, y-10, x+20, y+15, fill=self.colors['secondary'], outline=self.colors['accent'], width=2)
        self.canvas.create_arc(x-15, y-30, x+15, y-10, start=0, extent=180, fill=self.colors['secondary'], outline=self.colors['accent'], width=2)
        self.canvas.create_oval(x-5, y, x+5, y+10, fill='black', outline=self.colors['accent'])

    def draw_title(self):
        self.canvas.create_text(350,180, text="GUARDKEY PRO", font=('Arial Black',36,'bold'), fill=self.colors['primary'])
        self.canvas.create_text(350,240, text="Password Security Reimagined", font=('Arial',18,'italic'), fill=self.colors['success'])
        self.canvas.create_text(350,300, text="⭐ BY AJ ⭐", font=('Arial',24,'bold'), fill=self.colors['accent'])

    def draw_features(self):
        feats = ["🔐 Real-time Analysis","📊 Entropy Calculation","⚡ Crack Time Estimation",
                 "🛡️ Pattern Detection","🎯 Strong Password Generator"]
        for i,f in enumerate(feats):
            self.canvas.create_text(350, 350+i*25, text=f, font=('Arial',11), fill='white')

    def draw_progress(self):
        self.canvas.create_rectangle(150,450,550,470, fill='#333', outline=self.colors['primary'], width=2)
        w = int(400*self.pulse)
        self.canvas.create_rectangle(150,450,150+w,470, fill=self.colors['secondary'])
        self.canvas.create_text(350,460, text=f"Loading... {int(self.pulse*100)}%", fill='white', font=('Arial',10,'bold'))

    def animate(self):
        if not self.root.winfo_exists():
            return
        self.pulse = (self.pulse + 0.01) % 1.0
        self.angle += 5
        self.canvas.delete("all")
        self.draw_gradient()
        self.draw_shield(350,100,80)
        self.draw_title()
        self.draw_features()
        self.draw_progress()
        self._after_id = self.root.after(50, self.animate)

    def fade_out(self):
        if self._after_id is not None:
            try:
                self.root.after_cancel(self._after_id)
            except tk.TclError:
                pass
        for i in range(10,-1,-1):
            self.root.attributes('-alpha', i/10)
            time.sleep(0.05)
        self.root.destroy()

def display_banner():
    os.system('cls' if os.name=='nt' else 'clear')
    banner = f'''
{Fore.CYAN}{Style.BRIGHT}╔═══════════════════════════════════════════════════════════════════╗
║                                                                   ║
║     ██████╗ ██╗   ██╗ █████╗ ██████╗ ██╗  ██╗███████╗██╗   ██╗  ║
║    ██╔════╝ ██║   ██║██╔══██╗██╔══██╗██║ ██╔╝██╔════╝╚██╗ ██╔╝  ║
║    ██║  ███╗██║   ██║███████║██████╔╝█████╔╝ █████╗   ╚████╔╝   ║
║    ██║   ██║██║   ██║██╔══██║██╔══██╗██╔═██╗ ██╔══╝    ╚██╔╝    ║
║    ╚██████╔╝╚██████╔╝██║  ██║██║  ██║██║  ██╗███████╗   ██║     ║
║     ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝   ╚═╝     ║
║                                                                   ║
║                    {Fore.YELLOW}🔐 GUARDKEY PRO 🔐{Fore.CYAN}                   ║
║                                                                   ║
║                         {Fore.MAGENTA}⭐ BY AJ ⭐{Fore.CYAN}                         ║
║                                                                   ║
║            {Fore.GREEN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{Fore.CYAN}              ║
║              {Fore.WHITE}Analyze • Evaluate • Secure • Protect{Fore.CYAN}               ║
║            {Fore.GREEN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{Fore.CYAN}              ║
║                                                                   ║
║              {Fore.BLUE}🛡️ Your Digital Security Companion 🛡️{Fore.CYAN}               ║
║                                                                   ║
╚═══════════════════════════════════════════════════════════════════╝{Fore.RESET}
'''
    print(banner)
    print(f"{Fore.YELLOW}═══════════════════════════════════════════════════════════════════")
    print(f"{Fore.GREEN}🚀 Version: 1.0.0 | {Fore.CYAN}Python 3.6+ | {Fore.MAGENTA}Professional Edition")
    print(f"{Fore.YELLOW}═══════════════════════════════════════════════════════════════════{Fore.RESET}\n")
    print(f"{Fore.WHITE}Initializing GUARDKEY PRO", end="")
    for _ in range(3):
        time.sleep(0.3)
        print(f"{Fore.YELLOW}.", end="", flush=True)
    print(f"{Fore.GREEN} Ready!\n{Fore.RESET}")

def main():
    display_banner()
    print(f"{Fore.MAGENTA}══════ SYSTEM STATUS ══════{Fore.RESET}\n")
    modules = [("🔐 Password Analyzer","Loaded"),("📊 Entropy Calculator","Loaded"),
               ("🎨 GUI Interface","Initializing"),("🛡️ Security Module","Active"),
               ("⚡ Pattern Detector","Ready"),("🔑 Password Generator","Online")]
    for mod,stat in modules:
        time.sleep(0.2)
        if stat in ("Loaded","Ready","Online","Active"):
            print(f"{Fore.GREEN}✓ {mod}: {stat}{Fore.RESET}")
        else:
            print(f"{Fore.YELLOW}ℹ {mod}: {stat}{Fore.RESET}")
    time.sleep(0.3)
    print(f"\n{Fore.GREEN}✓ All systems operational{Fore.RESET}")
    print(f"{Fore.CYAN}ℹ GUARDKEY PRO Version 1.0.0{Fore.RESET}")
    print(f"{Fore.CYAN}ℹ Created by AJ{Fore.RESET}")
    print(f"\n{Fore.CYAN}{'='*60}")
    print(f"{Fore.WHITE}🚀 Launching GUARDKEY PRO Interface...")
    print(f"{Fore.CYAN}{'='*60}{Fore.RESET}\n")

    # Run splash on the main thread to avoid Tkinter threading errors.
    splash = SplashScreen()
    splash.show()

    root = tk.Tk()
    root.title("🔐 GUARDKEY PRO - Password Strength Analyzer | Created by AJ")
    root.geometry("750x850")
    root.minsize(650,750)

    style = ttk.Style()
    style.theme_use('clam')
    style.configure('Accent.TButton', foreground='white', background='#00d4ff', font=('Arial',11,'bold'))

    app = PasswordAnalyzerGUI(root)
    app.status_var.set("🔐 GUARDKEY PRO | By AJ | Ready to analyze passwords")

    root.update_idletasks()
    print(f"{Fore.GREEN}✓ GUI initialized successfully{Fore.RESET}")
    print(f"{Fore.MAGENTA}\n══════ READY ══════{Fore.RESET}\n")
    print(f"{Fore.GREEN}✨ GUARDKEY PRO is now running!{Fore.RESET}")
    print(f"{Fore.WHITE}💡 Tip: Enter a password to analyze its strength{Fore.RESET}")
    print(f"{Fore.CYAN}{'='*60}{Fore.RESET}\n")

    root.mainloop()

if __name__ == "__main__":
    try:
        main()
    except ImportError as e:
        print(Fore.RED + f"\n✗ Missing module: {e}\nPlease install requirements: pip install -r requirements.txt")
    except Exception as e:
        print(Fore.RED + f"\n✗ Error: {e}")   # removed extra parenthesis