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

# Running with Docker

You can also run the crawler using Docker without installing dependencies locally.

## Prerequisites

Make sure Docker is installed on your machine.

### Check if Docker is already installed

```bash
docker --version
```

If the command is not found, install Docker using the following steps (Ubuntu/Debian):

### Install Docker

```bash
sudo apt update
sudo apt install docker.io
```

### Enable and start Docker

```bash
sudo systemctl enable docker
sudo systemctl start docker
```

### Allow your user to run Docker without sudo

```bash
sudo usermod -aG docker $USER
```

After that, restart your session or run:

```bash
newgrp docker
```

### Test Docker installation

```bash
docker run hello-world
```

If you see the hello-world message, Docker is working correctly.

---

## Step 1: Build the Docker Image

Inside the project root directory, run:

```bash
docker build -t scrapy-app .
```

This will create a Docker image named `scrapy-app`.

---

## Step 2: Run the Kabum Crawler

To run the Kabum spider:

```bash
docker run -v $(pwd):/app scrapy-app kabum
```

---

## Step 3: Run with Custom Number of Pages

To pass arguments to the spider, use the `-a` flag:

```bash
docker run -v $(pwd):/app scrapy-app kabum -a pages=3
```

This will run the Kabum spider scraping 3 pages.

---

## Why use `-v $(pwd):/app`?

This mounts your current project directory into the Docker container so that files such as:

- `products.db`
- exported files
- logs

are saved in your local project folder instead of being lost when the container stops.

---

## Example Commands

### Run default crawl
```bash
docker run -v $(pwd):/app scrapy-app kabum
```

### Run scraping 5 pages
```bash
docker run -v $(pwd):/app scrapy-app kabum -a pages=5
```

### Run another spider
```bash
docker run -v $(pwd):/app scrapy-app spider_name
```

---

## Useful Docker Commands

### View running containers
```bash
docker ps
```

### View all containers
```bash
docker ps -a
```

### View Docker images
```bash
docker images
```
---
Follow these instructions to set up your environment and run the Kabum crawler successfully!
