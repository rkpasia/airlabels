from starlette.routing import Route
from starlette.requests import Request
from starlette.responses import Response


def resources_endpoint(request: Request) -> Response:
    return Response(status_code=200)


resources_routes = [
    Route("/", resources_endpoint, methods=["POST"])
]