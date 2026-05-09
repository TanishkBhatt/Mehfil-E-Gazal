import json

def get_song_names(songs_dataset: str) -> list[str]:
    with open(songs_dataset, "r") as f:
        data = json.load(f)
    return list(data.keys())

def fetch_song(songs_dataset: str, song_name: str) -> dict:
    with open(songs_dataset, "r") as f:
        data = json.load(f)
    if song_name in data:
        return data[song_name]
    return {}