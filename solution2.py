"""For the year 2014 - Bar Chart of population of ASEAN countries"""

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
        year = record["Year"]
        country = record["Country Name"]
        population = record["Value"]
        if int(year) == 2014 and country in asean_countries:
            result[country] = int(population)

    countries = result.keys()
    population_int = result.values()
    popultation_millions = [round(value / 1000000, 2) for value in population_int]
    return countries, popultation_millions


def plot(country, populations):
    """Plotting the parameters in the bar chart"""
    plt.figure(figsize=(12, 7))
    plt.title("Population of ASEAN countries in 2014", fontsize=14, fontweight="bold")
    plt.bar(country, populations, color="turquoise", edgecolor="black")
    plt.xlabel("Country name", fontsize=12)
    plt.ylabel("Population (In Millions)", fontsize=12)
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig("output/solution2.png", dpi=300)
    plt.show()


def execute(data):
    """Executing the calculation and plotting of the values"""
    country, population = calculate(data)
    plot(country, population)


execute(population_reader)
