import openpyxl

from User import User

car_file =openpyxl.load_workbook("Car_Rantal.xlsx")

car_list =car_file['Tabelle1']
#how many type car is available
car_per_name = {}
car_per_passagiere = {}
print(car_list.max_row)
for car_row in range(2, car_list.max_row + 1):
    type_car = car_list.cell(car_row,5).value
    number_passengers = car_list.cell(car_row, 3).value
   # print(type_car)
    if type_car in car_per_name:
        current_name_product= car_per_name[type_car]
        car_per_name[type_car]=current_name_product +1
# calculate type with number of passengers
        car_per_passagiere[type_car]=number_passengers
    else:
        car_per_name[type_car] =1
#print(car_per_name)
print("Herzlichen welcomen in Car rental")

print(f"see available taxis at the moment with copacity: {car_per_passagiere}")
# how many type car with number of passasigere



app_user_one =User("shabanzade","maryam shabanzadeh","pwd1","5","BMV")
app_user_one.get_user_info()
app_user_one.change_password("234")
import pandas as pd
#import matplotlib.pyplot as plt

from datetime import date
from pathlib import Path
from datetime import datetime
#read the file
#data_1 = pd.read_csv("/Car_Rantal.txt")
#print(data_1.shape)
#print(data_1.head(10))


#df = pd.read_csv('/Car_Rantal.txt')
#print(df)
#df.head(5)


