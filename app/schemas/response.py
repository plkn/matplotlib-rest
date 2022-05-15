from marshmallow import Schema, fields

from utils.exporter import export


class Response:
    def __init__(self, image_url):
        self.image_url = image_url


@export
class ResponseSchema(Schema):
    image_url = fields.String(required=True, description="URL of a result image")
