from enum import IntEnum
from typing import List, Type, TypeVar

from readchar import readkey

from config.config import TEXT

T = TypeVar("T")


class StateOptions(IntEnum):
    """Base enum class for possible actions in game state"""

    def __repr__(self) -> str:
        return f"{self.value} - {self.name}"

    @classmethod
    def list_options(cls: Type[T]) -> List[str]:
        """Returns the options as a list of strings for terminal output"""
        return [repr(option) for option in cls]


class State:
    """Base class for game state. Displays, holds, and reads options for state change"""

    @staticmethod
    def check_input(option_type: Type[T]) -> T:
        """Receives user input and returns corresponding StateOption"""
        print(*option_type.list_options(), sep="\n")
        print(TEXT["MISC"]["PROMPT"], end="\n" * 2)
        try:
            choice = readkey()
            chosen_option = option_type(int(choice))
            print(chosen_option.name, end="\n" * 2)
            return option_type(chosen_option)
        except ValueError:
            print(TEXT["MISC"]["OPTION_ERROR"])
