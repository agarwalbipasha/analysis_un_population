"""Plot a BAR CHART of Total SAARC population vs year"""

import matplotlib.pyplot as plt

from population_reader import population_reader


def calculate(data):
    """Extracting the population of ASEAN countries for 2014"""
    result = {}
    saarc_countries = [
        "Afghanistan",
        "Bangladesh",
        "Bhutan",
        "India",
        "Maldives",
        "Nepal",
        "Pakistan",
        "Sri Lanka",
    ]
    for record in data():
        year = int(record["Year"])
        country = record["Country Name"]
        if country in saarc_countries:
            population = int(record["Value"])
            if year not in result:
                result[year] = population
            else:
                result[year] += population
    years = result.keys()
    population_int = result.values()
    population_billions = [round(value / 1000000000, 2) for value in population_int]
    return years, population_billions


def plot(year, populations):
    """Plotting the parameters in the bar chart"""
    plt.figure(figsize=(12, 7))
    plt.title("Population of SAARC countries vs years", fontsize=14, fontweight="bold")
    plt.bar(year, populations, color="turquoise", edgecolor="black")
    plt.xlabel("Year", fontsize=12)
    plt.ylabel("Population (In Billions)", fontsize=12)
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig("output/solution3.png", dpi=300)
    plt.show()


def execute(data):
    """Executing the calculation and plotting of the values"""
    year, population = calculate(data)
    plot(year, population)


execute(population_reader)
