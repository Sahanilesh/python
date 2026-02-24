import requests

def get_random_joke():
    url = "https://api.freeapi.app/api/v1/public/randomjokes/joke/random"
    response = requests.get(url)
    data = response.json()
    if data["success"] and "data" in data:
        joke = data["data"]
        joke_data = data["data"]["content"]
        return joke_data
    else:
        raise Exception("Failed to featch user data")

def main():
    try:
        joke = get_random_joke()
        print(f"Joke of the day is: {joke}")
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()