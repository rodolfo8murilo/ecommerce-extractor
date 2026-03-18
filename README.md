# Ecommerce Extractor

## Setup Instructions

This project utilizes Poetry for dependency management and virtual environment management. Follow the steps below to set up the Poetry virtual environment and run the Kabum crawler.

### Prerequisites
- Ensure you have [Poetry](https://python-poetry.org/docs/#installation) installed on your system.
- Python 3.8 or higher is recommended.
- Ensure you have pre-commit installed:
```bash
sudo apt install pre-commit
```

### Step 1: Clone the Repository

Open your terminal and run the following command to clone the repository:
```bash
git clone https://github.com/rodolfo8murilo/ecommerce-extractor.git
```

### Step 2: Navigate to the Project Directory

Change to the directory of the cloned repository:
```bash
cd ecommerce-extractor
```
### Step 3: Activate the Poetry Environment

```bash
poetry config virtualenvs.in-project true
```
This will create the .venv/ folder.

### Step 4: Install Dependencies

Use Poetry to install the required dependencies:
```bash
poetry install
```

### Step 5: Activate the Poetry Environment

Before running the crawler, activate the Poetry virtual environment:
```bash
poetry env activate
```
### Step 6: Install pre-commit hooks
```bash
pre-commit install
```
### Step 7: Run the Crawler

Once the environment is activated, you can run the Kabum crawler using the following command:
```bash
poetry run scrapy crawl kabum
```

---

Follow these instructions to set up your environment and run the Kabum crawler successfully!
