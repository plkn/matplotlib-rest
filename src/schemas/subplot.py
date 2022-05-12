from marshmallow import Schema, fields

from src.schemas import PlotSchema
from src.schemas.line import BasePlotSchema


class Subplot:
    def __init__(self, plot, index=1):
        self.plot = plot
        self.index = index


class SubplotSchema(Schema):
    index = fields.Integer(description="Index of a subplot in a subplots grid", load_default=1)
    plot = fields.Nested(BasePlotSchema, description="", required=True)
