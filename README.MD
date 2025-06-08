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

1. **Clone the repository**:

2. **Set up the virtual environment**:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `.\venv\Scripts\activate`
   ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

### Scripts

- running the app:

  ```bash
  flask run # with `--debug` for debug mode
  ```

- updating dependencies:

  ```bash
  pip freeze > requirements.txt
  ```
