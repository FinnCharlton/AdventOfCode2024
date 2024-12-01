from dotenv import load_dotenv
import os
import requests

class Importer():

    def __init__(self, day):

        load_dotenv()

        self.baseurl = f"https://adventofcode.com/2024/day/{str(day)}/input"

        self.cookie = os.getenv("SESSION")

    def load(self):

        headers = {"Cookie": f"session={self.cookie}"}
        content = requests.get(self.baseurl, headers=headers)

        if content.status_code == 200:
            return content.text
        else:
            return f"Error retrieving data, error code {content.status_code}"

