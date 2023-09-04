from services.VariantData import VariantData


class VcfProcessor:
    def __init__(self, stream, parser, httpx_wrapper):
        self.stream = stream
        self.parser = parser
        self.httpx_wrapper = httpx_wrapper
        self.variantData = VariantData()

    async def loadFromStream(self, start, end, minDP, limit, deNovo):
        try:
            async for line in self.stream:
                if line.startswith("#"):
                    self.variantData.columns = line[1:].split("\t")
                    continue

                row = line.split("\t")
                rowData = {}
                for index, header in enumerate(self.variantData.columns):
                    rowData[header] = row[index]

                # Processing each row as it's read in order to not exceed out of memory
                await self.processRow(rowData, start, end, minDP, limit, deNovo)

                # Finishing the program once it reaches the limit for all the samples
                if self.variantData.limitReachedCount >= len(self.variantData.samples): break

        except Exception as e:
            print("Error loading VCF Data from stream:", e)

    async def processRow(self, rowData, start, end, minDP, limit, deNovo):
        try:
            # Process each sample data for the current variant row
            for sample in self.variantData.samples:
                if not self.variantData.samplesLimitReached[sample] and rowData[sample] != "./.:.:.:.:.:.:.":
                    await self.processData(sample, rowData, start, end, minDP, limit, deNovo)
        except Exception as e:
            print("Error processing variant Row:", e)

    async def processData(self, sample, rowData, start, end, minDP, limit, deNovo):
        pass
