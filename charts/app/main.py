import mod
import read_csv
import charts

def run():
    data = read_csv.read_csv('data.csv')
    data = list(filter(lambda item: item['Continent'] == 'South America', data))
    countries = list(map(lambda x: x['Country/Territory'], data))
    percentages = list(map(lambda x: x['World Population Percentage'], data))
    charts.generate_pie_chart(countries, percentages)
    
    country = input('Type Country => ').capitalize()

    result = mod.population_by_country(data, country)
    
    if len(result) > 0:
        country = result[0]
        labels, values = mod.get_population(country)
        charts.generate_bar_chart(country['Country/Territory'], labels, values)
    

if __name__ == '__main__': #Para manejar la dualidad de modulos, ya que solo se puede llamar a run en example.py y queremos que tambien se pueda correr aqui
    run()