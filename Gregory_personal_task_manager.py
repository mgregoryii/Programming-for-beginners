# This is my Project Management assignment and I attempted the Basic level.

# Test Case 1. First run — no .db file exists
# === Adding Tasks ===
# Task added successfully. ID: 1
# Task added successfully. ID: 2
# Task added successfully. ID: 3
# Task added successfully. ID: 4
# Task added successfully. ID: 5
# Task added successfully. ID: 6

# === All Tasks ===
# ID   Title                      Priority    Status         Due Date    
# -----------------------------------------------------------------------
# 1    Complete Python assignmen  High        Pending        2026-10-15  
# 2    Review database design     Medium      In Progress    2026-10-18  
# 3    Organize project files     Low         Pending        2026-10-20  
# 4    Test application           High        In Progress    2026-10-12  
# 5    Write documentation        Medium      Pending        2026-10-22  
# 6    Update project notes       Low         Done           2026-10-25  

# === Pending Tasks ===
# ID   Title                      Priority    Status         Due Date    
# -----------------------------------------------------------------------
# 1    Complete Python assignmen  High        Pending        2026-10-15  
# 3    Organize project files     Low         Pending        2026-10-20  
# 5    Write documentation        Medium      Pending        2026-10-22  
# Task 1 updated successfully to In Progress.
# Task 6 deleted successfully.

# === All Tasks After Updates ===
# ID   Title                      Priority    Status         Due Date    
# -----------------------------------------------------------------------
# 1    Complete Python assignmen  High        In Progress    2026-10-15  
# 2    Review database design     Medium      In Progress    2026-10-18  
# 3    Organize project files     Low         Pending        2026-10-20  
# 4    Test application           High        In Progress    2026-10-12  
# 5    Write documentation        Medium      Pending        2026-10-22  

# Database connection closed.

# Test Case 2. Second run without deleting .db
# === Adding Tasks ===
# Task added successfully. ID: 7
# Task added successfully. ID: 8
# Task added successfully. ID: 9
# Task added successfully. ID: 10
# Task added successfully. ID: 11
# Task added successfully. ID: 12

# === All Tasks ===
# ID   Title                      Priority    Status         Due Date    
# -----------------------------------------------------------------------
# 1    Complete Python assignmen  High        In Progress    2026-10-15  
# 2    Review database design     Medium      In Progress    2026-10-18  
# 3    Organize project files     Low         Pending        2026-10-20  
# 4    Test application           High        In Progress    2026-10-12  
# 5    Write documentation        Medium      Pending        2026-10-22  
# 7    Complete Python assignmen  High        Pending        2026-10-15  
# 8    Review database design     Medium      In Progress    2026-10-18  
# 9    Organize project files     Low         Pending        2026-10-20  
# 10   Test application           High        In Progress    2026-10-12  
# 11   Write documentation        Medium      Pending        2026-10-22  
# 12   Update project notes       Low         Done           2026-10-25  

# === Pending Tasks ===
# ID   Title                      Priority    Status         Due Date    
# -----------------------------------------------------------------------
# 7    Complete Python assignmen  High        Pending        2026-10-15  
# 3    Organize project files     Low         Pending        2026-10-20  
# 9    Organize project files     Low         Pending        2026-10-20  
# 5    Write documentation        Medium      Pending        2026-10-22  
# 11   Write documentation        Medium      Pending        2026-10-22  
# Task 7 updated successfully to In Progress.
# Task 12 deleted successfully.

# === All Tasks After Updates ===
# ID   Title                      Priority    Status         Due Date    
# -----------------------------------------------------------------------
# 1    Complete Python assignmen  High        In Progress    2026-10-15  
# 2    Review database design     Medium      In Progress    2026-10-18  
# 3    Organize project files     Low         Pending        2026-10-20  
# 4    Test application           High        In Progress    2026-10-12  
# 5    Write documentation        Medium      Pending        2026-10-22  
# 7    Complete Python assignmen  High        In Progress    2026-10-15  
# 8    Review database design     Medium      In Progress    2026-10-18  
# 9    Organize project files     Low         Pending        2026-10-20  
# 10   Test application           High        In Progress    2026-10-12  
# 11   Write documentation        Medium      Pending        2026-10-22  

