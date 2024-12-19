from pydantic import BaseModel

class Task(BaseModel):
    """
    Represents a task in the system.

    Attributes:
        name (str): The name of the task.
        pomodoro_count (int): The number of pomodoros (work intervals) assigned to the task.
        category_id (int): The ID of the category to which the task belongs.
    """
    name: str
    pomodoro_count: int
    category_id: int