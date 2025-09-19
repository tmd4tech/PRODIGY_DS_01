import pandas as pd
import matplotlib.pyplot as plt

# Load the data, skipping metadata rows
df = pd.read_csv("Population_data/API_SP.POP.TOTL_DS2_en_csv_v2_38144.csv", skiprows=4)

# Check which years are available
available_years = [col for col in df.columns if col.isdigit()]
print("Available years:", available_years)

# Choose the latest available year with data
for year in sorted(available_years, reverse=True):
    if df[year].notna().sum() > 0:
        selected_year = year
        break

# Prepare data for plotting
df_plot = df[["Country Name", selected_year]].dropna()
df_plot[selected_year] = pd.to_numeric(df_plot[selected_year], errors="coerce")
df_plot = df_plot.dropna().sort_values(by=selected_year, ascending=False)

# Plot bar chart (top 20 countries for readability)
plt.figure(figsize=(12, 8))
plt.bar(df_plot["Country Name"][:20], df_plot[selected_year][:20], color="skyblue")
plt.xticks(rotation=75, ha='right')
plt.title(f"Top 20 Country Populations in {selected_year}")
plt.xlabel("Country")
plt.ylabel("Population")
plt.tight_layout()
plt.show()