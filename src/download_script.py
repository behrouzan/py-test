import requests

download_url = "https://raw.githubusercontent.com/fivethirtyeight/data/master/nba-elo/nbaallelo.csv"
# download_url = "https://www.w3schools.com/python/pandas/data.csv"
target_file_pah = "files/nba_data.csv"

response = requests.get(download_url)
response.raise_for_status()  # check if was successful ==>> this will throw http error if in case of fail

with open(target_file_pah, "wb") as f:
    f.write(response.content)

print("Download Completed")
