# Cholesterol Distribution Analysis

This project visualizes the distribution of total cholesterol levels among 55-year-old males in the United States.

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Linux/Mac
# or
.\venv\Scripts\activate  # On Windows
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Analysis

Run the main script:
```bash
python main.py
```

This will generate a visualization showing:
- The distribution of cholesterol levels
- An arrow pointing to the 184 mg/dL threshold
- The percentage of people above and below 184 mg/dL
- The mean cholesterol level

The output will be saved as 'cholesterol_distribution.png' in the project directory. 