from gui import DhinchakGUI
from history import History

def main():
    # Initialize history
    history = History()
    
    # Initialize GUI
    app = DhinchakGUI()
    app.history = history  # Attach history to GUI
    
    # Connect the GUI conversion event to history
    def save_to_history(text):
        app.history.add(text)
        app.update_history_display()
        
    app.on_convert = save_to_history
    
    # Load existing history into UI on startup
    app.update_history_display()
    
    # Run
    app.run()

if __name__ == "__main__":
    main()