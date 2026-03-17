IMDb User Reviews Scraper
This Python script allows you to scrape user reviews for movies from IMDb and store them in separate CSV files. It utilizes the IMDbPY package  and BeautifulSoup to gather movie URLs and scrape user reviews.

Prerequisites Before using this script, make sure you have the following installed:

Python: This script is written in Python. Chrome WebDriver: You need to download the Chrome WebDriver and provide its path in the script. This WebDriver is used to control the Chrome browser. Required Python Packages: Install the required packages using the following command:

pip install requests beautifulsoup4 pandas

Steps to clone and run the script:
1) Clone the repository or download the script to your local machine.
2) Install the required packages using the command mentioned above.
3) Download the Chrome WebDriver and set the PATH variable in the script to the path of the WebDriver on your machine.
4) Run the script using the command: python Movie.py
5) Then, the script will scrape user reviews for each movie from the IMDb URLs and store them in imdb_top_25_python CSV file.
