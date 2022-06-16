from starlette.routing import Route, Request
from starlette.responses import Response


def labels_endpoint(request: Request) -> Response:
    return Response(status_code=200)


labels_routes = [
    Route('/', labels_endpoint, methods=['POST'])
]
