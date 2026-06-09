"""
Starter code for Python Decorators assignment.

Task 1: Implement the @timer decorator
Task 2: Implement the @repeat(n) decorator
Task 3: Implement the @track_calls decorator
Task 4: Implement the @validate_positive decorator (stretch goal)
"""

import time
import functools


# ============================================================================
# Task 1: Create a Timing Decorator
# ============================================================================

def timer(func):
    """
    Decorator that measures how long a function takes to execute.
    
    TODO: Implement this decorator.
    """
    pass


# ============================================================================
# Task 2: Create a Decorator with Parameters
# ============================================================================

def repeat(n):
    """
    Decorator factory that returns a decorator to run a function n times.
    
    TODO: Implement this decorator factory.
    """
    pass


# ============================================================================
# Task 3: Create a Call Tracking Decorator
# ============================================================================

def track_calls(func):
    """
    Decorator that logs function calls and tracks the number of invocations.
    
    TODO: Implement this decorator.
    """
    pass


# ============================================================================
# Task 4: Create a Validation Decorator (Stretch Goal)
# ============================================================================

def validate_positive(func):
    """
    Decorator that validates all numeric arguments are positive.
    
    TODO: Implement this decorator.
    """
    pass


# ============================================================================
# Test your decorators below
# ============================================================================

if __name__ == "__main__":
    # Test Task 1: @timer
    print("=== Testing @timer ===")
    @timer
    def slow_function():
        time.sleep(0.5)
        return "Done!"
    
    result = slow_function()
    print(f"Result: {result}\n")

    # Test Task 2: @repeat(n)
    print("=== Testing @repeat(3) ===")
    @repeat(3)
    def greet(name):
        return f"Hello, {name}!"
    
    results = greet("Alice")
    print(f"Results: {results}\n")

    # Test Task 3: @track_calls
    print("=== Testing @track_calls ===")
    @track_calls
    def add(a, b):
        return a + b
    
    add(2, 3)
    add(5, 7)
    print(f"Total calls: {add.call_count}\n")

    # Test Task 4: @validate_positive (uncomment after implementing)
    # print("=== Testing @validate_positive ===")
    # @validate_positive
    # def divide(numerator, denominator):
    #     return numerator / denominator
    
    # print(divide(10, 2))
    # try:
    #     print(divide(-10, 2))
    # except ValueError as e:
    #     print(f"Error: {e}")
