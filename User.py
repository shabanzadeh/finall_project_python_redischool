import openpyxl
class User:
    car_file = openpyxl.load_workbook("Car_Rantal.xlsx")
    car_list = car_file['Tabelle1']
    print(car_list)
    car_per_name = {}
    car_per_passagiere = {}
    car_price_type = {}
    dicount_car = {}
    for car_row in range(2, car_list.max_row + 1):
        number_passengers = car_list.cell(car_row, 3).value
        preis_car = car_list.cell(car_row, 7).value
        type_car = car_list.cell(car_row, 5).value
        if type_car in car_per_name:
            current_name_product = car_per_name[type_car]
            car_per_name[type_car] = current_name_product + 1

            # calculate type with number of passengers
            car_per_passagiere[type_car] = number_passengers
        else:
            car_per_name[type_car] = 1
        if type_car in car_price_type:
            current_total_price = car_price_type.get(type_car)
            car_price_type[type_car] = preis_car
            dicount_car[type_car] = 0.3 * preis_car
        car_price_type[type_car] = preis_car
        dicount_car[type_car] = 0.3 * preis_car

    def __init__(self,name, user_email, password,numberOffamily,select_car_user):
        self.name = name
        self.email=user_email
        self.password=password
        self.numberOffamily=numberOffamily
        self.id_booking = 0
        self.select_car_user = select_car_user
        self.offer_auto = ""
        self.price = 0
        self.discount=0


    def get_number_family(self):
        for i in range(1):
            family=input("are you family: yes oder no: ")

            if family=="no":


                break
            else:
                try:
                    numberOf_family=int(input("how many people did you consist of: "))
                    self.numberOffamily = numberOf_family
                except ValueError:
                    print("you can to write just string")
                    numberOf_family = int(input("how many people did you consist of: "))



    def change_password(self,new_password):
        self.password=new_password
    #def get_select_car(self,which_auto):
     #   self.select_car = which_auto




    def get_offer_auto(self):
        while 1:
            if self.numberOffamily >= 2:
                offer = input("I can offer you Hachback or SUV: please select your car otherweise write no: ")
                if offer == "Hachback".lower() or offer == "SUV".lower():
                    self.offer_auto = offer
                    break

            else:
                offer = input("I can offer you Luxy or SUV: please select your car otherweise write no: ")
                self.offer_auto = offer
                break

        return self.offer_auto


    def get_select_car(self):
         #neu_select_car_user = input(" Please choose the car you want: ")
        self.select_car_user = self.offer_auto
        return self.select_car_user


    def get_calculate_price(self,car_price_type):
        if self.offer_auto=="hachback":
            price1 =car_price_type['Hatchback']
        elif self.offer_auto=="suv":
            price1 = car_price_type["SUV"]
        elif self.offer_auto=="sendan":
            price1=car_price_type["Hatchback"]
        else:
            price1=car_price_type["Sendan"]
        self.price=price1
        return self.price

    def get_calculate_auto_rabbatt(self):
        if self.numberOffamily >= 2:
            self.discount =(self.price) - (self.price * 0.3)
        else:
            self.discount=self.price
        return self.discount



    def get_user_info(self):
        print(f"User {self.name} current nummber of family is {self.numberOffamily}"
              f" and chose {self.offer_auto} car price ist {self.price} Euro per days and mit discount {self.discount}, per days! ")






    def exist_booking_auto(self,anzahle_auto,total_numberCar_list):

        for x in total_numberCar_list:
            if anzahle_auto>=2 or total_numberCar_list>=2:
                result =total_numberCar_list[0] or total_numberCar_list[2]  or total_numberCar_list[3]
                return self.result.append(result)
            elif total_numberCar_list>=1:
                result=total_numberCar_list[0]
                return self.result.append(result)

    def booking_info(self):
        print(f"haben für dich auto {self.result} zur verfügung")

    # def arrange_booking(self,anzahl_ auto):









