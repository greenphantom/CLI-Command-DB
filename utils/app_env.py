"""Script defining the utility to read env constants."""

import os
from typing import Any
from dotenv import load_dotenv, dotenv_values

from utils.singleton import Singleton

truth_comp_list = ['true', '1', 'y', 'yes', 't', 'on']


class AppEnv(metaclass=Singleton):
    """Class the encapsulates utilizing the .ENV functionality."""

    def __init__(self) -> None:
        """Load the env file into object."""
        self.loaded = load_dotenv()
        self.env_dict = dotenv_values()

        # Add catch for system variables
        for k, v in self.env_dict.items():
            self.env_dict[k] = os.environ.get(k, v)

    def get_value(self, key: str, default: Any = None) -> str | Any | None:
        """Retrieve the value from the defined .env file.

        If value is not present, use the default value.

        Args:
            key (str): Key to look for in the .env
            default (object, optional): Optional default to use if env key is missing. Defaults to None.

        Returns:
            str: The str value defined in the .env.
            object: The default if provided.
            None: If no default is provided and key does not exist.
        """
        return default if self.env_dict[key] is None else self.env_dict[key]

    def get_bool_value(self, key: str, default: bool = False) -> bool:
        """Retrieve the boolean value defined within the env file.

        If nothing is present, will default to default provided bool value.

        Args:
            key (str): Key to check against in the env file.
            default (bool, optional): Boolean default if key not defined.
            Defaults to False.

        Returns:
            bool: The boolean value.
        """
        # Try to get the str value from the env
        ret = self.get_value(key, default)

        # Return its proper value
        match ret:
            case '':
                return ret.lower() if ret.lower() in truth_comp_list else default
            case _:
                return ret if isinstance(ret, bool) else default

ENV = AppEnv()