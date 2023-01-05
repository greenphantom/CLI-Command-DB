"""Script defining the model for command objects."""

from dataclasses import dataclass, field

@dataclass(frozen=True)
class Command():
    """Model for the commands, used to group data on command groupings."""

    # CLI Command
    command: str = "Some command..."

    # Description fo the command
    description: str = "Info about the command and its usage..."

    # List of options/flags to use with the commands
    options: list[str] = field(default_factory=list)

    # List of supported args for the command
    args: list[str] = field(default_factory=list)

    # Example of the completed command
    example: str = "some_command [example]"

    # CLI Tag to group
    cli: str = "git"
