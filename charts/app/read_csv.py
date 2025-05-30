import csv

def read_csv(path):
    with open(path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',') #el delimiter puede ser , o ; dependiendo de lo que separe cada dato en el csv que se use
        header = next(reader)
        data = []
        for row in reader: #convierte cada columna de datos en un array
            iterable = zip(header, row)
            country_dict = {key: value for key, value in iterable}
            data.append(country_dict)
        return data

if __name__ == '__main__':
    data = read_csv('./Modulos_Propios/data.csv')
    print(data[0]) #Usando [] podemos ver cada diccionario por separado
