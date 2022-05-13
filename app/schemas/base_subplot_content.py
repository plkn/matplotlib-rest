from marshmallow_oneofschema import OneOfSchema

from .hist import Hist, HistSchema
from .plot import Plot, PlotSchema
from ..utils.exporter import export


@export
class BasePlotSchema(OneOfSchema):
    type_schemas = {"plot": PlotSchema, "hist": HistSchema}

    def get_obj_type(self, obj):
        if isinstance(obj, Plot):
            return "plot"
        elif isinstance(obj, Hist):
            return "hist"
        else:
            raise Exception("Unknown object type: {}".format(obj.__class__.__name__))
