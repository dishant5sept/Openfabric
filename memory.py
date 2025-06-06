import sqlite3

class MemoryManager:
    def __init__(self, db_path: str):
        self.conn = sqlite3.connect(db_path)
        self.create_table()

    def create_table(self):
        with self.conn:
            self.conn.execute("""
                CREATE TABLE IF NOT EXISTS memories (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    prompt TEXT,
                    enhanced_prompt TEXT,
                    image_path TEXT,
                    model_path TEXT
                )
            """)

    def save_prompt_result(self, prompt: str, enhanced: str, image_path: str, model_path: str):
        with self.conn:
            self.conn.execute(
                "INSERT INTO memories (prompt, enhanced_prompt, image_path, model_path) VALUES (?, ?, ?, ?)",
                (prompt, enhanced, image_path, model_path)
            )

    def get_all_memories(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM memories")
        return cursor.fetchall()
