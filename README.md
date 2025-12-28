# Taskly – A Simple Task Management Dashboard

#### Project Demo: [here in youtube](https://youtu.be/7UbNTLQl57Q)

## Description

Taskly is a lightweight web-based task management application built as a CS50x final project. It allows users to organize tasks into multiple workflow states and visualize progress through a clean, intuitive interface.

The project demonstrates core CS50 concepts, including Flask-based backend development, SQLite database design, Jinja templating, form handling, and frontend interactivity using JavaScript and Bootstrap.

Users can create tasks, assign optional categories, update task status across predefined stages, view real-time task statistics, and submit messages via a contact form that integrates with Google Sheets.

---

## Features

- Create tasks with title, category, and initial status
- Group tasks automatically by workflow state:

  - Backlog
  - Pending
  - In Progress
  - Completed

- Update task status dynamically
- Delete tasks
- Dashboard with real-time task statistics
- Visual task distribution chart using Chart.js
- Responsive layout for desktop and mobile
- Contact form that sends submissions to Google Sheets via a server-side HTTP request

---

## Project Structure

```bash
project/
│
├── static/
│   ├── script.js
│   └── style.css
│
├── templates/
│   ├── about.html
│   ├── add.html
│   ├── index.html
│   ├── layout.html
│   ├── projects.html
│   └── success.html
│
├── .env
├── .gitignore
├── app.py
├── helper.py
├── LICENSE
├── README.md
├── requirements.txt
└── task.db
```

---

## Backend Implementation

The backend is built with Flask and uses SQLite for persistent storage. A single `tasks` table stores task data, including title, category, status, and creation timestamp.

Helper functions are used to:

- Retrieve tasks from the database
- Group tasks by status
- Compute task statistics for display

This separation of concerns keeps route handlers concise and improves maintainability.

---

## Frontend Implementation

The frontend uses Jinja templates to render dynamic content. Bootstrap provides responsive layout and styling, while custom CSS refines the user interface.

JavaScript is used to:

- Render task statistics using Chart.js
- Handle minor UI interactions

Data is passed safely from Flask to JavaScript using Jinja’s `tojson` filter.

---

## Configuration

The contact form submits messages to a Google Sheet via a Google Apps Script endpoint.

Before running the application, set the following environment variable:

- `GOOGLE_SCRIPT_URL`: The deployed Google Apps Script Web App URL

This avoids hard-coding sensitive configuration values in the source code.

---

## Design Decisions

A multi-state status system was chosen instead of a simple completed flag to better represent real-world workflows and allow future expansion.

User authentication was intentionally excluded to keep the project focused on task management logic, data flow, and interface clarity, in line with the project’s scope.

---

## Future Improvements

- User authentication and multi-user support
- Project-based task grouping
- Drag-and-drop task movement
- Due dates and reminders
- Persistent chart filters

---

## Conclusion

Taskly demonstrates a complete, functional web application that integrates backend logic, database operations, templating, and responsive frontend design, reflecting the core skills taught throughout CS50 and provides a strong foundation for more advanced applications.
