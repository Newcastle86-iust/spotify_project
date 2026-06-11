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

    def compare_scatter_by_top_genres(self, x_col, y_col, top_n= 10):
        
        top_genres = self.df_after.groupby('track_genre')['popularity'].mean().nlargest(top_n).index.tolist()
        
        df_before_filtered = self.df_before[self.df_before['track_genre'].isin(top_genres)]
        df_after_filtered = self.df_after[self.df_after['track_genre'].isin(top_genres)]
        
        fig, axes = plt.subplots(1, 2, figsize=(18, 7))
        
        sns.scatterplot(data=df_before_filtered, x=x_col, y=y_col, hue='track_genre', 
                        palette='viridis', ax=axes[0], alpha=0.6, s=50)
        axes[0].set_title(f"Before: {self.label_before}")
        axes[0].get_legend().remove() 
        
        sns.scatterplot(data=df_after_filtered, x=x_col, y=y_col, hue='track_genre', 
                        palette='viridis', ax=axes[1], alpha=0.6, s=50)
        axes[1].set_title(f"After: {self.label_after}")
        
        axes[1].legend(bbox_to_anchor=(1.05, 1), loc='upper left', title="Top Genres")
        
        plt.suptitle(f"Comparison: {x_col} vs {y_col} for Top {top_n} Genres", fontsize=16)
        plt.tight_layout()
        plt.show()