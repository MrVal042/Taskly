from flask import  render_template
import sqlite3
import os


DB_NAME = "task.db"
SCRIPT_URL = os.environ.get("GOOGLE_SCRIPT_URL")

# ---------- Helpers ----------
def get_all_tasks():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("""
        SELECT id, title, category, status, created_at
        FROM tasks
        ORDER BY created_at DESC
    """)
    rows = c.fetchall()
    conn.close()
    return rows

def group_tasks_by_status():
    grouped = {
        "backlog": [],
        "pending": [],
        "in-progress": [],
        "completed": []
    }

    for t in get_all_tasks():
        task = {
            "id": t[0],
            "title": t[1],
            "category": t[2],
            "status": t[3],
            "created_at": t[4]
        }
        grouped[t[3]].append(task)

    return grouped

def get_task_stats():
    grouped = group_tasks_by_status()
    return {k: len(v) for k, v in grouped.items()}

def apology(message, code=400):
    """Render message as an apology to user."""

    def escape(s):
        """
        Escape special characters.

        https://github.com/jacebrowning/memegen#special-characters
        """
        for old, new in [
            ("-", "--"),
            (" ", "-"),
            ("_", "__"),
            ("?", "~q"),
            ("%", "~p"),
            ("#", "~h"),
            ("/", "~s"),
            ('"', "''"),
        ]:
            s = s.replace(old, new)
        return s

    return render_template("apology.html", top=code, bottom=escape(message)), code

