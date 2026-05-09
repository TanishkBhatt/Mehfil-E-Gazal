import json
import os

def available_songs(songs_filepath: str) -> list[str]:
    songs = []
    for song in os.listdir(f"{songs_filepath}"):
        songs.append(os.path.splitext(song)[0])
    return songs

def recommend_more(songs_list: str, singer_name: str, categories: list[str]) -> tuple[list, list]:
    with open(songs_list, "r") as f:
        data = json.load(f)

    rec_by_singer = set()
    rec_by_category = set()

    for song, details in data.items():
        if details["Singer"] == singer_name:
            if song in available_songs("datasets/audio"):
                rec_by_singer.add((song, details["Singer"]))
        else:
            for category in details["Category"]:
                if category in categories:
                    if song in available_songs("datasets/audio"):
                        rec_by_category.add((song, details["Singer"]))

    res = list(rec_by_singer)[:3], list(rec_by_category)[:3]
    return res