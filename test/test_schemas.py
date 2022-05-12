from src.schemas.figure import FigureSchema, Figure
from src.schemas.line import Plot
from src.schemas.subplot import Subplot


def test_figure_scheme_serialization():
    plot = Plot("12", "bb")
    subplot = Subplot(plot, index=2)
    figure = Figure([subplot])
    figure_schema = FigureSchema()
    result = figure_schema.dump(figure)
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
