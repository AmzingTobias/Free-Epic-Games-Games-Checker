import requests
import gui
from datetime import datetime


class Epic_games_browser():
    def __init__(self):
        pass

    def get_games_webpage(self):
        # Access the website on epic games that returns json for the free games available
        contents = requests.get(
            url="https://store-site-backend-static.ak.epicgames.com/freeGamesPromotions?locale=en-US&country=GB&allowCountries=GB"
        )
        # Takes the returned information in json and stores it in a variable
        free_games = contents.json()
        # There is more json than needed for what the use case is
        # So only the games are extracted from the data
        free_games_list = free_games["data"]["Catalog"]["searchStore"]["elements"]
        valid_game_list = []
        # Looks at each game to store in a list
        for game in free_games_list:
            title = game["title"]
            # The effective date is needed as they sometimes showcase free games for the next week
            # However these free games will not be available at time of running
            # So should not be shown
            date = game["effectiveDate"]
            # The productSlug is the url that is added to the store page products url
            # To get to the products page
            product_link = game["productSlug"]
            # The effective date is in [yyyy-mm-ddThh-mm-ss-SSSZ]
            # Only the date is really, so the string is split at the T and then only the first bit of the list is needed
            # for the date
            date = (date.split("T")).pop(0)
            # Checks the date against the current date and if valid is added to the list
            if self.check_in_date(date):
                valid_game_list.append([title, product_link])
            # The games are then sorted alphabetically by product title
            # Not needed but could for useability
            self.free_games_valid_list = sorted(
                valid_game_list, key=lambda valid_game_list: valid_game_list[0]
            )

    def check_in_date(self, date):
        # Converts the string date into a date time, just to make sure it's the same format as pythons
        # It is then checked against the present date
        past = datetime.strptime(str(date), "%Y-%m-%d")
        present = datetime.now()
        if past.date() < present.date():
            return True


def main_code():
    epic_games = Epic_games_browser()
    epic_games.get_games_webpage()
    gui.createWindow(epic_games.free_games_valid_list)


if __name__ == "__main__":
    main_code()
