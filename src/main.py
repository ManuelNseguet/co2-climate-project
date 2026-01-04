from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

# --------------------
# Paths
# --------------------
ROOT_DIR = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT_DIR / "data" / "co2.csv"
FIGURES_PATH = ROOT_DIR / "outputs" / "figures"

FIGURES_PATH.mkdir(exist_ok=True)

# --------------------
# Main function
# --------------------
def main():
    # Load data
    df = pd.read_csv(DATA_PATH)

    print("Columns in dataset:")
    print(df.columns)
    print("\nFirst rows:")
    print(df.head())

    # Basic cleaning
    df = df.dropna()

    # Filter one country (example: World or Aruba)
    country = "World"
    df_country = df[df["country_name"] == country]

    # Plot CO2 over time
    if "year" in df_country.columns and "value" in df_country.columns:
        plt.figure(figsize=(8, 5))
        plt.plot(df_country["year"], df_country["value"])
        plt.xlabel("Year")
        plt.ylabel("CO2 value")
        plt.title(f"CO2 over time - {country}")

        output_file = FIGURES_PATH / f"co2_{country.lower()}_over_time.png"
        plt.savefig(output_file)
        plt.close()

        print(f"Figure saved to {output_file}")
    else:
        print("⚠️ Required columns not found.")

if __name__ == "__main__":
    main()
