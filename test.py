# Pip is the official package manager for installing, 
# requests talks to http clients
import requests

# 
def get_random_anime_quote():
    # The Animechan API endpoint for a random quote by anime
    url = "https://api.animechan.io/v1/quotes/random?anime=<anime_name>"
    
    try:
        #send a GET request to the API
        response = requests.get(url)

            #parse the JSON data returned by the API
            data = response.json()
            
            # The API returns the data inside a 'data' object
            quote_info = data['data']
            
            print(f"Anime: {quote_info['anime']['name']}")
            print(f"Character: {quote_info['character']['name']}")
            print(f"Quote: \"{quote_info['content']}\"")
        else:
            print(f"Failed to retrieve quote. Status code: {response.status_code}")
            
    except Exception as e:
        print(f"An error occurred: {e}")

# Run the function
get_random_anime_quote()

def get_anime_quote():
    url = "https://api.animechan.io/v1/quotes/random"