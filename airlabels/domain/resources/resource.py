from enum import Enum


class ResourceKind(Enum):
    IMAGE = 1


class BaseResource:
    """
    Base class to define airlabels resources
    """

    id: str
    kind: ResourceKind
