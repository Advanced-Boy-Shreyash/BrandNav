# Python Developer Intern Task

## Objective

The goal of this assignment is to build a Python program that fetches, processes, and analyzes data from an API, demonstrating proficiency in Python programming, clean code, and adherence to best practices.

---

## Project Features

1. **Fetch Data from an API**

   - API Endpoint: `https://jsonplaceholder.typicode.com/posts`
   - Save the fetched data in a local file named `data.json`.

2. **Data Analysis**

   - Calculate:
     - Total number of posts.
     - Number of unique users (`userId` based).
     - Average number of words per post (`body` based).

3. **Generate Summary**

   - Create a `summary.txt` file containing:
     - Total posts.
     - Unique users.
     - Average words per post.

4. **Unit Testing**
   - Functions tested:
     - API fetching.
     - Data processing logic.
     - File generation.
   - Testing framework: `unittest`.

---

## Project Structure

```
Assignment 1
├── main.py
├── data.json
├── summary.txt
├── test_main.py
├── README.md
```

## Execution of Project

1. Pre-requisites:

   - Python 3.8 or above installed.
   - Clone of Project

   ```
   https://github.com/Advanced-Boy-Shreyash/BrandNav
   ```

   - Run below command in the project

   ```
   pip install requirements.txt
   ```

2. Execute the project:
   - To execute the project
   ```
   python main.py
   ```

The code will be running in the terminal you can even tweak the API urls for same response of data.
