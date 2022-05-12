from marshmallow import Schema, fields, post_load, pre_load, post_dump


class Line:
    def __init__(self, y, x=None, label=None, fmt=None, linewidth=1):
        self.x = x
        self.y = y
        self.label = label
        self.fmt = fmt
        self.linewidth = linewidth


class LineSchema(Schema):
    x = fields.List(fields.Float, description="", required=False)
    y = fields.List(fields.Float, description="")
    label = fields.String(description="Line label", required=False)
    fmt = fields.String(description="Line format", required=False, load_default="r-")
    linewidth = fields.Float(description="", required=False, load_default=1)

    @post_load
    def load_line(self, data, **kwargs):
        return Line(**data)


class Plot:
    def __init__(self, field_a, field_b):
        self.field_b = field_b
        self.field_a = field_a
        # self.lines = lines


class Hist:
    def __init__(self, field_c, field_d):
        self.field_c = field_c
        self.field_d = field_d


class BasePlotSchema(Schema):
    __plot_type__ = ""
    __model__ = Plot

    @pre_load
    def unwrap_envelope(self, data, **kwargs):
        return data[self.__plot_type__]

    @post_load
    def deserialize_object(self, data, **kwargs):
        return self.__model__(**data)

    @post_dump
    def wrap_with_envelope(self, data, **kwargs):
        pass
        # return {self.__plot_type__: data}


# class PlotSchema(Schema):
class PlotSchema(BasePlotSchema):
    __plot_type__ = "plot"
    __model__ = Plot
    field_a = fields.String(required=True)
    field_b = fields.String(required=True)

    # lines = fields.List(fields.Nested(LineSchema))

    @post_load
    def load_plot(self, data, **kwargs):
        return Plot(**data)


class HistSchema(BasePlotSchema):
    __plot_type__ = "hist"
    field_c = fields.String(required=True)
    field_d = fields.String(required=True)

    @post_load
    def load_hist(self, data, **kwargs):
        return Hist(**data)
