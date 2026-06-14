import os
import pandas as pd
from pathlib import Path

class Song:
    def __init__(self, track_id, artists, album_name, track_name, popularity, duration_ms,
                 explicit, danceability, energy, key, loudness, mode, speechiness,
                 acousticness, instrumentalness, liveness, valence, tempo, time_signature, track_genre):
       
        self.track_id = track_id
        self.artists = artists
        self.album_name = album_name
        self.track_name = track_name
        self.track_genre = track_genre
        
   
        self.popularity = popularity
        self.duration_ms = duration_ms
        self.explicit = explicit
        self.key = key
        self.loudness = loudness
        self.mode = mode
        self.tempo = tempo
        self.time_signature = time_signature
        
 
        self.danceability = danceability
        self.energy = energy
        self.speechiness = speechiness
        self.acousticness = acousticness
        self.instrumentalness = instrumentalness
        self.liveness = liveness
        self.valence = valence


    def check_string(self, value, field_name):
        if not isinstance(value, str) or not value.strip():
            raise ValueError(f"{field_name} must be a non-empty string.")
        return value.strip()

    def check_range(self, value, min_val, max_val, field_name):
        try:
            val = float(value)
        except (ValueError, TypeError):
            raise ValueError(f"{field_name} must be a numeric value.")
        if not (min_val <= val <= max_val):
            raise ValueError(f"{field_name} must be between {min_val} and {max_val}.")
        return val
    

    def dict_maker(self):
        return {
            'track_id': self.track_id, 'artists': self.artists, 'album_name': self.album_name,
            'track_name': self.track_name, 'popularity': self.popularity, 'duration_ms': self.duration_ms,
            'explicit': self.explicit, 'danceability': self.danceability, 'energy': self.energy,
            'key': self.key, 'loudness': self.loudness, 'mode': self.mode, 'speechiness': self.speechiness,
            'acousticness': self.acousticness, 'instrumentalness': self.instrumentalness,
            'liveness': self.liveness, 'valence': self.valence, 'tempo': self.tempo,
            'time_signature': self.time_signature, 'track_genre': self.track_genre
        }


    @property
    def track_id(self): 
        return self._track_id
    
    @track_id.setter
    def track_id(self, v): 
        self._track_id = self.check_string(v, "track_id")

    @property
    def artists(self): 
        return self._artists
    
    @artists.setter
    def artists(self, v): 
        self._artists = self.check_string(v, "artists")

    @property
    def album_name(self): 
        return self._album_name
    
    @album_name.setter
    def album_name(self, v): 
        self._album_name = self.check_string(v, "album_name")

    @property
    def track_name(self): 
        return self._track_name
    
    @track_name.setter
    def track_name(self, v): 
        self._track_name = self.check_string(v, "track_name")

    @property
    def track_genre(self): 
        return self._track_genre
    
    @track_genre.setter

    def track_genre(self, v): 
        self._track_genre = self.check_string(v, "track_genre")


    @property
    def popularity(self): 
        return self._popularity
    
    @popularity.setter
    
    def popularity(self, v): 
        self._popularity = int(self.check_range(v, 0, 100, "popularity"))

    @property
    def duration_ms(self): 
        return self._duration_ms
    
    @duration_ms.setter

    def duration_ms(self, v):

        if int(v) <= 0:
            raise ValueError("duration_ms must be a positive integer.")
        
        self._duration_ms = int(v)

    @property
    def explicit(self): 
        return self._explicit
    
    @explicit.setter

    def explicit(self, v):
   
        if isinstance(v, str):
            self._explicit = v.lower() in ['true', '1', 'yes']
        else:
            self._explicit = bool(v)

    @property
    def key(self): 
        return self._key

    @key.setter
    def key(self, v):
        self._key = int(self.check_range(v, 0, 11, "key"))

    @property
    def loudness(self): 
        return self._loudness
    
    @loudness.setter

    def loudness(self, v):
        try:
            self._loudness = float(v)

        except (ValueError, TypeError):
            raise ValueError("loudness must be a float value.")

    @property

    def mode(self): 
        return self._mode
    
    @mode.setter
    def mode(self, v):
  
        if int(v) not in [0, 1]:
            raise ValueError("mode must be 0 (Minor) or 1 (Major).")
        
        self._mode = int(v)

    @property
    def tempo(self): 
        return self._tempo
    
    @tempo.setter

    def tempo(self, v):
        if float(v) < 0:
            raise ValueError("tempo (BPM) cannot be negative.")
        
        self._tempo = float(v)

    @property

    def time_signature(self): 
        return self._time_signature
    
    @time_signature.setter
    
    def time_signature(self, v):
        if int(v) <= 0:
            raise ValueError("time_signature must be a positive integer.")
        
        self._time_signature = int(v)



    @property
    def danceability(self): 
        return self._danceability
    
    @danceability.setter
    def danceability(self, v): 
        self._danceability = self.check_range(v, 0.0, 1.0, "danceability")

    @property
    def energy(self): 
        return self._energy
    
    @energy.setter

    def energy(self, v): 
        self._energy = self.check_range(v, 0.0, 1.0, "energy")

    @property
    def speechiness(self): 
        return self._speechiness
    
    @speechiness.setter
    def speechiness(self, v): 
        self._speechiness = self.check_range(v, 0.0, 1.0, "speechiness")

    @property
    def acousticness(self): 
        return self._acousticness
    
    @acousticness.setter
    def acousticness(self, v): 
        self._acousticness = self.check_range(v, 0.0, 1.0, "acousticness")

    @property
    def instrumentalness(self): 
        return self._instrumentalness
    
    @instrumentalness.setter
    def instrumentalness(self, v): 
        self._instrumentalness = self.check_range(v, 0.0, 1.0, "instrumentalness")

    @property
    def liveness(self): 
        return self._liveness
    
    @liveness.setter
    def liveness(self, v): 
        self._liveness = self.check_range(v, 0.0, 1.0, "liveness")

    @property
    def valence(self): 
        return self._valence
    
    @valence.setter
    def valence(self, v): 
        self._valence = self.check_range(v, 0.0, 1.0, "valence")

    def __str__(self):
        return f"Song: {self.track_name} by {self.artists} [{self.track_genre}]"
    

