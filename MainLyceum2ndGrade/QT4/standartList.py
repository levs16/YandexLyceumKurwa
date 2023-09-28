class DefaultList(list):
    def __init__(self, default):
        super().__init__()
        self.default = default

    def __getitem__(self, index):
        try:
            return super().__getitem__(index)
        except IndexError:
            return self.default
