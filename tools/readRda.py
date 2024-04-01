import rdata
import pandas as pd

class ReadRda:
    def __init__(self, rda_file=None, para=None, csv_file=None):
        self.rda_file = rda_file
        self.para = para
        self.csv_file = csv_file
        self.read()

    def read(self):
        self.rda = rdata.read_rda(self.rda_file)
        return self.rda

    def get_dict(self, rda=None, para=None):
        if rda is None:
            rda = self.read()

        if para is None:
            para = self.para

        rda_dict = rda[para]
        return rda_dict

    def to_csv(self, rda=None, para=None, csv_file=None):
        if rda is None:
            rda = self.read()

        if para is None:
            para = self.para

        if csv_file is None:
            if self.csv_file is None:
                csv_file = para + '.csv'
            else:
                csv_file = self.csv_file

        df = pd.DataFrame.from_dict(self.get_dict(rda, para))
        df.to_csv(csv_file, index=False)