from marshmallow import Schema, fields, post_load, pre_load, post_dump, pre_dump


class Plot:
    def __init__(self, field_a, field_b):
        self.field_b = field_b
        self.field_a = field_a
        # self.lines = lines


class PlotSchema(Schema):
    field_a = fields.String(required=True)
    field_b = fields.String(required=True)

    # lines = fields.List(fields.Nested(LineSchema))

    @post_load
    def load_plot(self, data, **kwargs):
        return Plot(**data)
