import requests
import json
import webbrowser
import threading
import os
import time
from flask import Flask, render_template, jsonify, request

# Initialize Flask app
app = Flask(__name__)

# Global variable for game list cache and cache file name
CACHE_FILE = "game_list_cache.json"
game_list_cache = []
# Global thread object to track the data fetching task
data_fetch_thread = None

def fetch_data_from_url(url, source_name):
    """
    Fetch JSON data from a specified URL.
    """
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, timeout=30, headers=headers)
        response.raise_for_status()
        print(f"Successfully fetched data from {source_name}.")
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Warning: Could not fetch data from {source_name}. Error: {e}")
    except json.JSONDecodeError:
        print(f"Warning: Failed to parse data from {source_name}.")
    return None

def fetch_steam_games():
    """
    Fetches the game list from Steam's official API.
    Loads from a local cache if available, otherwise fetches from the network and creates the cache.
    """
    global game_list_cache
    
    if os.path.exists(CACHE_FILE):
        try:
            with open(CACHE_FILE, "r", encoding="utf-8") as f:
                game_list_cache = json.load(f)
                if game_list_cache:
                    print(f"Successfully loaded {len(game_list_cache)} games from local cache {CACHE_FILE}.")
                    return
        except (json.JSONDecodeError, IOError) as e:
            print(f"Failed to read cache file: {e}. Refetching from the network.")

    print("Local cache is empty or invalid, fetching the latest game list from Steam API...")
    
    steam_data = fetch_data_from_url("https://api.steampowered.com/ISteamApps/GetAppList/v2/", "steam")
    
    if not steam_data:
        print("Error: Could not fetch the official Steam app list. Unable to proceed.")
        return

    steam_apps = steam_data.get('applist', {}).get('apps', [])
    
    # Filter out apps with no name
    filtered_list = [app for app in steam_apps if app.get('name')]
    
    game_list_cache = filtered_list
    print(f"Successfully fetched and processed {len(game_list_cache)} apps from the network.")

    try:
        with open(CACHE_FILE, "w", encoding="utf-8") as f:
            json.dump(game_list_cache, f, ensure_ascii=False, indent=4)
            print(f"Successfully wrote the game list to cache file {CACHE_FILE}.")
    except IOError as e:
        print(f"Error: Failed to write to cache file: {e}")


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/games')
def get_games():
    return jsonify(game_list_cache)

def shutdown_server():
    """Function to shut down the Werkzeug server."""
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        print('Not running with the Werkzeug Server. Forcing exit.')
        # A more forceful shutdown for other servers
        os._exit(0)
    func()

@app.route('/api/shutdown', methods=['POST'])
def shutdown():
    """Shutdown endpoint."""
    print("Shutdown request received. Shutting down server...")
    shutdown_server()
    return 'Server shutting down...'

def open_browser():
    # Delay opening to ensure the server has started
    time.sleep(1)
    webbrowser.open_new('http://127.0.0.1:5000/')


if __name__ == '__main__':
    # Start loading data in the background on startup
    data_fetch_thread = threading.Thread(target=fetch_steam_games)
    data_fetch_thread.start()

    # Open the browser in a separate thread
    threading.Thread(target=open_browser).start()
    
    app.run(host='127.0.0.1', port=5000, debug=False, use_reloader=False)
