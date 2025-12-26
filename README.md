# Taskly – A Simple Task Management Dashboard

#### Video Demo: https://youtu.be/YOUR_VIDEO_LINK

## Description

Taskly is a lightweight web-based task management application built using Flask, SQLite, HTML, CSS, JavaScript, and Bootstrap. The goal of this project is to provide a clean and intuitive interface for managing tasks across multiple states while demonstrating core concepts learned throughout CS50, including backend development, database design, templating, and frontend interactivity.

The application allows users to create tasks, assign categories, track progress through different statuses, visualize task statistics, and manage their workload efficiently. Taskly is designed to be minimal yet extensible, focusing on clarity, usability, and correctness rather than unnecessary complexity.

---

## Features

- Add new tasks with a title, category, and initial status
- Automatically group tasks by status:
  - Backlog
  - Pending
  - In Progress
  - Completed
- Update task status and mark tasks as completed
- Delete tasks
- Dashboard showing real-time task statistics
- Visual task distribution chart using Chart.js
- Responsive layout optimized for mobile and desktop
- Clean UI using Bootstrap and custom CSS

---

## Project Structure

```bash
project/
│
├── app.py
├── task.db
├── requirements.txt
│
├── templates/
│   ├── layout.html
│   ├── index.html
│   ├── add.html
│   ├── projects.html
│   └── about.html
│
├── static/
│   ├── style.css
│   └── script.js
│
└── README.md

```

---

## Backend (Flask + SQLite)

The backend is implemented using Flask. The database is SQLite and contains a single table called `tasks`. Each task has the following fields:

- `id`: unique identifier
- `title`: task title
- `category`: optional category
- `status`: backlog, pending, in-progress, or completed
- `created_at`: timestamp

Helper functions are used to fetch tasks, group them by status, and compute statistics. This logic is intentionally separated from the route handlers to keep the code clean and maintainable.

---

## Frontend (HTML, CSS, JavaScript)

The frontend uses Jinja templates for rendering dynamic data. Bootstrap provides a responsive grid system and consistent styling, while custom CSS enhances layout and branding.

JavaScript is used for:

- Mobile navigation toggling
- Rendering dynamic charts using Chart.js

Task statistics are passed from Flask to JavaScript safely using Jinja’s `tojson` filter.

---

## Design Decisions

One key design decision was using a status field instead of a simple completed boolean. This allows the application to support multiple stages of task progress and makes the project more scalable.

Another decision was to keep authentication out of scope. The focus of this project is task management logic, data flow, and UI clarity rather than user accounts.

---

## Future Improvements

- User authentication and multi-user support
- Project-based task grouping
- Drag-and-drop task movement
- Due dates and reminders
- Persistent chart filters

---

## Conclusion

Taskly demonstrates a complete, functional web application that integrates backend logic, database management, frontend rendering, and responsive design. It reflects the core skills taught in CS50 and provides a strong foundation for more advanced applications.
