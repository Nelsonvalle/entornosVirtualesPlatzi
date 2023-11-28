from funciones import charts_bar,charts_pie
from funciones import reader_csv
from funciones import get_population
from funciones import population_by_country



def run():
    ruta_archivo = 'world_population.csv'
    data = reader_csv(ruta_archivo)
    data = list(filter(lambda item: item['Continent']== 'South America',data))
    
    countries = list(map(lambda x: x['Country/Territory'],data))
    percentages = list(map(lambda x: x['World Population Percentage'],data))
    charts_pie(countries,percentages)
    
    opcion = input('Ingrese un pais latinoAmericano: ')
    
    result = population_by_country(data,opcion)
    
    if len(result) > 0:
        country = result[0]
        labels, values = get_population(country)
        charts_bar(labels,values)
        

if __name__ == '__main__':
    run()