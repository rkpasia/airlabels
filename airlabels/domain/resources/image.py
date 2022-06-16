from typing import Optional

from airlabels.domain.resources.resource import BaseResource, ResourceKind


class ImageResource(BaseResource):

    def __init__(self, resource_id: Optional[str] = 0):
        self.id = resource_id
        self.kind = ResourceKind.IMAGE
