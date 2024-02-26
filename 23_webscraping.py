import requests
from bs4 import BeautifulSoup
from collections import defaultdict

website = "https://en.wikipedia.org/wiki/List_of_countries_by_carbon_dioxide_emissions_per_capita"
response = requests.get(website)
soup = BeautifulSoup(response.content, "html.parser")

table = soup.find("table", class_="sortable")
columns = ["Country", "1980", "2018"]
data = defaultdict(dict)

for row in table.find_all("tr")[1:]:
    cells = row.find_all("td")

    if len(cells) >= 8:
        country_name = cells[0].text.strip()
        year_1980 = cells[2].text.strip()
        year_2018 = cells[7].text.strip()

        data[country_name][columns[0]] = country_name
        data[country_name][columns[1]] = year_1980
        data[country_name][columns[2]] = year_2018

for country in data:
    print(f"{country}: {data[country]}")