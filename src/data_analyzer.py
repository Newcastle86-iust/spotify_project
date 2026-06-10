import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

class DataAnalyzer:
    def __init__(self, df_before: pd.DataFrame, df_after: pd.DataFrame, processing_label: str = "None"):
        self.df_before = df_before
        self.df_after = df_after
        self.processing_label = processing_label

    def get_correlation_matrix(self):
        print(f"\n--- Correlation Matrix (BEFORE: Raw Data) ---")
        print(self.df_before.select_dtypes(include=['number']).corr())
        
        print(f"\n--- Correlation Matrix (AFTER: {self.processing_label}) ---")
        print(self.df_after.select_dtypes(include=['number']).corr())

    def plot_heatmap(self):
            plt.figure(figsize=(10, 8))
            corr_before = self.df_before.select_dtypes(include=['number']).corr()
            sns.heatmap(corr_before, annot=True, cmap='coolwarm', fmt=".2f", annot_kws={"size": 8})
            plt.title("Before Cleaning (Raw Data)")
            plt.show() 

            plt.figure(figsize=(10, 8))
            corr_after = self.df_after.select_dtypes(include=['number']).corr()
            sns.heatmap(corr_after, annot=True, cmap='coolwarm', fmt=".2f", annot_kws={"size": 8})
            plt.title(f"After Cleaning ({self.processing_label})")
            plt.show()