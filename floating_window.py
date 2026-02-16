import customtkinter as ctk
import queue

class FloatingWindow:
    def __init__(self):
        self.queue = queue.Queue()
        
        # Set appearance and theme
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")
        
        self.root = ctk.CTk()
        self.root.title("AI Assistant")
        
        # Window configuration
        self.root.geometry("500x380+880+140")
        self.root.attributes("-topmost", True)
        self.root.attributes("-alpha", 0.98)
        
        # Mac-specific: handle window transparency properly if needed
        # self.root.wm_attributes("-transparent", True) # Sometimes buggy
        
        # Main Outer Frame with rounded corners
        self.main_container = ctk.CTkFrame(
            self.root, 
            corner_radius=20, 
            fg_color="#0f1115", 
            border_width=2, 
            border_color="#1f2937"
        )
        self.main_container.pack(fill="both", expand=True, padx=10, pady=10)
        
        # ===== Header =====
        self.header = ctk.CTkFrame(self.main_container, fg_color="transparent")
        self.header.pack(fill="x", pady=(20, 10), padx=25)
        
        self.title_container = ctk.CTkFrame(self.header, fg_color="transparent")
        self.title_container.pack(side="left")
        
        self.title_label = ctk.CTkLabel(
            self.title_container, 
            text="AI ASSISTANT", 
            font=ctk.CTkFont(family="SF Pro Display", size=20, weight="bold"),
            text_color="#60a5fa" # Soft neon blue
        )
        self.title_label.pack(side="left")
        
        # Status indicator
        self.status_container = ctk.CTkFrame(self.header, fg_color="transparent")
        self.status_container.pack(side="right")
        
        self.status_dot = ctk.CTkLabel(
            self.status_container,
            text="●",
            font=ctk.CTkFont(size=14),
            text_color="#22c55e" # Pulse green
        )
        self.status_dot.pack(side="left", padx=(0, 5))
        
        self.status_label = ctk.CTkLabel(
            self.status_container,
            text="ACTIVE",
            font=ctk.CTkFont(family="SF Pro Display", size=12, weight="bold"),
            text_color="#9ca3af"
        )
        self.status_label.pack(side="left")
        
        # ===== Content Area =====
        self.text_frame = ctk.CTkFrame(
            self.main_container, 
            fg_color="#181a1f", 
            corner_radius=15,
            border_width=1,
            border_color="#2d3748"
        )
        self.text_frame.pack(expand=True, fill="both", padx=20, pady=10)
        
        self.text_area = ctk.CTkTextbox(
            self.text_frame,
            fg_color="transparent",
            text_color="#e5e7eb",
            font=ctk.CTkFont(family="SF Pro Text", size=15),
            padx=15,
            pady=15,
            wrap="word",
            border_width=0
        )
        self.text_area.pack(expand=True, fill="both")
        self.text_area.configure(state="disabled")
        
        # ===== Footer =====
        self.footer = ctk.CTkFrame(self.main_container, fg_color="transparent")
        self.footer.pack(fill="x", side="bottom", pady=(5, 20), padx=25)
        
        self.hint_label = ctk.CTkLabel(
            self.footer,
            text="Listening on Ctrl + Opt + A",
            font=ctk.CTkFont(family="SF Pro Text", size=12),
            text_color="#6b7280"
        )
        self.hint_label.pack(side="left")
        
        self.hide_btn = ctk.CTkButton(
            self.footer,
            text="HIDE",
            width=90,
            height=32,
            corner_radius=10,
            fg_color="#3b82f6",
            hover_color="#2563eb",
            text_color="white",
            font=ctk.CTkFont(family="SF Pro Text", size=12, weight="bold"),
            command=self.root.withdraw
        )
        self.hide_btn.pack(side="right")
        
        # Start polling queue
        self.root.after(100, self._poll_queue)

    def _poll_queue(self):
        while not self.queue.empty():
            text = self.queue.get()
            self._update_text(text)
        self.root.after(100, self._poll_queue)

    def _update_text(self, text):
        self.text_area.configure(state="normal")
        self.text_area.delete("1.0", "end")
        self.text_area.insert("1.0", text)
        self.text_area.configure(state="disabled")
        self.text_area.see("end")
        self.root.deiconify()

    def show_text(self, text):
        self.queue.put(text)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    # Test UI
    ui = FloatingWindow()
    ui.show_text("This is a preview of the new modern UI for the AI Assistant.\n\nIt looks much cooler now!")
    ui.run()
