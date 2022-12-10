import openpyxl

from User import User


car_file =openpyxl.load_workbook("Car_Rantal.xlsx")

car_list =car_file['Tabelle1']
#how many type car is available
car_per_name = {}
car_per_passagiere={}
car_price_type = {}
dicount_car={}



for car_row in range(2, car_list.max_row + 1):
    number_passengers = car_list.cell(car_row, 3).value
    preis_car=car_list.cell(car_row,7).value
    type_car =car_list.cell(car_row,5).value




   # print(type_car)
    if type_car in car_per_name:
        current_name_product= car_per_name[type_car]
        car_per_name[type_car]=current_name_product +1

# calculate type with number of passengers
        car_per_passagiere[type_car]=number_passengers
    else:
        car_per_name[type_car] =1
    if type_car in car_price_type:
        current_total_price =car_price_type.get(type_car)
        car_price_type[type_car]=preis_car
        dicount_car[type_car]=0.3*preis_car
    car_price_type[type_car]=preis_car
    dicount_car[type_car]=0.3 * preis_car


#type_car_list =[]
#for i in total_numberCar_dic:
 #   type_car_list.append(i)




#print("Herzlichen welcomen in Car rental\n")

#print(f"see available taxis at the moment with copacity: {car_per_passagiere}\n")
#print(f"Car rental price in one day {car_price_type}\n")
#print(f"if the car is reserved as a family, we have a 30% discount for you: {dicount_car} Euro \n")



user_input =""
while user_input != "exit":
    print("Herzlichen welcomen in Car rental\n")

    print(f"see available taxis at the moment with copacity: {car_per_passagiere}\n")
    print(f"Car rental price in one day {car_price_type}\n")
    print(f"if the car is reserved as a family, we have a 30% discount for you: {dicount_car} Euro \n")
    app_user_one = User("shabanzade", "maryam", "pwd1", 0, "Hatchback")
    app_user_one.get_number_family()
    app_user_one.get_offer_auto()
    app_user_one.get_select_car()
    #app_user_one.get_calculate_auto_rabbatt()
    app_user_one.get_user_info()
    app_user_one.change_password("234")
    user_input = input("exit oder start: ")






