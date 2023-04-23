from plyer import notification

from informant.messengers import Messenger


class DesktopMessenger(Messenger):
    def __init__(self):
        pass

    def notify(self, **kwargs) -> None:
        opts = {
            "title": kwargs["header"],
            "message": kwargs["message"],
            "timeout": 15,
        }
        notification.notify(**opts)