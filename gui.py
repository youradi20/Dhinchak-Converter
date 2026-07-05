import customtkinter as ctk
from converter import convert

COLORS = {
    "bg": "#1a1a2e", "panel": "#16213e", "accent": "#0f3460",
    "highlight": "#e94560", "success": "#4ecca3", "text": "#ffffff", "text_dim": "#a0a0a0" 
}

class DhinchakGUI:
    def __init__(self):
        ctk.set_appearance_mode("dark")

        self.root = ctk.CTk()
        self.root.title("Dhinchak Converter")
        self.root.geometry("650x520")
        self.root.configure(fg_color = COLORS["bg"])
        self.root.resizable(False, False)
        
        self.root.update_idletasks()
        x = (self.root.winfo_screenwidth()-650) // 2
        y = (self.root.winfo_screenheight()-520) // 2
        self.root.geometry(f"650x520+{x}+{y}")

        self.selected_category = None
        self.build_header()
        self.build_categories()
        self.build_history_area()

    def build_header(self):
        ctk.CTkLabel(self.root, text = "Dhinchak Converter", font=("Segoe UI", 26, "bold"), text_color= COLORS["highlight"]).pack(pady = (25,15))
    def build_categories(self):
        frame = ctk.CTkFrame(self.root, fg_color="transparent")
        frame.pack(pady = 10)
        self.cat_buttons = []
        for text, cat in [("🌡️ Temperature", "Temperature"),("📏 Length","Length"),("⚖️ Weight", "Weight")]:
            btn = ctk.CTkButton(frame, text = text, width=180, height=40, font= ("Segoe UI", 13), corner_radius= 10, fg_color= COLORS["accent"], hover_color=COLORS["panel"], command = lambda c=cat: self.select_category(c))
            btn.pack(side = "left", padx = 5)
            self.cat_buttons.append((btn, cat))

    def build_history_area(self):
        self.history_frame = ctk.CTkFrame(self.root, fg_color=COLORS["panel"], corner_radius=12)
        self.history_frame.pack(fill="both", expand=True, padx=25, pady=(5, 25))
        
        # Header row
        header = ctk.CTkFrame(self.history_frame, fg_color="transparent")
        header.pack(fill="x", padx=15, pady=(10, 5))
        
        ctk.CTkLabel(header, text="📊 History", 
                     font=("Segoe UI", 14, "bold"), 
                     text_color=COLORS["text_dim"]).pack(side="left")
                     
        ctk.CTkButton(header, text="Clear", width=50, height=25,
                      font=("Segoe UI", 10), fg_color=COLORS["highlight"],
                      hover_color="#ff6b6b",
                      command=self.clear_history).pack(side="right")
        
        # Use CTkTextbox instead of CTkLabel for multi-line text
        self.history_textbox = ctk.CTkTextbox(
            self.history_frame, 
            height=120, 
            font=("Consolas", 11), 
            fg_color=COLORS["bg"], 
            text_color="#888",
            border_width=0,
            state="disabled"  # Makes it read-only
        )
        self.history_textbox.pack(fill="both", expand=True, padx=15, pady=(0, 15))
    
    
    def select_category(self, category):
        self.selected_category = category

        for btn,cat in self.cat_buttons:
            btn.configure(fg_color = COLORS["highlight"] if cat == category else COLORS["accent"])
            
        if hasattr(self, 'converter_frame'):
            self.converter_frame.destroy()
            
        self.build_converter()

    def run(self):
        self.root.mainloop()
    
    def clear_history(self):
        if hasattr(self, 'history'):
            self.history.clear()
        
        self.history_textbox.configure(state="normal")
        self.history_textbox.delete("1.0", "end")
        self.history_textbox.insert("1.0", "No conversions yet")
        self.history_textbox.configure(state="disabled")

    def update_history_display(self):
        if hasattr(self, 'history'):
            items = self.history.get_all()
            
            self.history_textbox.configure(state="normal") # Unlock to edit
            self.history_textbox.delete("1.0", "end")      # Clear old text
            
            if items:
                self.history_textbox.insert("1.0", "\n".join(items))
            else:
                self.history_textbox.insert("1.0", "No conversions yet")
                
            self.history_textbox.configure(state="disabled") # Lock again
    
    def build_converter(self):
        self.converter_frame = ctk.CTkFrame(self.root, fg_color=COLORS["panel"], corner_radius= 12)

        self.converter_frame.pack(fill = "x", padx = 25, pady=(0,5), before = self.history_frame)

        units = {
            "Temperature" : ["Celsius","Fahrenheit", "Kelvin"],
            "Length" : ["Inch","Centimeter"],
            "Weight": ["Grams","Pounds"] 
        }

        unit_list = units[self.selected_category]
        # ---- ROW 1 -----
        row1 = ctk.CTkFrame(self.converter_frame, fg_color="transparent")
        row1.pack(fill = "x", padx = 15, pady = (15,5))

        ctk.CTkLabel(row1, text="FROM: ", text_color=COLORS["text_dim"],width=50).pack(side = "left")

        self.input_entry = ctk.CTkEntry(row1, width = 200, height = 40, font = ("Segoe UI", 14), fg_color= COLORS["bg"], border_color=COLORS["accent"])
        self.input_entry.pack(side = "left", padx = 10)
        self.input_entry.bind("<Return>", lambda e: self.do_conversion())
        self.from_var = ctk.StringVar(value = unit_list[0])
        ctk.CTkOptionMenu(row1, variable= self.from_var, values=unit_list, width=140, height=40).pack(side = "left")

        ctk.CTkButton(self.converter_frame, text="⇅", width= 35, height=35, font=("Segoe UI", 16), fg_color= COLORS["accent"], hover_color=COLORS["highlight"], command= self.swap_units).pack(pady=5)

        # ---- ROW 2 -----
        row2 = ctk.CTkFrame(self.converter_frame, fg_color="transparent")
        row2.pack(fill="x", padx=15, pady=(0,5))
        
        ctk.CTkLabel(row2, text="TO:", text_color=COLORS["text_dim"], width=50).pack(side="left")
        
        self.result_entry = ctk.CTkEntry(row2, width=200, height=40, font=("Segoe UI", 14), fg_color=COLORS["bg"], border_color=COLORS["success"], text_color=COLORS["success"], state="disabled")
        self.result_entry.pack(side="left", padx=10)
        
        self.to_var = ctk.StringVar(value=unit_list[1])
        ctk.CTkOptionMenu(row2, variable=self.to_var, values=unit_list, width=140, height=40, command=lambda e: self.do_conversion()).pack(side="left")

        # --- CONVERT BUTTON ---
        ctk.CTkButton(self.converter_frame, text="⚡ CONVERT", width=300, height=42, font=("Segoe UI", 14, "bold"), fg_color=COLORS["highlight"], hover_color="#ff6b6b", command=self.do_conversion).pack(pady=(5, 15))
        
        self.error_label = ctk.CTkLabel(self.converter_frame, text="", text_color=COLORS["highlight"])
        self.error_label.pack(pady=(0, 10))
        
        self.input_entry.focus()
    
    def swap_units(self):
        temp = self.from_var.get()
        self.from_var.set(self.to_var.get())
        self.to_var.set(temp)
        self.do_conversion()
        

    def do_conversion(self):
        self.error_label.configure(text="")
        val_str = self.input_entry.get()
        
        try:
            value = float(val_str)
        except ValueError:
            self.error_label.configure(text="⚠️ Enter a valid number" if val_str else "")
            self._update_result("")
            return
        
        if self.from_var.get() == self.to_var.get():
            self.error_label.configure(text="⚠️ Select different units")
            return
            
        if self.selected_category == "Temperature" and self.from_var.get() == "Kelvin" and value < 0:
            self.error_label.configure(text="⚠️ Kelvin can't be negative")
            return
        
        result = convert(self.selected_category, self.from_var.get(), self.to_var.get(), value)
        
        if result is None:
            self.error_label.configure(text="⚠️ Conversion error")
            return
            
        # Format nicely
        res_str = str(int(result)) if result == int(result) else f"{result:.4f}".rstrip('0').rstrip('.')
        self._update_result(res_str)
        
        # Trigger history save (will implement in Day 4)
        if hasattr(self, 'on_convert'): 
            self.on_convert(f"{value} {self.from_var.get()} → {res_str} {self.to_var.get()}")

    def _update_result(self, text):
        self.result_entry.configure(state="normal")
        self.result_entry.delete(0, "end")
        self.result_entry.insert(0, text)
        self.result_entry.configure(state="disabled")