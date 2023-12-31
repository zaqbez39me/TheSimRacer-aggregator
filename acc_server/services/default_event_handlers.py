from .event_handler import ServerHandler
from .server_event import ServerEvent, SessionCompleted, EventEnd, SessionPhaseChanged


class OnSessionCompleted(ServerHandler):

    @staticmethod
    def checker(event: ServerEvent):
        return isinstance(event, SessionCompleted)


class OnEventEnd(ServerHandler):

    @staticmethod
    def checker(event: ServerEvent):
        return isinstance(event, EventEnd)


class OnSessionPhaseChanged(ServerHandler):

    @staticmethod
    def checker(event: ServerEvent):
        return isinstance(event, SessionPhaseChanged)
