from abc import ABC, abstractmethod
import pandas as pd
import numpy as np
from sklearn.impute import KNNImputer

class BaseImputer(ABC):
    def __init__(self):
       self.method_name = "None"
    @abstractmethod
    def impute(self, df, column):
        pass

class MeanImputer(BaseImputer):
    def impute(self, df, column):
        self.method_name = "Mean Imputation"
        mean_value = df[column].mean()
        df[column] = df[column].fillna(mean_value)
        return df

class MedianImputer(BaseImputer):
    def impute(self, df, column):
        self.method_name = "Median Imputation"
        median_value = df[column].median()
        df[column] = df[column].fillna(median_value)
        return df

class KNNMissingImputer(BaseImputer):
    def __init__(self, n_neighbors=5):
        self.method_name = "KNN Imputation"
        self.n_neighbors = n_neighbors
        self.imputer = KNNImputer(n_neighbors=self.n_neighbors)

    def impute(self, df,columns):
        df_imputed = df.copy()
        df_imputed[columns] = self.imputer.fit_transform(df_imputed[columns])
        return df_imputed




class BaseOutlierHandler(ABC):
    @abstractmethod
    def handle(self, df, column):
        pass

class IQROutlierHandler(BaseOutlierHandler):
    def handle(self, df, column):
        Q1 = df[column].quantile(0.25)
        Q3 = df[column].quantile(0.75)
        IQR = Q3 - Q1
        
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        

        df[column] = np.clip(df[column], lower_bound, upper_bound)
        return df

class ZScoreOutlierHandler(BaseOutlierHandler):
    def __init__(self, threshold=3):
        self.threshold = threshold

    def handle(self, df, column):
        mean = df[column].mean()
        std = df[column].std()
        
        lower_bound = mean - self.threshold * std
        upper_bound = mean + self.threshold * std
        
        df[column] = np.clip(df[column], lower_bound, upper_bound)
        return df