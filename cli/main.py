import sys
sys.path.append('.')

from models.user import User
from models.project import Project
from models.task import Task
from lib.database import init_db

class TaskManagerCLI:
    def __init__(self):
        init_db()
    
    def main_menu(self):
        while True:
            print("\n=== Task Manager ===")
            print("1. User Management")
            print("2. Project Management") 
            print("3. Task Management")
            print("4. Exit")
            
            choice = input("\nSelect option: ").strip()
            
            if choice == "1":
                self.user_menu()
            elif choice == "2":
                self.project_menu()
            elif choice == "3":
                self.task_menu()
            elif choice == "4":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Try again.")
    
    def user_menu(self):
        while True:
            print("\n=== User Management ===")
            print("1. Create User")
            print("2. View All Users")
            print("3. Find User by ID")
            print("4. Delete User")
            print("5. View User's Projects")
            print("6. Back to Main Menu")
            
            choice = input("\nSelect option: ").strip()
            
            if choice == "1":
                self.create_user()
            elif choice == "2":
                self.view_all_users()
            elif choice == "3":
                self.find_user()
            elif choice == "4":
                self.delete_user()
            elif choice == "5":
                self.view_user_projects()
            elif choice == "6":
                break
            else:
                print("Invalid choice. Try again.")
    
    def create_user(self):
        try:
            name = input("Enter name: ").strip()
            email = input("Enter email: ").strip()
            user = User.create(name, email)
            print(f"User created successfully! ID: {user.id}")
        except Exception as e:
            print(f"Error: {e}")
    
    def view_all_users(self):
        users = User.get_all()
        if not users:
            print("No users found.")
            return
        
        print("\n--- All Users ---")
        for user in users:
            print(f"ID: {user.id}, Name: {user.name}, Email: {user.email}, Projects: {user.project_count}")
    
    def find_user(self):
        try:
            user_id = int(input("Enter user ID: "))
            user = User.find_by_id(user_id)
            if user:
                print(f"Found: ID: {user.id}, Name: {user.name}, Email: {user.email}")
            else:
                print("User not found.")
        except ValueError:
            print("Invalid ID format.")
    
    def delete_user(self):
        try:
            user_id = int(input("Enter user ID to delete: "))
            user = User.find_by_id(user_id)
            if user:
                user.delete()
                print("User deleted successfully!")
            else:
                print("User not found.")
        except ValueError:
            print("Invalid ID format.")
    
    def view_user_projects(self):
        try:
            user_id = int(input("Enter user ID: "))
            user = User.find_by_id(user_id)
            if user:
                if user.projects:
                    print(f"\n--- Projects for {user.name} ---")
                    for project in user.projects:
                        print(f"ID: {project.id}, Name: {project.name}, Tasks: {project.task_count}")
                else:
                    print("No projects found for this user.")
            else:
                print("User not found.")
        except ValueError:
            print("Invalid ID format.")

    def project_menu(self):
        while True:
            print("\n=== Project Management ===")
            print("1. Create Project")
            print("2. View All Projects")
            print("3. Find Project by ID")
            print("4. Delete Project")
            print("5. View Project Tasks")
            print("6. Back to Main Menu")
            
            choice = input("\nSelect option: ").strip()
            
            if choice == "1":
                self.create_project()
            elif choice == "2":
                self.view_all_projects()
            elif choice == "3":
                self.find_project()
            elif choice == "4":
                self.delete_project()
            elif choice == "5":
                self.view_project_tasks()
            elif choice == "6":
                break
            else:
                print("Invalid choice. Try again.")
    
    def create_project(self):
        try:
            name = input("Enter project name: ").strip()
            description = input("Enter description: ").strip()
            user_id = int(input("Enter user ID: "))
            
            user = User.find_by_id(user_id)
            if not user:
                print("User not found.")
                return
            
            project = Project.create(name, description, user_id)
            print(f"Project created successfully! ID: {project.id}")
        except ValueError:
            print("Invalid user ID format.")
        except Exception as e:
            print(f"Error: {e}")
    
    def view_all_projects(self):
        projects = Project.get_all()
        if not projects:
            print("No projects found.")
            return
        
        print("\n--- All Projects ---")
        for project in projects:
            print(f"ID: {project.id}, Name: {project.name}, Owner: {project.owner.name}, Tasks: {project.task_count}")
    
    def find_project(self):
        try:
            project_id = int(input("Enter project ID: "))
            project = Project.find_by_id(project_id)
            if project:
                print(f"Found: ID: {project.id}, Name: {project.name}, Description: {project.description}")
            else:
                print("Project not found.")
        except ValueError:
            print("Invalid ID format.")
    
    def delete_project(self):
        try:
            project_id = int(input("Enter project ID to delete: "))
            project = Project.find_by_id(project_id)
            if project:
                project.delete()
                print("Project deleted successfully!")
            else:
                print("Project not found.")
        except ValueError:
            print("Invalid ID format.")
    
    def view_project_tasks(self):
        try:
            project_id = int(input("Enter project ID: "))
            project = Project.find_by_id(project_id)
            if project:
                if project.tasks:
                    print(f"\n--- Tasks for {project.name} ---")
                    for task in project.tasks:
                        print(f"ID: {task.id}, Title: {task.title}, Status: {task.status}, Priority: {task.priority}")
                else:
                    print("No tasks found for this project.")
            else:
                print("Project not found.")
        except ValueError:
            print("Invalid ID format.")
    
    def task_menu(self):
        while True:
            print("\n=== Task Management ===")
            print("1. Create Task")
            print("2. View All Tasks")
            print("3. Find Task by ID")
            print("4. Delete Task")
            print("5. Mark Task Complete")
            print("6. Back to Main Menu")
            
            choice = input("\nSelect option: ").strip()
            
            if choice == "1":
                self.create_task()
            elif choice == "2":
                self.view_all_tasks()
            elif choice == "3":
                self.find_task()
            elif choice == "4":
                self.delete_task()
            elif choice == "5":
                self.mark_task_complete()
            elif choice == "6":
                break
            else:
                print("Invalid choice. Try again.")
    
    def create_task(self):
        try:
            title = input("Enter task title: ").strip()
            description = input("Enter description: ").strip()
            priority = input("Enter priority (low/medium/high): ").strip().lower()
            project_id = int(input("Enter project ID: "))
            
            project = Project.find_by_id(project_id)
            if not project:
                print("Project not found.")
                return
            
            task = Task.create(title, description, priority, project_id)
            print(f"Task created successfully! ID: {task.id}")
        except ValueError:
            print("Invalid project ID format.")
        except Exception as e:
            print(f"Error: {e}")
    
    def view_all_tasks(self):
        tasks = Task.get_all()
        if not tasks:
            print("No tasks found.")
            return
        
        print("\n--- All Tasks ---")
        for task in tasks:
            print(f"ID: {task.id}, Title: {task.title}, Status: {task.status}, Priority: {task.priority}, Project: {task.project.name}")
    
    def find_task(self):
        try:
            task_id = int(input("Enter task ID: "))
            task = Task.find_by_id(task_id)
            if task:
                print(f"Found: ID: {task.id}, Title: {task.title}, Description: {task.description}, Status: {task.status}")
            else:
                print("Task not found.")
        except ValueError:
            print("Invalid ID format.")
    
    def delete_task(self):
        try:
            task_id = int(input("Enter task ID to delete: "))
            task = Task.find_by_id(task_id)
            if task:
                task.delete()
                print("Task deleted successfully!")
            else:
                print("Task not found.")
        except ValueError:
            print("Invalid ID format.")
    
    def mark_task_complete(self):
        try:
            task_id = int(input("Enter task ID to mark complete: "))
            task = Task.find_by_id(task_id)
            if task:
                task.mark_complete()
                print("Task marked as complete!")
            else:
                print("Task not found.")
        except ValueError:
            print("Invalid ID format.")

if __name__ == "__main__":
    cli = TaskManagerCLI()
    cli.main_menu()