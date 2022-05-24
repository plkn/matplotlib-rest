from matplotlib import pyplot

from schemas.figure import Figure


def build_figure(fig: Figure):
    pyplot.figure(facecolor=fig.facecolor,
           edgecolor=fig.edgecolor,
           tight_layout=fig.tight_layout
           )

    for subpl in fig.subplots:
        pyplot.subplot(fig.subplot_rows, fig.subplot_columns, subpl["index"])
        p = subpl["subplot"]

        if p.type == "plot":
            pyplot.plot()
        elif subpl.type == "hist":
            pyplot.hist()

    pyplot.show()