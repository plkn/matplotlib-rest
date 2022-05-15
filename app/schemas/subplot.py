from marshmallow import Schema, fields

from .base_subplot_content import BasePlotSchema
from utils.exporter import export


class Subplot:
    def __init__(self, content, index=1):
        self.content = content
        self.index = index


@export
class SubplotSchema(Schema):
    index = fields.Integer(description="Index of a subplot in a subplots grid", load_default=1)
    content = fields.Nested(BasePlotSchema, description="Content of a subplot. Either plot, hist or another "
                                                        "matplotlib function.", required=True)
