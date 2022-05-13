from marshmallow import Schema, fields, post_load, pre_load, post_dump, pre_dump


class Hist:
    def __init__(self, field_c, field_d):
        self.field_c = field_c
        self.field_d = field_d




class HistSchema(Schema):
    field_c = fields.String(required=True)
    field_d = fields.String(required=True)

    @post_load
    def load_hist(self, data, **kwargs):
        return Hist(**data)