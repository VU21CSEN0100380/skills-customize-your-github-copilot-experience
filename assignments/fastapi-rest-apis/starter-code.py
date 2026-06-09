"""
Building REST APIs with FastAPI - Starter Code

This starter code provides a foundation for building a task management REST API.
Complete the tasks by implementing the missing endpoints and functionality.
"""

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import Optional, List

# Initialize the FastAPI application
app = FastAPI(
    title="Task Management API",
    description="A simple REST API for managing tasks",
    version="1.0.0"
)

# TODO: Define a Pydantic model for Task
# The model should have: id (int), title (str), description (str), completed (bool)


# In-memory storage for tasks
tasks_db = []
next_task_id = 1


# TODO: Create a GET endpoint at "/" that returns a welcome message
# Example response: {"message": "Welcome to Task Management API"}


# TODO: Create a GET endpoint at "/health" that returns a status check
# Example response: {"status": "ok"}


# TODO: Create a POST endpoint at "/tasks" to add a new task
# - Accept a Task model in the request body
# - Assign an auto-incrementing ID
# - Store the task in tasks_db
# - Return the created task with status code 201


# TODO: Create a GET endpoint at "/tasks" to retrieve all tasks
# - Add an optional query parameter "completed" (bool) for filtering
# - Return all tasks, or filter by completion status if specified
# - Return status code 200


# TODO: Create a GET endpoint at "/tasks/{task_id}" to retrieve a specific task
# - Return the task if found
# - Return 404 error if task not found


# TODO: Create a PUT endpoint at "/tasks/{task_id}" to update a task
# - Accept updated task data in the request body
# - Return 404 if task not found
# - Return the updated task with status code 200


# TODO: Create a DELETE endpoint at "/tasks/{task_id}" to delete a task
# - Remove the task from tasks_db
# - Return 404 if task not found
# - Return status code 204 (No Content) on success


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
