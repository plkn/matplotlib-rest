from marshmallow import Schema, fields, post_load

from ..utils.exporter import export


@export
class ResponseSchema(Schema):
    image_url = fields.String(required=True, description="URL of a result image")
