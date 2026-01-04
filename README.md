# CO2 Climate Analysis Project

This is a beginner-friendly Python project that analyzes CO2 emissions data
to identify trends over time and visualize climate-related information.

---

## Dataset
Source: Kaggle _ CO2 Emissions by Country
The dataset contains yearly CO2 emission values for multiple countries.

Main columns:
- country_code
- country_name
- year
- value

---

## Project Structure
co2-climate-project/
├── data/
│ └── co2.csv
├── src/
│ └── main.py
├── outputs/
│ ├── figures/
│ └── tables/
├── requirements.txt
└── README.md

---

## Tools & Technologies
- Python
- pandas
- matplotlib
- pathlib (Python standard library)

---

## Setup & Installation
Create a virtual environment (recommended) and install dependencies:

```bash
pip install -r requirements.txt

How to Run the Project

From the project root directory, run:

python src/main.py


.The script will:

.load the CO2 dataset

.clean the data

.generate a CO2 trend plot for a selected country

.save the figure in outputs/figures/

###Author

Manuel Nseguet Tchamfa / Data Scientist Student an der Technischen Hochschule Nürnberg