class DataLoader:
    def __init__(self,file_path):
        self.base_path = Path(__file__).resolve().parent.parent
        self.file_path = self.base_path / "data" / "spotify_tracks.csv"
        self.df = None

    def load_data(self) -> pd.DataFrame:
        try:
            if not os.path.exists(self.file_path):
                raise FileNotFoundError(f"The Database file wasn't found in this Path: {self.file_path}")
            
            self.df = pd.read_csv(self.file_path)
            print(f" The file loaded successfully !! number of rows: {len(self.df)}")
            return self.df
        
        except FileNotFoundError as e:
            print(f"\n[SYSTEM ERROR!]: {e}")
            self.df = pd.DataFrame()
            return self.df
        except Exception as e:
            print(f"\n[Unexpected Error happened during loading !!]: {e}")
            self.df = pd.DataFrame()
            return self.df

    def append_song(self, song: Song):
        if self.df is None:
            print("❌ First you should load the database!!!")
            return

        try:
            song_data = song.dict_maker()
            

            last_index = self.df.iloc[:, 0].max() 
            new_index = last_index + 1
            

            final_data = {'index': new_index} 
            final_data.update(song_data)
            
            new_song_df = pd.DataFrame([final_data])
            
            header_needed = False
            new_song_df.to_csv(self.file_path, mode='a', index=False, header=header_needed)

            self.df = pd.concat([self.df, new_song_df], ignore_index=True)
            print(f"✅ Song '{song.track_name}' added successfully!!")
            
        except Exception as e:
            print(f"\n❌ Error adding song: {e}")

    
    def save_clean_data(self, df_clean, file_name):
        if df_clean is None or df_clean.empty:
            print("❌ No cleaned data available to save!")
            return

        reports_dir = self.base_path / "reports"
        reports_dir.mkdir(parents=True, exist_ok=True)

        if not file_name.endswith('.csv'):
            file_name += '.csv'

        save_path = reports_dir / file_name

        if save_path.exists():
            print(f"\n❌ Error: A file named '{file_name}' already exists in the reports folder.")
            print("Please try again with a different name.")
            return

        try:
            df_clean.to_csv(save_path, index=False)
            print(f"✅ Cleaned data successfully saved to: {save_path}")
            
        except Exception as e:
            print(f"\n❌ Error saving file: {e}")