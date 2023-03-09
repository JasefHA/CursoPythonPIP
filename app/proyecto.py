import read_csv 
import chart

path = './app/data.csv'
data_csv = read_csv.read_csv(path)


if __name__ == '__main__':
  #labels, values = read_csv.get_labels_and_values_poblacion_country(data_csv)
  countries, percentages = read_csv.get_world_percentages(data_csv)
  #chart.generate_bar_chart(labels, values)
  #print(labels)
  #print(values)
  #print(countries)
  #print(percentages)
  chart.generate_pie_chart(countries, percentages)
  



      


    
    
    