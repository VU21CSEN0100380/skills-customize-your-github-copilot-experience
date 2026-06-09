# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

In this assignment, you'll build a RESTful API using the FastAPI framework, learning how to create endpoints, handle HTTP methods, validate request data, and serve structured responses. You'll develop a task management API that demonstrates core REST principles and best practices.

## 📝 Tasks

### 🛠️ Set Up FastAPI and Create Your First Endpoint

#### Description
Initialize a FastAPI application and create a simple endpoint. This task introduces you to the basics of FastAPI's elegant design and automatic API documentation features.

#### Requirements
Completed program should:

- Import and instantiate a FastAPI application
- Create a GET endpoint at `/` that returns a welcome message
- Create a GET endpoint at `/health` that returns a status check response
- Run the server using `uvicorn` and verify it works with automatic API documentation at `/docs`

### 🛠️ Build CRUD Operations for Tasks

#### Description
Implement Create, Read, Update, and Delete operations for a task management system. Use Pydantic models for data validation and in-memory storage to persist tasks during the session.

#### Requirements
Completed program should:

- Define a Pydantic model `Task` with fields: `id` (int), `title` (str), `description` (str), and `completed` (bool)
- Implement POST `/tasks` to create new tasks with auto-incrementing IDs
- Implement GET `/tasks` to retrieve all tasks
- Implement GET `/tasks/{id}` to retrieve a specific task by ID
- Implement PUT `/tasks/{id}` to update an existing task
- Implement DELETE `/tasks/{id}` to delete a task
- Return appropriate HTTP status codes (201 for creation, 404 for not found, etc.)

### 🛠️ Add Request Validation and Error Handling

#### Description
Enhance your API with robust data validation using Pydantic and proper error handling for edge cases. This ensures your API is reliable and provides meaningful error messages to clients.

#### Requirements
Completed program should:

- Validate that task titles are not empty and not excessively long (e.g., max 200 characters)
- Return 400 (Bad Request) for invalid input with descriptive error messages
- Return 404 (Not Found) when attempting to access or modify a non-existent task
- Use FastAPI's built-in validation decorators and response models
- Test your API endpoints using the automatic Swagger UI at `/docs`

### 🛠️ Add Query Parameters and Filters

#### Description
Implement filtering capabilities to allow clients to query tasks by status. This teaches you how to handle optional query parameters and implement business logic based on client requests.

#### Requirements
Completed program should:

- Add an optional query parameter `completed` (bool) to GET `/tasks` to filter tasks by completion status
- When `completed=true`, return only completed tasks
- When `completed=false`, return only incomplete tasks
- When the parameter is omitted, return all tasks
- Test the filtering functionality with various parameter combinations
