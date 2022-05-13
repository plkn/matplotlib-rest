from marshmallow import Schema, fields, post_load

from ..utils.exporter import export


class Plot:
    def __init__(self, field_a, field_b):
        self.field_b = field_b
        self.field_a = field_a
        # self.lines = lines


@export
class PlotSchema(Schema):
    field_a = fields.String(required=True)
    field_b = fields.String(required=True)

    # lines = fields.List(fields.Nested(LineSchema))

    @post_load
    def load_plot(self, data, **kwargs):
        return Plot(**data)
