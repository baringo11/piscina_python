import csv

# NO ESTÁ ACABADO

class CsvReader():
    def __init__(self, filename=None, sep=',', header=False, skip_top=0, skip_bottom=0):
        print("class csv init")
        self.filename = filename
        self.sep = sep
        self.header = header
        self.skip_top = skip_top
        self.skip_bottom = skip_bottom
        self.file = None
        self.data = None

    def __enter__(self):
        print("Ingresando al contexto")
        csv_reader = csv.reader(self.file, delimiter=self.sep)
        self.data = [row for row in csv_reader]
        if self.header:
            self.header_data = self.data.pop(0)
        if self.skip_top > 0:
            self.data = self.data[self.skip_top:]
        if self.skip_bottom > 0:
            self.data = self.data[:-self.skip_bottom]
        return self

    def __exit__(self):
        print("Saliendo del contexto")
        if self.file is not None:
            self.file.close()

    def getdata(self):
        """ Retrieves the data/records from skip_top to skip bottom.
        Return:
        nested list (list(list, list, ...)) representing the data.
        """
        if self.data is None:
            return None
        return self.data

    def getheader(self):
        """ Retrieves the header from csv file.
        Returns:
        list: representing the data (when self.header is True).
        None: (when self.header is False).
        """
        if self.header is False:
            return None
        return self.header_data


if __name__ == "__main__":
    with CsvReader('good.csv') as file:
        data = file.getdata()
        header = file.getheader()
    with CsvReader('bad.csv') as file:
        if file == None:
            print("File is corrupted")