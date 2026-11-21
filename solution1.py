"""Make a Bar Plot of 'population of India' vs. years."""

import matplotlib.pyplot as plt

from population_reader import population_reader


def calculate(data):
    """Extracting the population vs year of India"""
    result = {}
    for record in data():
        country = record["Country Name"]
        if country == "India":
            year = record["Year"]
            population = int(record["Value"])
            if year not in result:
                result[year] = round(population / 100000000, 2)
    years = result.keys()
    population_value = result.values()
    return years, population_value


def plot(year, populations):
    """Plotting the parameters in the bar chart"""
    plt.figure(figsize=(12, 7))
    plt.title("Population of India vs years", fontsize=14, fontweight="bold")
    plt.bar(year, populations, color="turquoise", edgecolor="black")
    plt.xlabel("Year", fontsize=12)
    plt.ylabel("Population (In Ten Crores)", fontsize=12)
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig("output/solution1.png", dpi=300)
    plt.show()


def execute(data):
    """Executing the calculation and plotting of the values"""
    year, population = calculate(data)
    plot(year, population)


execute(population_reader)
