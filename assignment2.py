file = open("city.txt","w+")
file.write("Hello World")
n = int(input("Enter the total number of cities"))
city = []
population = []
area = []
for i in range(n):
    city.append(input("Enter city name : "))
    population.append(float(input("Enter population : ")))
    area.append(float(input("Enter the area : ")))
final = zip(city,population,area)
final_list = list(final)
str_list = str(final_list)
file.write(str_list)
#file.write()