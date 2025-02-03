import os
import unittest
from unittest.mock import patch, MagicMock
import pandas as pd
from generate_documents import generate_pdf, generate_word, process_excel


class TestGenerateDocuments(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        os.makedirs("output", exist_ok=True)

    @classmethod
    def tearDownClass(cls):
        for file in os.listdir("output"):
            os.remove(os.path.join("output", file))
        os.rmdir("output")

    def test_generate_pdf(self):
        pdf_path = generate_pdf(
            "John Doe", "john@example.com", "ExampleCorp", "Developer", "2023-01-01")
        self.assertTrue(os.path.exists(pdf_path))
        self.assertTrue(pdf_path.endswith(".pdf"))

    def test_generate_word(self):
        word_path = generate_word(
            "John Doe", "john@example.com", "ExampleCorp", "Developer", "2023-01-01")
        self.assertTrue(os.path.exists(word_path))
        self.assertTrue(word_path.endswith(".docx"))

    @patch('generate_documents.pd.read_excel')
    def test_process_excel(self, mock_read_excel):
        mock_df = pd.DataFrame({
            'Name': ['John Doe'],
            'Email': ['john@example.com'],
            'Company Name': ['ExampleCorp'],
            'Position': ['Developer'],
            'Joining Date': ['2023-01-01']
        })
        mock_read_excel.return_value = mock_df

        generated_files = process_excel("dummy_path.xlsx")
        self.assertEqual(len(generated_files), 1)
        pdf_path, word_path = generated_files[0]
        self.assertTrue(os.path.exists(pdf_path))
        self.assertTrue(os.path.exists(word_path))


if __name__ == '__main__':
    unittest.main()
