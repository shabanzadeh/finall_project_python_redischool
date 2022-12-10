class User:
    def __init__(self,name, user_email, password,numberOffamily,select_car_user):
        self.name = name
        self.email=user_email
        self.password=password
        self.numberOffamily=numberOffamily
        self.id_booking = 0
        self.select_car_user = select_car_user
        self.offer_auto = ""
        self.result=[]
    def get_number_family(self):
        for i in range(1):
            family=input("are you family: ja oder nein: ")

            if family=="nein":
                break
            else:
                numberOf_family=int(input("how many people did you consist of: "))
                self.numberOffamily=numberOf_family
    def change_password(self,new_password):
        self.password=new_password
    #def get_select_car(self,which_auto):
     #   self.select_car = which_auto

    def get_user_info(self):
        print(f"User {self.name} current nummber of family is {self.numberOffamily} and chose this car {self.select_car_user}")

    def get_offer_auto(self):

        while 1:
            if self.numberOffamily>=2:
                offer = input("I can offer you Hachback or SUV: please select your car otherweise write no: ")
                if offer == "Hachback" or offer=="SUV":
                    break

                else:
                    offer = input("I can offer you Luxy or SUV: please select your car otherweise write no: ")
                    if offer == "no":
                        continue

                    self.offer_auto=offer
                    return self.offer_auto

    #def get_select_car(self):
     #   print(self.offer_auto)
      #  neu_select_car_user = input(" Please choose the car you want: ")
       # self.select_car_user = neu_select_car_user
        #return self.select_car_user


    def get_calculate_price(self,price):
        print(price)
    def get_calculate_auto_rabbatt(self):
        if self.numberOffamily>=2:
            self.price = self.price * 0.3
        else:
            self.price = self.price
            return self.price
    def anzahl_booking(self):
        if self.numberOffamily>4 or self.select_car_user == "":
            anzahle_auto = 2
            return anzahle_auto

        else:
            anzahle_auto= 1
            return anzahle_auto


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









