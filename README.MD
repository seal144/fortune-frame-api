# Fortune Frame

Fortune Frame is a web app for saving values of user assets (like FIAT currencies, cryptocurrencies, and precious metals) and converting these assets to other units based on current rates.

## Development Setup

Follow these instructions to set up the project in your local development environment.

### Prerequisites

#### Software

- Python 3.13
- Virtualenv
- Docker Desktop

#### VSC Extensions

- Python
- Ruff

### Installation

1. **Clone the repository**

2. **Set up the virtual environment**:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `.\venv\Scripts\activate`
   ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the database and adminer**:

   ```bash
   docker compose up # with `-d` for detached mode (background - with no logs in terminal)
   ```

   - on windows there might be a problem with running .sh files (`db-setup.sh: cannot execute: required file not found`), related to CRLF line endings, the `git config --global core.autocrlf true` might not work, the simplest solution is to create the .sh files and copy the content from the original files.

## Scripts

- running the app:

  ```bash
  flask run # with `--debug` for debug mode (flask debug mode can be also set in .env file (FLASK_DEBUG))
  ```

- updating dependencies:

  ```bash
  pip freeze > requirements.txt
  ```

## Development Database

- on localhost:5432
- adminer on localhost:8080
- username: postgres
- password: postgres
- database: fortune_frame

## API Documentation

- http://localhost:5000/docs

## License

[MIT](LICENSE)
