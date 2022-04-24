"""Script defining the utility to read env constants."""
from dotenv import load_dotenv, dotenv_values

truth_comp_list = ['true', '1', 'y', 'yes', 't', 'on']

class AppEnv():
    """Class the encapsulates utilitizing the .ENV functionality."""

    def __init__(self) -> None:
        """Load the env file into object."""
        self.env_dict = dotenv_values(".env")
    
    def get_value(self, key: str, default: object = None) -> str | object | None:
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
        
        If nothing is present, will default to deafult provided bool value.

        Args:
            key (str): Key to check against in the env file.
            default (bool, optional): Boolean default if key not defined. Defaults to False.

        Returns:
            bool: The boolean value.
        """
        # Try to get the str value from the env
        ret = self.get_value(key, default)
        
        # Return its proper value
        match ret:
            case '':
                return ret.lower() in truth_comp_list
            case _:
                return ret