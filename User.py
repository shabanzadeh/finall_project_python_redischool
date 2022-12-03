class User:
    def __init__(self,name, user_email, password, number_family,select_car):
        self.name = name
        self.email=user_email
        self.password=password
        self.number_family =number_family
        self.select_car = select_car

    def change_password(self,new_password):
        self.password=new_password
    def get_select_car(self,select_car_user):
        self.select_car = select_car_user
    def get_user_info(self):
        print(f"User {self.name} current have a {self.number_family}")
    def get_calculate_price(self,price):
        print(price)
    def get_calculate_auto_rabbatt(self):
        if (self.number_family>=3):
            self.price = self.price/3.3
        else:
            self.price = self.price




