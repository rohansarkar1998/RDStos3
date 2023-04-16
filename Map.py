import csv

import pymysql


class City:
    def __init__(self, ID, Name, CountryCode, District, Population):
        self.ID = ID
        self.Name = Name
        self.CountryCode = CountryCode
        self.District = District
        self.Population = Population


Citydetails = []
dbHost = "192.168.0.5"
dbUser = "app"
dbPass = "password"
dbName = "world"
mydb = pymysql.connect(host=dbHost, user=dbUser, password=dbPass, database=dbName)
mycorsor = mydb.cursor()
mycorsor.execute("select * from city")
name = mycorsor.fetchall()



field = ['Id', 'Name', 'Countrycode', 'Dist', 'Population']
filename = 'City.csv'
with open(filename, 'w', encoding='utf8', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(field)
    for i in name:
        csvwriter.writerow(i)

