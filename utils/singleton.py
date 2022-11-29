"""Script defining class to enforce Singleton Design Pattern on Python Objects."""

from typing import Any


class Singleton(type):
    """Metaclass to apply the Singleton DP to Python classes."""

    def __init__(self, name, bases, dict):
        """Procedure for initialization."""
        self.__single_instance = None
        super().__init__(name, bases, dict)

    def __call__(cls, *args: Any, **kwds: Any) -> Any:
        """Ensure only one object is created at runtime."""
        if cls.__single_instance:
            return cls.__single_instance
        single_obj = cls.__new__(cls)
        single_obj.__init__(*args, **kwds)
        cls.__single_instance = single_obj
        return single_obj