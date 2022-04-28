class Figure:
    def __init__(self, subplots, tight_layout=False, edgecolor='white', facecolor='white', subplot_columns=1, subplot_rows=1):
        self.edgecolor = edgecolor
        self.facecolor = facecolor
        self.tight_layout = tight_layout
        self.subplot_columns = subplot_columns
        self.subplot_rows = subplot_rows
        self.subplots = subplots

