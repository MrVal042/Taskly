from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)
DB_NAME = "task.db"

# ---------- DB ----------
def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            category TEXT,
            status TEXT DEFAULT 'backlog',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()

init_db()

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

# ---------- Routes ----------
@app.route("/")
def index():
    return render_template(
        "index.html",
        tasks=group_tasks_by_status(),
        stats=get_task_stats()
    )

@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        title = request.form.get("title")
        category = request.form.get("category")
        status = request.form.get("status", "backlog")

        if title:
            conn = sqlite3.connect(DB_NAME)
            c = conn.cursor()
            c.execute(
                "INSERT INTO tasks (title, category, status) VALUES (?, ?, ?)",
                (title, category, status)
            )
            conn.commit()
            conn.close()

        return redirect(url_for("index"))

    return render_template("add.html")

@app.route("/update/<int:task_id>/<string:new_status>")
def update(task_id, new_status):
    if new_status not in ["backlog", "pending", "in-progress", "completed"]:
        return redirect(url_for("index"))

    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute(
        "UPDATE tasks SET status = ? WHERE id = ?",
        (new_status, task_id)
    )
    conn.commit()
    conn.close()

    return redirect(url_for("index"))

@app.route("/delete/<int:task_id>", methods=["POST"])
def delete(task_id):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()

    return redirect(url_for("index"))

@app.route("/projects")
def projects():
    return render_template(
        "projects.html",
        stats=get_task_stats()
    )

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)
