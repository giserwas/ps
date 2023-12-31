import requests

def amap_poi_search(keywords, city, citylimit=True, output="json", offset=20, page=1):

    # Amap API URL for place text search
    url = "https://restapi.amap.com/v3/place/text"
    
    # Please replace with your own Amap API key
    api_key = "YOUR_AMAP_API_KEY"

    # Parameters for the API request
    params = {
        "key": api_key,
        "keywords": keywords,
        "city": city,
        "citylimit": str(citylimit).lower(),
        "output": output,
        "offset": offset,
        "page": page,
    }

    # Send the API request
    response = requests.get(url, params=params)

    # Check if the request was successful (HTTP status code 200)
    if response.status_code == 200:
        # Parse the response JSON
        result = response.json()
        return result
    else:
        # Print an error message if the request fails
        print(f"Request failed, HTTP status code: {response.status_code}")
        return None

def main():
    # Set search keywords and city name
    keywords = "**"
    city = "**"

    # Send the search request
    result = amap_poi_search(keywords, city)

    # Process the search result
    if result:
        pois = result.get("pois", [])
        if pois:
            for poi in pois:
                print(f"Name: {poi['name']}\tAddress: {poi['address']}")
        else:
            print("No relevant POI information found.")
    else:
        print("Search failed.")

if __name__ == "__main__":
    main()
