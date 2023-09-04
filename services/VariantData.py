class VariantData:
    def __init__(self):
        self.columns = []
        self.limitReachedCount = 0
        self.samplesLimitReached = {}
        self.samples = self.columns[self.columns.index("FORMAT") + 1:]
