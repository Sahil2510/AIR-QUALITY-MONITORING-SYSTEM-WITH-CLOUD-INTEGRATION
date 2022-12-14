print("Python Random Number Generator")

#Random Number Library
import random
#Pandas for excel export
import pandas

#--------------EDIT THOSE FIRST-----------------#
#Export File Name
export_file = "DBMS_Mini_Project_Database_Test.xlsx"

#Total Random Numbers to be generated
random_number_limit = 10000
count = 1

#Temperature limits in Celcius
TLow = 26   #Temperature lower limit
THigh = 35  #Temperature higher limit

#Humidity Limits in g/m3
HLow = 80   #Humidity lower limit
HHigh = 99  #Humidity Upper Limit

#PM2.5 Limits in ug/m3
PMLow = 0   #PM2.5 lower limit
PMHigh = 800   #PM2.5 upper limit


#example variables: temperature, humidity, CO2, CO, SO2, PM2.5
#variable limits: Temp -> 28-40 C, Hum -> 80-100 g/kg, PM2.5 -> 0-800 ug/m3 

#Initialization of list variables
temp_list = []
humidity_list = []
PM_list = []


while count <= random_number_limit:
    #Temperature Random Function
    temp = random.randint(TLow,THigh)
    temp_list.append(temp)
    
    #Humidity Random Function
    humidity = random.randint(HLow,HHigh)
    humidity_list.append(humidity)
    
    #PM2.5 Random Function
    PM = random.randint(PMLow,PMHigh)
    PM_list.append(PM)
    
    count = count + 1


#Pandas Exprort Function
export = pandas.DataFrame({'Temperature': temp_list, 'Humidity': humidity_list, "PM2.5": PM_list}, index=None)
export.to_excel(export_file, index = False)


#Display Function
def display():
    print ("\nTemperature = ", temp_list)
    print ("\nHumidity = ", humidity_list)
    print ("\nPM2.5 = ", PM_list)

print("\nExported to ", export_file)
