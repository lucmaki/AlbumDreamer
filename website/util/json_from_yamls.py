import os
import yaml
import json

def read_yaml_file(filepath):
    with open(filepath, 'r') as file:
        return yaml.safe_load(file)

def create_albums_json(albums_dir, output_file):
    albums = []
    
    # Traverse through all the albums directories
    for album_dir in os.listdir(albums_dir):
        album_path = os.path.join(albums_dir, album_dir)
        
        # Check if it's a directory
        if os.path.isdir(album_path):
            # Read album info
            album_info = read_yaml_file(os.path.join(album_path, 'info.yaml'))
            album_info['id'] = int(album_dir)
            album_info['cover'] = f'/albums/{album_dir}/cover.jpg'
            
            # Traverse through all the tracks directories
            tracks = []
            tracks_dir = os.path.join(album_path, 'tracks')
            for track_dir in os.listdir(tracks_dir):
                track_path = os.path.join(tracks_dir, track_dir)
                
                # Check if it's a directory
                if os.path.isdir(track_path):
                    # Read track info
                    track_info = read_yaml_file(os.path.join(track_path, 'info.yaml'))
                    track_info['id'] = int(track_dir)
                    track_info['image'] = f'/albums/{album_dir}/tracks/{track_dir}/visual.jpg'
                    track_info['track'] = f'/albums/{album_dir}/tracks/{track_dir}/track.wav'
                    
                    tracks.append(track_info)
            
            album_info['tracks'] = tracks
            albums.append(album_info)
    
    # Write albums to JSON file
    with open(output_file, 'w') as file:
        json.dump(albums, file, ensure_ascii=False, indent=4)

# Define the albums directory and the output JSON file
ALBUMS_DIR = 'website/albums'
OUTPUT_FILE = 'website/_data/albums.json'
    
create_albums_json(ALBUMS_DIR, OUTPUT_FILE)