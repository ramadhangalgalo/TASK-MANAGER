## Task Manager CLI

A command-line task management application built with Python, SQLAlchemy ORM, and SQLite database.

## Features

- **User Management**: Create, view, find, and delete users
- **Project Management**: Create projects, assign to users, view project tasks
- **Task Management**: Create tasks, assign to projects, mark complete, set priorities
- **Database Relations**: Users → Projects (1-to-many), Projects → Tasks (1-to-many)

## Setup

1. Install dependencies:
   ```bash
   pipenv install
   ```

2. Activate virtual environment:
   ```bash
   pipenv shell
   ```

3. Run the application:
   ```bash
   python main.py
   ```

## Database Schema

- **Users**: id, name, email
- **Projects**: id, name, description, user_id (FK)
- **Tasks**: id, title, description, completed, priority, project_id (FK)

## Usage

The CLI provides interactive menus for:
- Creating and managing users
- Creating projects and assigning them to users
- Creating tasks and assigning them to projects
- Viewing relationships between users, projects, and tasks
- Marking tasks as complete

## Requirements Met

✅ CLI application solving real-world problem (task management)
✅ SQLAlchemy ORM with 3+ related tables
✅ Pipenv virtual environment
✅ Proper package structure
✅ 1-to-many relationships (User→Project, Project→Task)
✅ Property methods and constraints
✅ CRUD operations for all models
✅ Interactive CLI menus with validation
✅ OOP best practices