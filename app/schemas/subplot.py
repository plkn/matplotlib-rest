from marshmallow import Schema, fields

from utils.exporter import export
from .base_subplot_content import BasePlotSchema


class SubplotParams:
    def __init__(self, subplot, index=1):
        self.subplot = subplot
        self.index = index


@export
class SubplotSchema(Schema):
    index = fields.Integer(description="Index of a subplot in a subplots grid", load_default=1)
    subplot = fields.Nested(BasePlotSchema, description="Content of a subplot. Either plot, hist or another "
                                                        "matplotlib function.", required=True)
