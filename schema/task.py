from pydantic import BaseModel, field_validator, ValidationError, model_validator


class Task(BaseModel):
    """
    Represents a task in the system.

    Attributes:
        id (int): The id of the task.
        name (str): The name of the task.
        pomodoro_count (int): The number of pomodoros (work intervals) assigned to the task.
        category_id (int): The ID of the category to which the task belongs.
    """
    id: int
    name: str | None = None
    pomodoro_count: int | None = None
    category_id: int

    @field_validator("name", "pomodoro_count")
    @classmethod
    def check_name_or_pomodoro_count_is_not_none(cls, value, values):
        """
        Ensure that either the name or pomodoro_count is not None.
        """
        if values.get("name") is None and values.get("pomodoro_count") is None:
            raise ValueError("Either 'name' or 'pomodoro_count' must be provided.")
        return value


# class Task(BaseModel):
#     """
#     Represents a task in the system.
#
#     Attributes:
#         id (int): The id of the task.
#         name (str): The name of the task.
#         pomodoro_count (int): The number of pomodoros (work intervals) assigned to the task.
#         category_id (int): The ID of the category to which the task belongs.
#     """
#     id: int
#     name: str | None = None
#     pomodoro_count: int | None = None
#     category_id: int
#
#     @model_validator(mode='before')
#     @classmethod
#     def check_name_or_pomodoro_count_is_not_none(cls, values):
#         """
#         Ensure that either the name or pomodoro_count is not None.
#         """
#         name = values.get("name")
#         pomodoro_count = values.get("pomodoro_count")
#
#         if name is None and pomodoro_count is None:
#             raise ValueError("Either 'name' or 'pomodoro_count' must be provided.")
#
#         return values