from collections import defaultdict
import requests
import json
import os
from src.config import TARGET_PATH, URL


class Homework:

    def __init__(self, url: str, target_path: str) -> None:
        self.url = url
        self.target_path = target_path

    def download_data(self):
        try:
            response = requests.request('GET', self.url)
            if (response == None) or (response.status_code != 200):
                raise ResourceWarning()
            else:
                return response

        except ResourceWarning:
            print('Resource not found !')




    def create_defaultdict(self, json_data: json) -> defaultdict:
        my_dict = defaultdict(list)
        {my_dict[currency["code"]].append(line_data["name"]) for line_data in json_data for currency in line_data["currencies"]}
        return my_dict


    def save_dict_to_file(self, my_dict: defaultdict) -> None:
        try:
            os.makedirs(TARGET_PATH, exist_ok=True)
            for code in my_dict.keys():
                counter = 1
                with open(f'{self.target_path}{code}.txt', mode='w', encoding="UTF-8") as file:
                    for name in my_dict[code]:
                        file.write(f'{counter}. {name}\n')
                        counter += 1;

        except Exception:
            print('File write failed !')
            raise Exception



if __name__ == '__main__':
    homework = Homework(URL, TARGET_PATH)
    response = homework.download_data()
    json_data = json.loads(response.content)
    my_dict=homework.create_defaultdict(json_data)
    homework.save_dict_to_file(my_dict)







