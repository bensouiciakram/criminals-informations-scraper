# Criminals Information Scraper

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

## Description

This Python project is a web scraper that collects information about wanted criminals from multiple sites. The scraper extracts fields like first name, last name, gender, country, date of birth, address, source URL, age, firm name, and full name of the criminals. The scraped data is then stored in a structured format using pandas for further analysis and manipulation.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Supported Sites](#supported-sites)
- [Data Format](#data-format)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Clone this repository to your local machine.
2. Install the required dependencies using pip:

```bash
pip install pandas scrapy
```
## Usage 
To start scraping, run the following command in the terminal:

```bash
scrapy crawl criminals -o site_id.csv
```
The scraper will start collecting information from the supported sites and save the data into a CSV file named "site_id.csv.

## Data Format
The scraped data will be stored in CSV format with the following fields:

first_name: The first name of the criminal.
last_name: The last name of the criminal.
gender: The gender of the criminal.
country: The country where the criminal is wanted.
date_of_birth: The date of birth of the criminal.
address: The last known address of the criminal.
source_url: The URL of the page where the information was scraped from.
age: The age of the criminal.
firm_name: The name of the law enforcement firm handling the case.
full_name: The full name of the criminal (combining first and last name).

## License
This project is licensed under the MIT License - see the LICENSE file for details.


