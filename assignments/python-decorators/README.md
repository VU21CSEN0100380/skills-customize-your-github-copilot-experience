# 📘 Assignment: Python Decorators

## 🎯 Objective

Master the art of writing custom decorators in Python. You'll learn how to create reusable functions that modify other functions, unlocking powerful patterns for logging, timing, authentication, and validation that you've seen in frameworks like FastAPI.

## 📝 Tasks

### 🛠️ Task 1: Create a Timing Decorator

#### Description

Write a decorator called `@timer` that measures how long a function takes to execute and prints the elapsed time. This is useful for performance monitoring and optimization.

#### Requirements

Completed program should:

- Define a decorator function `timer` that wraps any function
- Measure execution time using the `time` module
- Print the function name and elapsed time in a readable format (e.g., "my_function took 0.152 seconds")
- Return the original function's result unchanged
- Work with functions that take any number of arguments and keyword arguments

#### Example

```python
@timer
def slow_function():
    time.sleep(0.5)
    return "Done!"

result = slow_function()
# Output: slow_function took 0.501 seconds
# result = "Done!"
```

---

### 🛠️ Task 2: Create a Decorator with Parameters

#### Description

Write a decorator called `@repeat(n)` that runs a function `n` times and returns a list of all results. This demonstrates how to create decorators that accept custom parameters.

#### Requirements

Completed program should:

- Define a decorator factory `repeat` that accepts a parameter `n`
- Return a decorator that calls the wrapped function `n` times
- Collect and return all results in a list
- Preserve the original function's name and docstring using `functools.wraps`
- Work with functions that return different types of values

#### Example

```python
@repeat(3)
def greet(name):
    return f"Hello, {name}!"

results = greet("Alice")
# results = ["Hello, Alice!", "Hello, Alice!", "Hello, Alice!"]
```

---

### 🛠️ Task 3: Create a Call Tracking Decorator

#### Description

Write a decorator called `@track_calls` that logs every time a function is called, including the arguments passed and the result returned. This decorator should keep count of total function calls.

#### Requirements

Completed program should:

- Define a decorator `track_calls` that logs function calls
- Print the function name, arguments, keyword arguments, and return value
- Keep a call counter that increments with each invocation
- Provide a way to retrieve the total number of calls (e.g., via a `.call_count` attribute)
- Format the output clearly and readably

#### Example

```python
@track_calls
def add(a, b):
    return a + b

add(2, 3)
add(5, 7)
print(add.call_count)

# Output:
# Calling add with args=(2, 3), kwargs={}. Result: 5
# Calling add with args=(5, 7), kwargs={}. Result: 12
# 2
```

---

### 🛠️ Task 4: Create a Validation Decorator (Stretch Goal)

#### Description

Write a decorator called `@validate_positive` that ensures a function's numeric arguments are positive. If any argument is not positive, raise a `ValueError` with a descriptive message instead of calling the function.

#### Requirements

Completed program should:

- Define a decorator `validate_positive` that checks all positional and keyword arguments
- Raise `ValueError` if any numeric argument is ≤ 0
- Include the argument name and value in the error message
- Allow non-numeric arguments to pass through unchanged
- Still execute and return results for valid inputs

#### Example

```python
@validate_positive
def divide(numerator, denominator):
    return numerator / denominator

print(divide(10, 2))      # 5.0
print(divide(-10, 2))     # ValueError: Argument 'numerator' must be positive (got -10)
print(divide(10, 0))      # ValueError: Argument 'denominator' must be positive (got 0)
```