# Database connection closed.

# Test Case 3, 4, 5, 6. update_task_status() on a valid ID
# Database connected successfully!
# Database file path: C:\Users\GregoryCTRMartinez\AppData\Local\Programs\Microsoft VS Code\tasks.db
# Tasks table created or verified successfully.

# === Adding Tasks ===
# Task added successfully. ID: 13
# Task added successfully. ID: 14
# Task added successfully. ID: 15
# Task added successfully. ID: 16
# Task added successfully. ID: 17
# Task added successfully. ID: 18

# === All Tasks ===
# ID   Title                      Priority    Status         Due Date    
# -----------------------------------------------------------------------
# 1    Complete Python assignmen  High        In Progress    2026-10-15  
# 2    Review database design     Medium      In Progress    2026-10-18  
# 3    Organize project files     Low         Pending        2026-10-20  
# 4    Test application           High        In Progress    2026-10-12  
# 5    Write documentation        Medium      Pending        2026-10-22  
# 7    Complete Python assignmen  High        In Progress    2026-10-15  
# 8    Review database design     Medium      In Progress    2026-10-18  
# 9    Organize project files     Low         Pending        2026-10-20  
# 10   Test application           High        In Progress    2026-10-12  
# 11   Write documentation        Medium      Pending        2026-10-22  
# 13   Complete Python assignmen  High        Pending        2026-10-15  
# 14   Review database design     Medium      In Progress    2026-10-18  
# 15   Organize project files     Low         Pending        2026-10-20  
# 16   Test application           High        In Progress    2026-10-12  
# 17   Write documentation        Medium      Pending        2026-10-22  
# 18   Update project notes       Low         Done           2026-10-25  

# === Pending Tasks ===
# ID   Title                      Priority    Status         Due Date    
# -----------------------------------------------------------------------
# 13   Complete Python assignmen  High        Pending        2026-10-15  
# 3    Organize project files     Low         Pending        2026-10-20  
# 9    Organize project files     Low         Pending        2026-10-20  
# 15   Organize project files     Low         Pending        2026-10-20  
# 5    Write documentation        Medium      Pending        2026-10-22  
# 11   Write documentation        Medium      Pending        2026-10-22  
# 17   Write documentation        Medium      Pending        2026-10-22  
# Task 13 updated successfully to In Progress.

# === Test Non-Existent Task ID ===
# Task ID 99999 not found. No update performed.
# Task 18 deleted successfully.

# === All Tasks After Updates ===
# ID   Title                      Priority    Status         Due Date    
# -----------------------------------------------------------------------
# 1    Complete Python assignmen  High        In Progress    2026-10-15  
# 2    Review database design     Medium      In Progress    2026-10-18  
# 3    Organize project files     Low         Pending        2026-10-20  
# 4    Test application           High        In Progress    2026-10-12  
# 5    Write documentation        Medium      Pending        2026-10-22  
# 7    Complete Python assignmen  High        In Progress    2026-10-15  
# 8    Review database design     Medium      In Progress    2026-10-18  
# 9    Organize project files     Low         Pending        2026-10-20  
# 10   Test application           High        In Progress    2026-10-12  
# 11   Write documentation        Medium      Pending        2026-10-22  
# 13   Complete Python assignmen  High        In Progress    2026-10-15  
# 14   Review database design     Medium      In Progress    2026-10-18  
# 15   Organize project files     Low         Pending        2026-10-20  
# 16   Test application           High        In Progress    2026-10-12  
# 17   Write documentation        Medium      Pending        2026-10-22  

