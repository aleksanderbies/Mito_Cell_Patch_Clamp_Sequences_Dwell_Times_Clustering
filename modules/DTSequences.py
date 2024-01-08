import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

class OCO_Sequence:
    def __init__(self, path, category, is_first_open):
        self.path = path
        self.category = category
        self.is_first_open = is_first_open
        
    def prepare_time_series(self):
        data_list = self.read_time_series_from_file()
        samples = self.generate_samples(data_list)
        return samples
    
    def read_time_series_from_file(self):
        file = open(self.path, "r")
        data = file.read()
        data_list = data.split("\n")
        file.close()
        data_list.pop()
        return data_list

    def check_first_open(self, df):
        if not self.is_first_open:
            df = df.iloc[1: , :]
        return df

    def generate_samples(self, data_list):
        samples = []
        for i in range(0,len(data_list)-2, 2):
            signal = [data_list[i], data_list[i+1], data_list[i+2]]
            samples.append(signal)
        return samples
    
    def scale(self, df):
        values = df.values
        min_max_scaler = MinMaxScaler()
        df_scaled = min_max_scaler.fit_transform(values)
        df_scaled = pd.DataFrame(df_scaled)
        df_scaled.columns = df.columns
        return df_scaled
    
    def make_DataFrame(self):
        samples = self.prepare_time_series()
        columns=["o1", "c", "o2"]
        df = pd.DataFrame(samples, columns=columns)
        df = self.scale(df)
        category = [self.category for i in range (df.shape[0])]
        df.loc[:,'category'] = category
        df = self.check_first_open(df)
        return df