class DataFiltering:

    def filterByPosition(self, rowData, start, end):
        return start <= rowData["POS"] <= end

    def fitlerByMinDP(self, rowData, minDP, sample):
        try:
            formatFields = rowData["FORMAT"].split(":")
            dpIndex = formatFields.index('DP')
            sampleFields = rowData[sample].split(":")
            dpValue = int(sampleFields[dpIndex])
            return dpValue > minDP
        except Exception as e:
            print('Error when filtering by minDP', e)

    def check_de_novo(self, sample, row_data, de_novo):
        try:
            if sample != "proband":
                return True

            if de_novo:
                both_parents_missing = (
                        row_data["father"] == "./.:.:.:.:.:.:." and
                        row_data["mother"] == "./.:.:.:.:.:.:."
                )
                if both_parents_missing:
                    return True

            if not de_novo:
                at_least_one_parent_present = (
                        row_data["father"] != "./.:.:.:.:.:.:." or
                        row_data["mother"] != "./.:.:.:.:.:.:."
                )
                if at_least_one_parent_present:
                    return True

            return False
        except Exception as error:
            raise Exception(f"Error checking deNovo: {str(error)}")