# Database connection closed.

#Test Case 4. 


import sqlite3
import os


# -------------------------------------------------
# Database connection
# -------------------------------------------------

def create_connection(db_file):
    """Create the database file and return the connection."""
    try:
        file_path = os.path.abspath(db_file)
        file_exists = os.path.exists(file_path)

        conn = sqlite3.connect(file_path)

        if not file_exists:
            print("Database created successfully!")
        else:
            print("Database connected successfully!")

        print(f"Database file path: {file_path}")
        return conn

    except sqlite3.Error as error:
        print(f"Database connection error: {error}")
        return None


# -------------------------------------------------
# Create database table
# -------------------------------------------------

def setup_database(conn):
    """Create the tasks table if it does not exist."""
    try:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                description TEXT,
                priority TEXT DEFAULT 'Medium',
                status TEXT DEFAULT 'Pending',
                due_date TEXT,
                project_id INTEGER
            )
        """)
        conn.commit()
        print("Tasks table created or verified successfully.")

    except sqlite3.Error as error:
        print(f"Database setup error: {error}")
        raise


# -------------------------------------------------
# Add a task
# -------------------------------------------------

def add_task(conn, title, description="", priority="Medium",
             status="Pending", due_date=""):
    """Insert a task and return its ID."""
    try:
        cursor = conn.execute("""
            INSERT INTO tasks
                (title, description, priority, status, due_date, project_id)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            title,
            description,
            priority,
            status,
            due_date,
            None
        ))

        conn.commit()
        return cursor.lastrowid

    except sqlite3.Error as error:
        print(f"Error adding task: {error}")
        return None


# -------------------------------------------------
# Retrieve all tasks
# -------------------------------------------------

def get_all_tasks(conn):
    """Return all tasks from the database."""
    try:
        cursor = conn.execute("SELECT * FROM tasks")
        return cursor.fetchall()

    except sqlite3.Error as error:
        print(f"Error retrieving all tasks: {error}")
        return []


# -------------------------------------------------
# Retrieve tasks ordered by priority and due date
# -------------------------------------------------

def get_tasks_ordered(conn):
    """Return tasks ordered by priority and due date."""
    try:
        cursor = conn.execute(
            "SELECT * FROM tasks ORDER BY priority, due_date"
        )
        return cursor.fetchall()

    except sqlite3.Error as error:
        print(f"Error retrieving ordered tasks: {error}")
        return []


# -------------------------------------------------
# Retrieve tasks by status
# -------------------------------------------------

def get_tasks_by_status(conn, status):
    """Return tasks matching a status, ordered by priority."""
    try:
        cursor = conn.execute("""
            SELECT *
            FROM tasks
            WHERE status = ?
            ORDER BY priority
        """, (status,))

        return cursor.fetchall()

    except sqlite3.Error as error:
        print(f"Error retrieving tasks by status: {error}")
        return []


# -------------------------------------------------
# Update task status
# -------------------------------------------------

def update_task_status(conn, task_id, new_status):
    """Update a task's status and return whether a row changed."""
    try:
        cursor = conn.execute(
            "UPDATE tasks SET status = ? WHERE id = ?",
            (new_status, task_id)
        )

        conn.commit()

        # Return True if a task was updated; otherwise, False.
        return cursor.rowcount > 0

    except sqlite3.Error as error:
        print(f"Error updating task status: {error}")
        return False


# -------------------------------------------------
# Delete a task
# -------------------------------------------------

def delete_task(conn, task_id):
    """Delete a task by ID and return whether a row was deleted."""
    try:
        cursor = conn.execute(
            "DELETE FROM tasks WHERE id = ?",
            (task_id,)
        )

        conn.commit()
        return cursor.rowcount > 0

    except sqlite3.Error as error:
        print(f"Error deleting task: {error}")
        return False


# -------------------------------------------------
# Display tasks
# -------------------------------------------------

