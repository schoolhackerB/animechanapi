# Pip is the official package manager for installing, 
# requests talks to http clients
import requests

# this works woohoo
a_name = input("Enter an anime to receive a random quote from it: ")
def get_random_anime_quote():
    # The Animechan API endpoint for a random quote by anime + endpoints for specific anime name
    url = f"https://api.animechan.io/v1/quotes/random?anime={a_name}"

    # RAN INTO A PROBLEM HERE:    edit: FIXED IT
    try:
        #send a GET request to the API
        response = requests.get(url)
        #process JSON data returned by the API n returns dictionary or list
        info = response.json()
            
            # The API returns the data inside a 'data' object
        quote_info = info['data']
            
        print(f"Anime: {quote_info['anime']['name']}")
        print(f"Character: {quote_info['character']['name']}")
        print(f"Quote: \"{quote_info['content']}\"")          
    except Exception as e:
        print("An error occurred; anime likely isn't in the database. Try a more popular anime!")

# Run the function
# i tried putting in a parameter, naruto, but it says they are not allowed. the solution was fixing my variables and my url
get_random_anime_quote()

# this is important maybe? edit: no its not also this is the endpoint for all 
# def get_anime_quote():
#     url = "https://api.animechan.io/v1/quotes/random"
