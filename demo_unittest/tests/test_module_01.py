import unittest
import requests

class IndexPageTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("\nset up class..")
        cls.url = "http://localhost:5000"
        cls.example_username = "Josh"

    def get(self, api_endpoint, query_string=None):
        query_string = query_string if query_string else ''
        res = requests.get(self.url + api_endpoint + '?' + query_string)
        return  res.json(), res.status_code
        
    @classmethod
    def tearDownClass(cls):
        print("\ntear down class..")
     
    def test_add_user(self):
        print(f"\nadd user {self.example_username}.")
        api_endpoint = "/add_user"
        query_string = f"name={self.example_username}"
        res_json, status_code = self.get(api_endpoint, query_string)
        self.assertEqual(200, status_code)
        if res_json['add']:
            self.assertEqual(query_string.split('=')[1], res_json['add'])
            self.assertEqual('success', res_json['status'])
        else:
            self.assertEqual('', res_json['add'])
            self.assertEqual('already exists', res_json['status'])

    def test_user_info(self):
        print(f"\nuser info {self.example_username}." )
        api_endpoint = "/user_info"
        res_json, status_code = self.get(api_endpoint)
        self.assertEqual(200, status_code)
        self.assertIn("user_info", res_json)
    
    def test_delete_user(self):
        print(f"\ndelete user {self.example_username}.")
        api_endpoint = "/delete_user"
        query_string = f"name={self.example_username}"
        res_json, status_code = self.get(api_endpoint, query_string)
        self.assertEqual(200, status_code)


if __name__ == "__main__":
    unittest.main()