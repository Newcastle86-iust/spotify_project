from src.data_loader import DataLoader, Song
from src.data_analyzer import DataAnalyzer
from src.data_visualizer import DataVisualizer
from src.data_cleaner import MeanImputer, MedianImputer, KNNMissingImputer, IQROutlierHandler, ZScoreOutlierHandler
import numpy as np
import subprocess
import platform

import seaborn as sns
import matplotlib.pyplot as plt
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
csv_path = BASE_DIR / "data" / "spotify_tracks.csv"

def get_input(prompt: str):

    value = input(f"\n{prompt} (or type 'back' to return to menu): ").strip()
    if value.lower() in ['back', 'cancel']:
        raise ValueError("User requested return to main menu")
    
    return value

def clear_screen():
    command = 'cls' if platform.system() == 'Windows' else 'clear'

    subprocess.run(command, shell=True)

def get_current_data(df_raw, df_clean):
    return df_clean if df_clean is not None else df_raw

def main():
    loader = DataLoader(file_path=csv_path)
    df_raw = None
    df_clean = None
    processing_label = "Raw Data"

    while True:
        clear_screen()
        print("\n=================== Spotify Data Studio & Management System ===================")
        print("1. Load Dataset & View Missing Values Report")
        print("2. Clean Missing Values (Mean / Median / KNN)")
        print("3. Handle Outliers (IQR / Z-Score)")
        print("4. Add a New Song to the Dataset (Interactive Input)")
        print("5. Calculate Genre Insights & Correlation Matrix")
        print("6. Generate Advanced Visualizations (Plots)")
        print("7. Exit")
        print("================================================================================")
        
        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            df_raw = loader.load_data()
            processing_label="Raw Data"
            if not df_raw.empty:
                print("Missing Values per column:\n", df_raw.isnull().sum())

            input("\nPress any key to continue !!")
        
    
        elif choice == '2':
            if df_raw is None: input("❌ First load data"); continue
            
            numeric_cols = df_raw.select_dtypes(include=[np.number]).columns.tolist()
            
            print(f"\nAvailable numeric columns: {numeric_cols}")
            col = input("Enter column name (or press Enter to apply to ALL): ").strip()
            
            print("1. Mean | 2. Median | 3. KNN")
            method = input("Select method: ")

            method_names = {'1': 'Mean Imputer', '2': 'Median Imputer', '3': 'KNN Imputer'}
            selected_method = method_names.get(method, 'Unknown')

            if (processing_label!="Raw Data"):
                processing_label+=f"and  {selected_method}"

            else:
                processing_label=selected_method
            
            df_clean = df_raw.copy()
            
            target_cols = [col] if col else numeric_cols
            
            for c in target_cols:
                if method == '1': df_clean = MeanImputer().impute(df_clean, c)
                elif method == '2': df_clean = MedianImputer().impute(df_clean, c)
                elif method == '3': df_clean = KNNMissingImputer().impute(df_clean, [c])
                else: df_clean = KNNMissingImputer().impute(df_clean, [c])
            
            print(f"✅ Missing values handled for: {target_cols}")
            input("\nPress Enter...")


        elif choice == '3':
            if df_raw is None: input("❌ First load data"); continue
            if df_clean is None: df_clean = df_raw.copy()
            
            numeric_cols = df_clean.select_dtypes(include=[np.number]).columns.tolist()
            
            print(f"\nAvailable numeric columns: {numeric_cols}")
            col = input("Enter column name (or press Enter to apply to ALL): ").strip()
            
            print("1. IQR | 2. Z-Score")

           


            method = input("Select: ")

            method_names = {'1': 'IQR', '2': 'Z-Score'}
            selected_method = method_names.get(method, 'Unknown')

            if (processing_label!="Raw Data"):
                processing_label+=f"and  {selected_method}"

            else:
                processing_label=selected_method
            
            target_cols = [col] if col else numeric_cols
            
            handler = IQROutlierHandler() if method == '1' else ZScoreOutlierHandler()
            
            for c in target_cols:
                df_clean = handler.handle(df_clean, c)
            
            print(f"✅ Outliers handled successfully for: {target_cols}")
            input("\nPress Enter to continue...")


        elif choice == '4':
            print("\n--- Add New Song (Type 'back' at any time to cancel) ---")
            
            def get_valid_input(prompt, type_func, min_val=None, max_val=None):
                while True:
                    user_input = get_input(prompt)
                    try:
                        val = type_func(user_input)
                        if (min_val is not None and val < min_val) or (max_val is not None and val > max_val):
                            print(f"❌ Value must be between {min_val} and {max_val}.")
                            continue
                        return val
                    except ValueError:
                        print(f"❌ Invalid format. Please enter a valid {type_func.__name__}.")

                    input("\nPress any key to continue !!")


            

            try:
                new_song = Song(
                            track_id=get_input("Enter Track ID:"),
                            artists=get_input("Enter Artist(s):"),
                            album_name=get_input("Enter Album Name:"),
                            track_name=get_input("Enter Track Name:"),
                            popularity=get_valid_input("Enter Popularity (0-100):", int, 0, 100),
                            duration_ms=get_valid_input("Enter Duration (ms):", int, 1000),
                            explicit=get_input("Is it Explicit? (True/False):").capitalize() == 'True',
                            danceability=get_valid_input("Enter Danceability (0.0-1.0):", float, 0.0, 1.0),
                            energy=get_valid_input("Enter Energy (0.0-1.0):", float, 0.0, 1.0),
                            key=get_valid_input("Enter Key (0-11):", int, 0, 11),
                            loudness=get_valid_input("Enter Loudness (e.g. -5.0):", float),
                            mode=get_valid_input("Enter Mode (0 or 1):", int, 0, 1),
                            speechiness=get_valid_input("Enter Speechiness (0.0-1.0):", float, 0.0, 1.0),
                            acousticness=get_valid_input("Enter Acousticness (0.0-1.0):", float, 0.0, 1.0),
                            instrumentalness=get_valid_input("Enter Instrumentalness (0.0-1.0):", float, 0.0, 1.0),
                            liveness=get_valid_input("Enter Liveness (0.0-1.0):", float, 0.0, 1.0),
                            valence=get_valid_input("Enter Valence (0.0-1.0):", float, 0.0, 1.0),
                            tempo=get_valid_input("Enter Tempo (e.g. 120.0):", float, 0.0),
                            time_signature=get_valid_input("Enter Time Signature (3-7):", int, 3, 7),
                            track_genre=get_input("Enter Genre:")
                        )
                
                loader.append_song(new_song) 
                df_clean = None
                df_raw = None
                processing_label = "Raw Data"
                print("\n✅ Song added successfully to Database!!. Data is now 'dirty'. Please run Cleaning (Option 2) again!")

                input("\nPress any key to continue !!")

                
            except ValueError as e:
                if str(e) == "User requested return to main menu":
                    print("↩️ Returning to main menu...")
                else:
                    print("❌ An unexpected error occurred.")

                input("\nPress any key to continue !!")


        elif choice == '5':
            current_df = get_current_data(df_raw, df_clean)
            if current_df is None: input("❌ Load data first!"); continue
            
            analyzer = DataAnalyzer(df_raw, current_df , processing_label=processing_label)

            print("\n1. Show Correlation Matrix (Text)")
            print("2. Show Correlation Heatmap (Graphic)")
            sub_choice = input("Select view: ")

            if sub_choice == '1':
                print(analyzer.get_correlation_matrix())
            elif sub_choice == '2':
                analyzer.plot_heatmap()
            
            input("\nPress Enter to continue...")

        elif choice == '6':
            if df_raw is None: input("❌ Load data first!"); continue
            if df_clean is None: input("❌ Load data first!"); continue

            print("1. Compare Outliers (Box Plot)")
            print("2. Compare Trends (Scatter Plot)")
            print("3. Show Distribution (Hist Plot)")
            sub_choice = input("Select plot type: ")
            
            current_label = processing_label if df_clean is not None else "Raw Data"
            vis = DataVisualizer(df_raw, df_clean if df_clean is not None else df_raw, 
                     label_before="Raw Data", label_after=current_label)
            
            if sub_choice == '1': vis.compare_outliers('danceability')
            elif sub_choice == '2': vis.compare_scatter('energy', 'danceability')
            elif sub_choice == '3': vis.plot_distribution('danceability')

            input("\nPress any key to continue !!")

            
        elif choice == '7':
            print("\nExiting system. Goodbye!")
            break
        else:
            print("\nInvalid choice, please try again.!!!")
            input("\nPress any key to continue !!")


if __name__ == "__main__":
    main()