class Vehicle:
    
    def __init__(self,brand,model,year,daily_price,insurance_Fee):
        self.brand=brand
        self.model=model
        self.year=year
        self.daily_price=daily_price
        self.insurance_Fee=insurance_Fee

    def calculate_rental_price(self,days):
         return (self.daily_price + self.insurance_Fee) * days

    def show_info(self):
        print("Brand: ",self.brand) 
        print("Model: ",self.model)
        print("Year: ",self.year)
        print("Daily_price: ",self.daily_price)
        print("insurance_Fee: ",self.insurance_Fee)

class Car(Vehicle):

    def __init__(self, brand, model, year, daily_price,insurance_Fee,number_of_doors):
        super().__init__(brand, model, year, daily_price,insurance_Fee)
        self.number_of_doors = number_of_doors

    def show_info(self):
        super().show_info()
        print(f"number_of_doors: {self.number_of_doors}")

car1=Car("Bmw","M4CSL",2023,1500,200,2)
car2=Car("Audi","RS7",2013,1000,130,4)
car3=Car("Mercedes","AMG GT63",2018,1250,170,4)

class Motorcycle(Vehicle):

    def __init__(self, brand, model, year, daily_price, insurance_Fee,engine_cc):
        super().__init__(brand, model, year, daily_price, insurance_Fee)
        self.engine_cc=engine_cc

    def show_info(self):
        super().show_info()
        print(f"engine_cc: {self.engine_cc}")

motor1=Motorcycle("Honda","WN7",2025,200,30,1000)         
motor2=Motorcycle("Yamaha","MT-09",2024,350,50,890)
motor3=Motorcycle("Bmw","S1000RR",2023,600,100,999)

class Truck(Vehicle):
    
    def __init__(self, brand, model, year, daily_price, insurance_Fee,cargo_capacity):
        super().__init__(brand, model, year, daily_price, insurance_Fee)
        self.cargo_capacity=cargo_capacity
    
    def show_info(self):
        super().show_info()
        print(f"cargo_capacity: {self.cargo_capacity}")

truck1=Truck("Mercedes","ACTROS",2024,3000,500,20)
truck2=Truck("Volvo","FH","2023",2800,450,25)
truck3=Truck("SCANIA","R500",2022,2900,480,24)

while True:
    Choice= input(""" ===== VEHİCLE RENTAL SYSTEM =====
1 - CAR
2 - MOTORCYCLE
3 - TRUCK 
=""")
      
    if Choice == "1":
       while True:
        print(" ==== AVAILABLE CARS ====")
        print()
        print("(1-)")
        car1.show_info()
        print()
        print("(2-)")
        car2.show_info()
        print()
        print("(3-)")
        car3.show_info()
        print()
        print()
        print("(1-) BMW M4CSL")
        print("(2-) AUDİ RS7")
        print("(3-) MERCEDES AMG GT63")
        print()
        car_choice = input("SELECT A CAR:")
        print()
        if car_choice == "1":
            selected = car1
        elif car_choice == "2":
            selected = car2
        elif car_choice == "3":
            selected =car3
        else:
            print("Invalid Select")
            continue
        selected.show_info()
        print()
        while True:
         try:
          days = int(input("How many days do you want to rent? "))
          if days <= 0:
            print("Please enter a positive number")
            continue
         except ValueError:
            print("Please enter a number ")
            continue
         print()
         print("Payment amount =",selected.calculate_rental_price(days))
         break

    elif Choice == "2":
       while True:
        print(" ==== AVAILABLE MOTORCYCLES ====")
        print()
        print("(1-)")
        motor1.show_info()
        print()
        print("(2-)")
        motor2.show_info()
        print()
        print("(3-)")
        motor3.show_info()
        print()
        print()
        print("(1-) Honda WN7 ")
        print("(2-) Yamaha MT-09")
        print("(3-) Bmw S1000RR")
        print()
        motor_choice = input("SELECT A MOTOR:")
        print()
        if motor_choice == "1":
            selected = motor1
        elif motor_choice == "2":
            selected = motor2
        elif motor_choice == "3":
            selected = motor3
        else:
            print("Invalid Select")
            continue
        selected.show_info()
        print()
        while True:
         try:
          days = int(input("How many days do you want to rent? "))
          if days <=0:
             print("Please enter a positive number")
         except ValueError:
            print("Please enter a number ")
            continue
         print()
         print("Payment amount =",selected.calculate_rental_price(days))
         break
        
    elif Choice == "3":
       while True:
        print("=== AVAILABLE TRUCK ====")
        print()
        print("(1-)")
        truck1.show_info()
        print()
        print("(2-)")
        truck2.show_info()
        print()
        print("(3-)")
        truck3.show_info()
        print()
        print()
        print("(1-) Mercedes Actors")
        print("(2-) Volvo 2023")
        print("(3-) SCANIA R500")
        print()
        truck_choice = input("SELECT A TRUCK:")
        print()
        if truck_choice == "1":
            selected = truck1 
        elif truck_choice == "2":
            selected = truck2
        elif truck_choice == "3":
            selected =truck3
        else:
            print("Invalid Select")
            continue
        selected.show_info()
        print()
        while True:
         try:
          days = int(input("How many days do you want to rent? "))
          if days <= 0:
            print("Please enter a positive number")
         except ValueError:
            print("Please enter a number ")
            continue
         print()
         print("Payment amount =",selected.calculate_rental_price(days))
         break
       
    else:
        print("Invalid Choice Please Try Again ")


        
        