def display_tasks(tasks):
    """Display tasks in a formatted, aligned table."""
    if not tasks:
        print("No tasks found.")
        return

    print(
        f"{'ID':<5}"
        f"{'Title':<27}"
        f"{'Priority':<12}"
        f"{'Status':<15}"
        f"{'Due Date':<12}"
    )

    print("-" * 71)

    for task in tasks:
        task_id = task[0]
        title = task[1][:25]
        priority = task[3] or ""
        status = task[4] or ""
        due_date = task[5] or ""

        print(
            f"{task_id:<5}"
            f"{title:<27}"
            f"{priority:<12}"
            f"{status:<15}"
            f"{due_date:<12}"
        )


# -------------------------------------------------
# Main program
# -------------------------------------------------

def main():
    # 1. Create or connect to the database
    conn = create_connection("tasks.db")

    if conn is None:
        print("Error: Could not connect to the database.")
        return

    try:
        # 2. Ensure the tasks table exists
        setup_database(conn)

        # 3. Add six sample tasks
        print("\n=== Adding Tasks ===")

        tasks_to_add = [
            (
                "Complete Python assignment",
                "Finish coding project",
                "High",
                "Pending",
                "2026-10-15"
            ),
            (
                "Review database design",
                "Check table structure",
                "Medium",
                "In Progress",
                "2026-10-18"
            ),
            (
                "Organize project files",
                "Sort documents",
                "Low",
                "Pending",
                "2026-10-20"
            ),
            (
                "Test application",
                "Run program tests",
                "High",
                "In Progress",
                "2026-10-12"
            ),
            (
                "Write documentation",
                "Document program functions",
                "Medium",
                "Pending",
                "2026-10-22"
            ),
            (
                "Update project notes",
                "Review meeting notes",
                "Low",
                "Done",
                "2026-10-25"
            )
        ]

        task_ids = []

        for title, description, priority, status, due_date in tasks_to_add:
            task_id = add_task(
                conn,
                title,
                description,
                priority,
                status,
                due_date
            )

            if task_id is not None:
                task_ids.append(task_id)
                print(f"Task added successfully. ID: {task_id}")
            else:
                print(f"Failed to add task: {title}")

        # 4. Display all tasks
        print("\n=== All Tasks ===")
        all_tasks = get_all_tasks(conn)
        display_tasks(all_tasks)

        # 5. Display Pending tasks
        print("\n=== Pending Tasks ===")
        pending_tasks = get_tasks_by_status(conn, "Pending")
        display_tasks(pending_tasks)

        # 6. Update a task to In Progress
        if task_ids:
            update_id = task_ids[0]

            if update_task_status(conn, update_id, "In Progress"):
                print(
                    f"Task {update_id} updated successfully "
                    "to In Progress."
                )
            else:
                print(
                    f"Task ID {update_id} not found. "
                    "No update performed."
                )

        # Test updating a non-existent task ID
        print("\n=== Test Non-Existent Task ID ===")

        nonexistent_id = 99999
        new_status = "In Progress"

        if update_task_status(conn, nonexistent_id, new_status):
            print(f"Task {nonexistent_id} updated successfully.")
        else:
            print(
                f"Task ID {nonexistent_id} not found. "
                "No update performed."
            )

        # 7. Delete the sixth newly added task
        if len(task_ids) >= 6:
            delete_id = task_ids[5]

            if delete_task(conn, delete_id):
                print(f"Task {delete_id} deleted successfully.")
            else:
                print(f"Task {delete_id} not found.")

        # 8. Display all tasks after changes
        print("\n=== All Tasks After Updates ===")
        all_tasks = get_all_tasks(conn)
        display_tasks(all_tasks)

    except sqlite3.Error as error:
        print(f"Database error: {error}")

    finally:
        # 9. Close the database connection
        conn.close()
        print("\nDatabase connection closed.")


if __name__ == "__main__":
    main()

