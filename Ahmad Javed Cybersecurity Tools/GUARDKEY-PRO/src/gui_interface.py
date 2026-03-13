import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
try:
    import pyperclip
except ImportError:
    pyperclip = None
from .password_analyzer import PasswordStrengthAnalyzer

class PasswordAnalyzerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("GUARDKEY PRO")
        self.analyzer = PasswordStrengthAnalyzer()
        self.show_password = tk.BooleanVar(value=False)
        self.setup_ui()

    def setup_ui(self):
        main = ttk.Frame(self.root, padding="10")
        main.grid(row=0, column=0, sticky=(tk.W,tk.E,tk.N,tk.S))
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main.columnconfigure(1, weight=1)

        ttk.Label(main, text="Enter Password:", font=('Arial',12)).grid(row=0,column=0,sticky=tk.W)
        self.password_entry = ttk.Entry(main, width=40, show="*", font=('Arial',11))
        self.password_entry.grid(row=0,column=1,padx=5,sticky=(tk.W,tk.E))
        ttk.Checkbutton(main, text="Show", variable=self.show_password, command=self.toggle_show).grid(row=0,column=2)

        btn_frame = ttk.Frame(main)
        btn_frame.grid(row=1,column=0,columnspan=3,pady=10)
        ttk.Button(btn_frame, text="Analyze", command=self.analyze).pack(side=tk.LEFT,padx=5)
        ttk.Button(btn_frame, text="Clear", command=self.clear).pack(side=tk.LEFT,padx=5)
        ttk.Button(btn_frame, text="Generate", command=self.generate).pack(side=tk.LEFT,padx=5)
        ttk.Button(btn_frame, text="Copy", command=self.copy).pack(side=tk.LEFT,padx=5)

        res = ttk.LabelFrame(main, text="Results", padding="10")
        res.grid(row=2,column=0,columnspan=3,sticky=(tk.W,tk.E,tk.N,tk.S),pady=10)
        res.columnconfigure(0, weight=1)

        self.strength_var = tk.StringVar(value="Not analyzed")
        ttk.Label(res, textvariable=self.strength_var, font=('Arial',14,'bold')).grid(row=0,column=0)
        self.progress = ttk.Progressbar(res, length=400, mode='determinate')
        self.progress.grid(row=1,column=0,pady=10)

        details_frame = ttk.Frame(res)
        details_frame.grid(row=2,column=0,pady=10,sticky=(tk.W,tk.E))
        details_frame.columnconfigure(1, weight=1)

        self.details = {}
        items = [('Length:','length'),('Uppercase:','has_upper'),('Lowercase:','has_lower'),
                 ('Numbers:','has_digit'),('Symbols:','has_symbol'),('Entropy:','entropy'),
                 ('Crack Time:','crack_time')]
        for i,(label,key) in enumerate(items):
            ttk.Label(details_frame, text=label, font=('Arial',10,'bold')).grid(row=i,column=0,sticky=tk.W)
            self.details[key] = ttk.Label(details_frame, text="--", font=('Arial',10))
            self.details[key].grid(row=i,column=1,sticky=tk.W,padx=10)

        ttk.Label(res, text="Feedback:", font=('Arial',11,'bold')).grid(row=3,column=0,sticky=tk.W,pady=(10,5))
        self.feedback_text = scrolledtext.ScrolledText(res, height=5, wrap=tk.WORD)
        self.feedback_text.grid(row=4,column=0,sticky=(tk.W,tk.E),pady=5)

        ttk.Label(res, text="Recommendations:", font=('Arial',11,'bold')).grid(row=5,column=0,sticky=tk.W)
        self.rec_text = scrolledtext.ScrolledText(res, height=5, wrap=tk.WORD)
        self.rec_text.grid(row=6,column=0,sticky=(tk.W,tk.E),pady=5)

        self.status_var = tk.StringVar(value="Ready")
        ttk.Label(self.root, textvariable=self.status_var, relief=tk.SUNKEN, anchor=tk.W).grid(row=1,column=0,sticky=(tk.W,tk.E))

    def toggle_show(self):
        self.password_entry.config(show="" if self.show_password.get() else "*")

    def analyze(self):
        pwd = self.password_entry.get()
        if not pwd:
            messagebox.showwarning("Warning","Enter a password")
            return
        analysis = self.analyzer.analyze_password(pwd)
        rec = self.analyzer.generate_recommendations(analysis)
        self.update_results(analysis, rec)

    def update_results(self, analysis, rec):
        self.strength_var.set(f"Strength: {analysis['strength']} ({analysis['percentage']:.1f}%)")
        self.progress['value'] = analysis['percentage']
        d = analysis['details']
        self.details['length'].config(text=str(d['length']))
        self.details['has_upper'].config(text="✅ Yes" if d['has_upper'] else "❌ No")
        self.details['has_lower'].config(text="✅ Yes" if d['has_lower'] else "❌ No")
        self.details['has_digit'].config(text="✅ Yes" if d['has_digit'] else "❌ No")
        self.details['has_symbol'].config(text="✅ Yes" if d['has_symbol'] else "❌ No")
        self.details['entropy'].config(text=f"{d['entropy']} bits")
        self.details['crack_time'].config(text=d['crack_time'])

        self.feedback_text.delete(1.0, tk.END)
        for fb in analysis['feedback']:
            self.feedback_text.insert(tk.END, f"• {fb}\n")

        self.rec_text.delete(1.0, tk.END)
        for i,r in enumerate(rec,1):
            self.rec_text.insert(tk.END, f"{i}. {r}\n")
        self.status_var.set("Analysis complete")

    def generate(self):
        import secrets, string
        chars = string.ascii_letters + string.digits + "!@#$%^&*"
        pwd = ''.join(secrets.choice(chars) for _ in range(16))
        self.password_entry.delete(0, tk.END)
        self.password_entry.insert(0, pwd)
        self.status_var.set("Strong password generated")

    def copy(self):
        pwd = self.password_entry.get()
        if pyperclip is None:
            messagebox.showwarning("Warning", "Clipboard support requires pyperclip. Install requirements first.")
            return
        if pwd:
            pyperclip.copy(pwd)
            self.status_var.set("Copied to clipboard")
        else:
            messagebox.showwarning("Warning","No password to copy")

    def clear(self):
        self.password_entry.delete(0, tk.END)
        self.strength_var.set("Not analyzed")
        self.progress['value'] = 0
        for key in self.details:
            self.details[key].config(text="--")
        self.feedback_text.delete(1.0, tk.END)
        self.rec_text.delete(1.0, tk.END)
        self.status_var.set("Cleared")