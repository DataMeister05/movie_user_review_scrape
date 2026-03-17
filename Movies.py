import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.imdb.com/chart/top/"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

response = requests.get(url, headers=headers)

print("Status Code:", response.status_code)

if response.status_code != 200:
    print("Failed to retrieve page")
    exit()

soup = BeautifulSoup(response.text, "html.parser")

movies = soup.select("li.ipc-metadata-list-summary-item")

movie_data = []

for movie in movies:

    title_tag = movie.select_one("h3.ipc-title__text")
    title = title_tag.text.strip() if title_tag else "N/A"

    # remove ranking number
    if ". " in title:
        title = title.split(". ", 1)[1]

    year_tag = movie.select_one("span.cli-title-metadata-item")
    year = year_tag.text.strip() if year_tag else "N/A"

    rating_tag = movie.select_one("span.ipc-rating-star--rating")
    rating = rating_tag.text.strip() if rating_tag else "N/A"

    movie_data.append({
        "Title": title,
        "Year": year,
        "Rating": rating
    })

for movie in movie_data[:10]:
    print(f"{movie['Title']} ({movie['Year']}) - Rating: {movie['Rating']}")

df = pd.DataFrame(movie_data)
df.to_csv("imdb_top_25_python.csv", index=False)

print("\nData saved to imdb_top_25_python.csv")



