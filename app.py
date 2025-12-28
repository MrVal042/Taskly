from flask import Flask, render_template, request, redirect, url_for
import requests
import sqlite3
from helper import DB_NAME, SCRIPT_URL, apology, get_task_stats, group_tasks_by_status


app = Flask(__name__)

# ---------- Initialize DB ----------
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


@app.route("/contact", methods=["POST"])
def contact():
    name = request.form.get("name")
    email = request.form.get("email")
    message = request.form.get("message")

    if not name or not email or not message:
        return apology("all fields required", 403)

    if not SCRIPT_URL:
        return apology("service not configured", 500)

    payload = {
        "name": name,
        "email": email,
        "message": message
    }

    try:
        response = requests.post(
            SCRIPT_URL,
            json=payload,
            timeout=5
        )
        response.raise_for_status()
    except requests.RequestException:
        return apology("failed to send message", 500)

    return render_template("success.html", name=name)


@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)
