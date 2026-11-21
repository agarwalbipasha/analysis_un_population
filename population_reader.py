import csv


def population_reader():
    with open("data_population.csv", mode="r", encoding="utf-8") as csv_file:
        population = csv.DictReader(csv_file)
        yield from population


population_reader()
