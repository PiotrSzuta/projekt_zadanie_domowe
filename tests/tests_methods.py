import unittest
import json
from src.config import URL, TARGET_PATH
from src.zadanie import Homework
from collections import defaultdict


class TestHomework(unittest.TestCase):


    def setUp(self):
        self.homework = Homework(url=URL, target_path=TARGET_PATH)


    def test_download_data(self):
        response = self.homework.download_data()
        self.assertEqual(200, response.status_code)


    def test_create_defaultdict(self):
        response = self.homework.download_data()
        json_data = json.loads(response.content)
        result = self.homework.create_defaultdict(json_data)

        self.assertIsInstance(result, defaultdict)
        self.assertGreater(len(result), 0)



    def test_save_dict_to_file(self):
        response = self.homework.download_data()
        json_data = json.loads(response.content)
        result = self.homework.create_defaultdict(json_data)
        self.assertRaises(Exception, self.homework.save_dict_to_file, None)



if __name__ == '__main__':
    unittest.main()
