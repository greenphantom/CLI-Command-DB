"""Script defining basic test fr the command dataclass model."""

import dataclasses
import pytest
from model.command import Command

@pytest.fixture
def test_command():
    """Test fixture for proving commands work as intended."""
    test_command = Command(
        command="print",
        description="Prints text to the screen",
        options=[],
        args="str: text to print",
        example="print 'Hello World'",
        cli="Python")
    yield test_command


def test_command_is_frozen(test_command: Command):
    """Tests the dataclass is frozen for command."""
    with pytest.raises(dataclasses.FrozenInstanceError):
        test_command.cli = "git"