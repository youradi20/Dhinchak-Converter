import json 
from pathlib import Path

class History:
    def __init__(self, file_path = "history.json"):
        self.file_path = Path(file_path)
        self.items = []
        self._load()
    
    def _load(self):
        if self.file_path.exists():
            try:
                self.items = json.loads(self.file_path.read_text())[:10]
            except: 
                self.items = []
    
    def _save(self):
        self.file_path.write_text(json.dumps(self.items))
    
    def add(self, text):
        self.items.insert(0,text)
        self.items = self.items[:10]
        self._save()
    
    def clear(self):
        self.items = []
        self._save()
    
    def get_all(self):
        return self.items
    
    