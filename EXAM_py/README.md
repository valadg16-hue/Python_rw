# Retail Sales Data Analyzer

## Project Overview
A Python-based tool to process, analyze, and visualize retail sales data.
Built for Practical Exam | Set A — Red & White Skill Education.

## Technologies Used
- **Python 3**
- **Pandas** – Data loading and manipulation
- **NumPy** – Numerical calculations
- **Matplotlib** – Plotting charts
- **Seaborn** – Enhanced visualization styling

## Files
| File | Description |
|------|-------------|
| `retail_analyzer.py` | Main Python script |
| `retail_sales.csv` | Sample dataset |
| `README.md` | This file |

## Setup Instructions

### 1. Install Required Libraries
Open terminal and run:
```
pip install pandas numpy matplotlib seaborn
```

### 2. Run the Program
```
python retail_analyzer.py
```

### 3. Enter the CSV Path
When prompted, type the path to `retail_sales.csv` or just press **Enter** to use the default (same folder).

## Features
1. **Data Input & Validation** – Loads CSV and checks for required columns and missing values
2. **OOP Design** – `RetailAnalyzer` class with clean methods
3. **Data Metrics** – Total sales, average sales, most popular product
4. **Data Filtering** – Filter by category, product, or date range
5. **Visualizations** – Bar chart, line graph, heatmap (saved as PNG files)

## Filter Examples (used in code)
```
category=Electronics
category=Fruits
product=Laptop
date_from=2024-02-01
date_to=2024-02-28
```

## Output Charts
- `bar_chart.png` – Total sales by category
- `line_graph.png` – Sales trend over time
- `heatmap.png` – Quantity sold by product and category
