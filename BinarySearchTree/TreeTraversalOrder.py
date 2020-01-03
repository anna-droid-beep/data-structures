from enum import Enum, auto


class AutoName(Enum):
    def _generate_next_value_(name, start, count, last_values):
        return name


class TreeTraversalOrder(AutoName):
    PRE_ORDER = auto()
    IN_ORDER = auto()
    POST_ORDER = auto()
    LEVEL_ORDER = auto()

    @staticmethod
    def values():
        return [name for name, _ in TreeTraversalOrder.__members__.items()]
