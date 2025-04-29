# 🕷️ Django Web Scraping App

A web application built with Django that performs web scraping to extract, process, and display data from external websites.

## 🚀 Features

- Scrape content from target websites (e.g., titles, articles, product info)
- Store scraped data in a Django database
- Display results on the frontend
- Manual and scheduled scraping
- Admin interface for managing scraped data

## 🛠️ Tech Stack

- **Backend**: Django (Python)
- **Frontend**: HTML, CSS, Bootstrap
- **Scraping**: BeautifulSoup, Requests
- **Database**: SQLite (default), PostgreSQL/MySQL compatible

## 📂 Project Structure

webscraper_project/ ├── scraper/ # Django app for scraping logic │ ├── views.py │ ├── models.py │ ├── urls.py │ └── scraper_utils.py ├── templates/ │ └── index.html ├── static/ ├── manage.py └── requirements.txt


## 🧪 How It Works

1. User triggers a scraping task from the web interface.
2. Django view handles the request and calls `scraper_utils.py`.
3. Scraper fetches data using `requests`, parses HTML using `BeautifulSoup`.
4. Extracted data is saved to the database.
5. Results are rendered in the frontend.

## ✅ Setup Instructions

```bash
# Clone the repository
git clone https://github.com/yourusername/django-web-scraper.git
cd django-web-scraper

# Create and activate a virtual environment
python -m venv env
source env/bin/activate  # For Linux/Mac
env\Scripts\activate     # For Windows

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Start the development server
python manage.py runserver
