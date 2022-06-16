from typing import Optional, Sequence

from starlette.applications import Starlette
from starlette.routing import Mount
from airlabels.webservice.scopes.resources import resources_routes
from airlabels.webservice.scopes.labels import labels_routes


def server_factory(debug: Optional[bool] = False) -> Starlette:
    """
    Factory that builds airlabels's webservice application instance

    :param debug: Whether to start the airlabels web service in debug mode or not
    :return: ASGI Starlette application instance
    """

    airlabels_routes = [
        Mount('/resources', routes=resources_routes),
        Mount('/labels', routes=labels_routes)
    ]

    return Starlette(debug=debug, routes=airlabels_routes)
