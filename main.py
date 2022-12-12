import openpyxl

from User import User









app_user_one = User("shabanzade", "maryam", "pwd1", 0, "Hatchback")
app_user_one.herzlich_welcome()
user_input =""
while user_input != "exit":

    app_user_one.get_number_family()
    app_user_one.get_offer_auto()
    app_user_one.get_select_car()
    app_user_one.get_calculate_price()
    app_user_one.get_calculate_auto_rabbatt()
    app_user_one.get_anzahle_auto()
    app_user_one.gesamt_preice()

    app_user_one.get_user_info()
    app_user_one.change_password("234")
    user_input = input("exit oder start: ")






