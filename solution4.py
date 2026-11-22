"""Plot population of ASEAN countries as groups over the years 2004 - 2014"""

import matplotlib.pyplot as plt

from population_reader import population_reader


def calculate(data):
    """Extracting the population of ASEAN countries for 2014"""
    result = {}
    asean_countries = [
        "Brunei Darussalam",
        "Cambodia",
        "Indonesia",
        "Laos",
        "Malaysia",
        "Myanmar",
        "Philippines",
        "Singapore",
        "Thailand",
        "Timor-Leste",
        "Vietnam",
    ]
    for record in data():
        year = int(record["Year"])
        country = record["Country Name"]
        if 2004 <= year <= 2014 and country in asean_countries:
            population = round(int(record["Value"]) / 1000000, 2)
            if year not in result:
                result[year] = {country: population}
            else:
                result[year][country] = population

    return result


def plot(data):
    """Plotting the parameters in the grouped bar chart"""
    years = list(data.keys())
    country_names = list(next(iter(data.values())).keys())
    x = list(range(len(years)))
    n_series = len(country_names)
    total_width = 0.8
    bar_width = total_width / n_series
    _, ax = plt.subplots(figsize=(9, 5))
    for i, country in enumerate(country_names):
        values = [data[year].get(country, 0) for year in years]
        offset = (i - (n_series - 1) / 2) * bar_width
        x_pos = [pos + offset for pos in x]
        ax.bar(x_pos, values, bar_width, label=country)

    ax.set_ylabel("Values")
    ax.set_title("Grouped bar chart")
    ax.set_xticks(x)
    ax.set_xticklabels(years)
    ax.legend(bbox_to_anchor=(1.02, 1), loc="upper left", borderaxespad=0)
    plt.tight_layout()
    plt.savefig("output/solution4.png", dpi=300)
    plt.show()


def execute(data):
    """Executing the calculation and plotting of the values"""
    result = calculate(data)
    plot(result)


execute(population_reader)
