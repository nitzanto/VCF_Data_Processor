class VcfProcessor:
    def __init__(self, stream, parser, httpx_wrapper):
        self.stream = stream
        self.parser = parser
        self.httpx_wrapper = httpx_wrapper
        self.columns = []

    async def loadFromStream(self, start, end, minDP, limit, deNovo):
        async for line in self.stream:
            if line.startswith("#"):
                self.columns = line[1:].split("\t")
                continue

            row = line.split("\t")
            rowData = {}
            for index, header in enumerate(self.columns):
                rowData[header] = row[index]