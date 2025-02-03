# Bulk Document Generator

## Overview

Bulk Document Generator is a Streamlit-based application that automates the creation of PDF and Word documents from an Excel file containing employee details. The application allows users to upload an Excel file, process the data, and generate downloadable documents for each entry.

### Features

- Upload an Excel file containing employee details.
- Generate PDF and Word documents for each employee
- Download generated documents directly from the app.
- Error handling for smooth processing.

## Installation
- Install the required dependencies:

```
    pip install -r requirements.txt
```

- Run the application with the following command:

```
    streamlit run generate_documents.py
```

## Input File Format

The uploaded Excel file should have the following columns:

- Name
- Email
- Company Name
- Position
- Joining Date

## Output

For each row in the Excel file, the app generates:

    - A PDF file with employee details.
    - A Word (.docx) file with the same details.

## Folder Structure

```
Assignment 4
    │── app.py
    │── output/  # Contains generated PDF and Word files
    │── requirements.txt
    │── README.md
```
