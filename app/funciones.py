import csv
import matplotlib.pyplot as plt

ruta_archivo = 'world_population.csv'

def reader_csv(ruta):
    with open(ruta,mode='r',encoding='utf-8') as archivo:
        lector = csv.reader(archivo,delimiter=',')
        header = next(lector)
        data = []
        
        for row in lector:
            iterable = zip(header,row)
            coutry_dict = {key: value for key,value in iterable}
            data.append(coutry_dict)
    return data


def get_population (country_dict):
    population_dict = {
        '2022': country_dict['2022 Population'],
        '2020': country_dict['2020 Population'],
        '2015': country_dict['2015 Population'],
        '2010': country_dict['2010 Population'],
        '2000': country_dict['2000 Population'],
        '1990': country_dict['1990 Population'],
        '1980': country_dict['1980 Population'],
        '1970': country_dict['1970 Population'],    
    }
    labels = population_dict.keys()
    values = population_dict.values()
    
    return labels, values


def population_by_country(data, country):
  result = list(filter(lambda item: item['Country/Territory'] == country, data))
  return result



def generate_bar_chart(name, labels, values):
  fig, ax = plt.subplots()
  ax.bar(labels, values)
  plt.savefig(f'./imgs/{name}.png')
  plt.close()
  
    
def charts_pie(labels,values):
    fig,ax = plt.subplots()
    ax.pie(values, labels = labels)
    ax.axis('equal')
    plt.savefig('pie.png')
    plt.close()
    
        
        
            
if __name__ == '__main__':
    data = reader_csv(ruta_archivo)
    print(data)