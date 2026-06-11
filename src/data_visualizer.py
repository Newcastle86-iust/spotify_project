import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

class DataVisualizer:
    def __init__(self, df_before, df_after, label_before="Raw Data", label_after="Processed Data"):
        self.df_before = df_before
        self.df_after = df_after
        self.label_before = label_before
        self.label_after = label_after

    def compare_outliers(self, column: str):
        fig, axes = plt.subplots(1, 2, figsize=(14, 6))
        
        # max_val = max(self.df_before[column].max(), self.df_after[column].max())
 
        
    
        sns.boxplot(data=self.df_before, y=column, ax=axes[0], color='salmon')
        axes[0].set_title(f"Before: {self.label_before}")
        

        sns.boxplot(data=self.df_after, y=column, ax=axes[1], color='lightgreen')
        axes[1].set_title(f"After: {self.label_after}")
        
        plt.suptitle(f"Box Plot: '{column}'", fontsize=16)
        plt.show()

    
    def compare_scatter(self, x_col: str, y_col: str):
        fig, axes = plt.subplots(1, 2, figsize=(14, 6))
        
        sns.scatterplot(data=self.df_before, x=x_col, y=y_col, ax=axes[0], color='salmon', alpha=0.6)
        axes[0].set_title(f"Before: {self.label_before}")
        
        sns.scatterplot(data=self.df_after, x=x_col, y=y_col, ax=axes[1], color='lightgreen', alpha=0.6)
        axes[1].set_title(f"After: {self.label_after}")
        
        plt.suptitle(f"Relationship Trend Analysis: {x_col} vs {y_col}", fontsize=16)
        plt.show()

    def plot_distribution(self, column: str):

        plt.figure(figsize=(10, 5))
        sns.histplot(self.df_before[column], kde=True, color='salmon')
        
        plt.title(f"Raw Data")


        plt.figure(figsize=(10, 5))
        sns.histplot(self.df_after[column], kde=True, color='skyblue')
        
        plt.title(f"Distribution of '{column}'\n(Processed via: {self.label_after})")
        plt.show()


    def get_valid_column(self, prompt):

        numeric_cols = self.df_after.select_dtypes(include=[np.number]).columns.tolist()
        while True:
            col = input(f"{prompt} (Available: {', '.join(numeric_cols)}): ").strip()
            if col in numeric_cols:
                return col
            print(f"\n❌ Error: '{col}' is not a valid numeric column. Please try again.")