import json

from src.schemas.figure import FigureSchema, Figure
from src.schemas.hist import Hist
from src.schemas.plot import Plot
from src.schemas.subplot import Subplot


def test_figure_scheme_serialization():
    plot = Plot("12", "bb")
    hist = Hist("21", "cc")
    subplot_1 = Subplot(plot, index=1)
    subplot_2 = Subplot(hist, index=2)
    figure = Figure([subplot_1, subplot_2])
    figure_schema = FigureSchema()
    result = figure_schema.dump(figure)
    json_result = json.dumps(result)
    restored = figure_schema.load(result)
    pass


def test_figure_scheme_deserialization():
    schema = FigureSchema()
    result = schema.load({
        "edgecolor": "red",
        "subplot_columns": 2,
        "subplot_rows": 2,
        "subplots": [
            {
                "index": 3,
                "plot": {}
            }
        ]
    })
    pass
