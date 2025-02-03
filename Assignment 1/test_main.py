import unittest
from unittest.mock import patch, mock_open, MagicMock
import json
from main import PostAnalyzer

# Define sample data at the global scope
sample_data = [
    {"userId": 1, "id": 1, "title": "Test Title 1", "body": "Test body of post 1."},
    {"userId": 2, "id": 2, "title": "Test Title 2",
        "body": "Another test body of post 2."},
]


class TestPostAnalyzer(unittest.TestCase):

    def setUp(self):
        self.api_url = "https://jsonplaceholder.typicode.com/posts"
        self.analyzer = PostAnalyzer(self.api_url)

    @patch('requests.get')
    def test_fetch_data(self, mock_get):
        # Mock API response
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = sample_data

        data = self.analyzer.fetch_data()
        self.assertEqual(data, sample_data)

    @patch('builtins.open', new_callable=mock_open)
    def test_save_data(self, mock_file):
        # Test saving data to a file
        result = self.analyzer.save_data(sample_data)
        mock_file.assert_called_once_with(self.analyzer.data_file, 'w')

        # Verify the data written to the file
        written_data = ''.join(call[0][0]
                               for call in mock_file().write.call_args_list)
        self.assertEqual(json.loads(written_data), sample_data)

        self.assertEqual(result, "Data saved Successfully.")

    @patch('builtins.open', new_callable=mock_open, read_data=json.dumps(sample_data))
    def test_load_data(self, mock_file):
        # Test loading data from a file
        data = self.analyzer.load_data()
        mock_file.assert_called_once_with(self.analyzer.data_file, 'r')
        self.assertEqual(data, sample_data)

    def test_analyze_data(self):
        # Test analyzing data
        total_posts, unique_users, avg_words_per_post = self.analyzer.analyze_data(
            sample_data)
        self.assertEqual(total_posts, 2)
        self.assertEqual(unique_users, 2)
        self.assertAlmostEqual(avg_words_per_post, 5.5)

    @patch('builtins.open', new_callable=mock_open)
    def test_save_summary(self, mock_file):
        # Test saving summary to a file
        self.analyzer.save_summary(2, 2, 5.5)
        mock_file.assert_called_once_with(self.analyzer.summary_file, 'w')
        mock_file().write.assert_any_call('Total Posts: 2\n')
        mock_file().write.assert_any_call('Unique users: 2\n')
        mock_file().write.assert_any_call('Average words per post: 5.50\n')


if __name__ == "__main__":
    unittest.main()
