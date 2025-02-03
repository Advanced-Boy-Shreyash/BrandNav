import requests
import json


class PostAnalyzer:
    def __init__(self, api_url, data_file='data.json', summary_file='summary.txt'):
        self.api_url = api_url
        self.data_file = data_file
        self.summary_file = summary_file

    def fetch_data(self):
        """This function fetch the data from API"""
        try:
            response = requests.get(self.api_url)
            response.raise_for_status()
            return response.json()

        except requests.exceptions.RequestException as e:
            print(f"Error fetching data from API: {e}")
            return None

    def save_data(self, data):
        """The function implement saving functionality"""
        try:
            with open(self.data_file, 'w') as f:
                json.dump(data, f, indent=2)
                f.close()
            return "Data saved Successfully."

        except Exception as e:
            print(f"Error saving data to file: {e}")

    def load_data(self):
        """Loads the data in development environment and returns the data"""
        try:
            with open(self.data_file, 'r') as f:
                data = json.load(f)
                f.close()

            return data

        except FileNotFoundError as e:
            print(f"File not found: {e}")
            return None

        except Exception as e:
            print(f"Something went wrong: {e}")
            return None

    def analyze_data(self, data):
        """Function is performing data analysis interms of total no of post, unique users and average no of words per post"""
        try:
            total_post = len(data)

            # unique users
            user_ids = [post['userId'] for post in data]
            unique_ids = set(user_ids)
            unique_users = len(unique_ids)

            # average words per post
            word_count_per_post = []
            for post in data:
                words_in_post = len(post['body'].split())
                word_count_per_post.append(words_in_post)
            avg_words_per_post = sum(word_count_per_post)/total_post

            return total_post, unique_users, avg_words_per_post

        except Exception as e:
            print(f"Error analyzing data: {e}")
            return None, None, None

    def save_summary(self, total_post, unique_users, avg_words_per_post):
        """The function creates a summary file saving Total no of post, no of unique users and average no of words per post"""
        try:
            with open(self.summary_file, 'w') as f:
                f.write(f'Total Posts: {total_post}\n')
                f.write(f'Unique users: {unique_users}\n')
                f.write(f'Average words per post: {avg_words_per_post:.2f}\n')
                f.close()

        except Exception as e:
            print(f"Error saving summary to file: {e}")

    def process(self):
        # 1. Fetch data form api
        data = self.fetch_data()
        if data:
            self.save_data(data)

        # 2. Data Analysis
            data = self.load_data()
            if data:
                total_post, unique_users, avg_words_per_post = self.analyze_data(
                    data)

        # 3. Generate Summary
                if total_post is not None:
                    self.save_summary(
                        total_post, unique_users, avg_words_per_post)
                    print(f"""Total Posts: {total_post}, Unique Users: {
                          unique_users}, Average Words per Post: {avg_words_per_post:.2f}""")


if __name__ == "__main__":
    api_url = "https://jsonplaceholder.typicode.com/posts"
    analyzer = PostAnalyzer(api_url)
    analyzer.process()
