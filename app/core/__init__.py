from matplotlib import pyplot

from schemas.figure import FigureParams


def build_figure(fig_p: FigureParams):
    pyplot.figure(facecolor=fig_p.facecolor,
                  edgecolor=fig_p.edgecolor,
                  tight_layout=fig_p.tight_layout
                  )

    for subpl in fig_p.subplots:
        subpl.subplot
        pyplot.subplot(fig_p.subplot_rows, fig_p.subplot_columns, subpl["index"])
        p = subpl["subplot"]

        if p.type == "plot":
            pyplot.plot()
        elif subpl.type == "hist":
            pyplot.hist()

    pyplot.show()