"""Defines all types, base classes, and dataclasses used in the package."""
from abc import ABC, abstractmethod
from dataclasses import dataclass, field

# NOTE: dataclass for secrets


@dataclass
class TaskInfo:
    """Dataclass that holds information about a task.

    An instance of this class is passed to the notify method of all messengers. \
    If creating a custom messenger, you can use these fields to construct a \
    notification message.

    Args:
        name: A string containing the name of the function being run.
        send_result: Boolean indicating whether results should be sent.
        send_args: Boolean indicating whether args and kwargs should be sent.
        args: Tuple containing the arguments passed to the function.
        kwargs: Dictionary containing the keyword arguments passed to the function.
        result: A string containing the return result of the function, or the traceback.
        header: A string containing a summary line for the notification header.
        has_errored: A boolean indicating whether the function raised an exception.
    """

    name: str = ""
    send_result: bool = True
    send_args: bool = True
    args: tuple = ()
    kwargs: dict = field(default_factory=dict)
    result: str = ""
    header: str = ""
    has_errored: bool = False


class Messenger(ABC):
    """Abstract base class for all messengers."""

    @abstractmethod
    def set_secrets(self, secrets: dict) -> None:
        """Receive and set secrets used for the messenger.

        This method is abstract and must be implemented by all subclasses.

        Args:
            secrets: Secrets that need to be set for the messenger.
        """
        pass

    @abstractmethod
    def notify(self, info: TaskInfo) -> None:
        """Send a notification to the user.

        This method is abstract and must be implemented by all subclasses.

        Args:
            info: TaskInfo object containing information about the function that can \
            be used to construct the notification message.
        """
        pass
